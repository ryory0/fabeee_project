import streamlit as st
import requests
from PIL import Image, ImageOps
from io import BytesIO

product_api_url = "http://django-back:8000/api/product/"
recipe_api_url = "http://django-back:8000/api/recipe/"

# APIからデータを取得
def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("APIからデータを取得できませんでした。")
        return []

products = fetch_data(product_api_url)
recipes = fetch_data(recipe_api_url)

# 画像を表示するための関数
def display_image(url):
    try:
        image_response = requests.get(url)
        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            # 画像のアスペクト比を統一（200x150ピクセルに固定）
            image = ImageOps.fit(image, (800, 600))
            st.image(image, use_column_width=True)
        else:
            st.error("画像を取得できませんでした。")
    except Exception as e:
        st.error(f"画像の読み込み中にエラーが発生しました: {e}")

# ヘッダー
def header(subheader):
    st.title("Fudo Food")
    st.text_input(label=' ', placeholder="検索")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("ショッピング", use_container_width=True): st.switch_page('pages/home.py')
    with col2:
        if st.button("レシピ", use_container_width=True): st.switch_page('pages/recipe.py')
    with col3:
        if st.button("トピック", use_container_width=True): st.switch_page('pages/topic.py')
    st.divider()
    st.subheader(subheader)
    st.divider()

# 保持変数 初期化
if 'select_data' not in st.session_state: st.session_state.select_data = {"title":"エラー"} # 選択された項目
if 'had_data' not in st.session_state: st.session_state.had_data = {"title":"エラー"} # ページ遷移前に選択されていた項目
if "can_move" not in st.session_state: st.session_state.can_move = False                  # ページ遷移フラグ
if "had_page" not in st.session_state: st.session_state.had_page = "エラー"                # ページ遷移前のページ（「商品詳細→レシピ詳細」 or 「レシピ一覧→レシピ詳細」の区別 戻るボタンで必要）

# サイドバーに表示
def side_view(num):
    st.session_state.select_data = products[num]
    with st.sidebar:
        st.title(products[num]["title"]) # 商品名
        st.divider()
        display_image(products[num]["image"]) # 画像表示
        st.subheader(products[num]["title"]) # 商品名
        st.title(f'¥ {products[num]["price"]}') # 価格
        st.divider()
        st.write("**商品の説明**")
        st.write(products[num]["description"]) # 商品情報
        st.divider()
        st.button("続きを見る", key='can_move', use_container_width=True)

# 商品一覧
def product_display(width, height):
    num = 0
    total_items = len(products)  # 商品の総数を取得
    while num < total_items:
        cols = st.columns(width)  # 列を定義
        for col in cols:
            if num >= total_items:
                break  # num が商品リストの範囲を超えたらループを終了
            with col:
                display_image(products[num]['image'])  # 画像を表示
                if st.button(f"{products[num]['title']}\n\n¥ {products[num]['price']}", key=products[num]["id"], use_container_width=True):
                    side_view(num)
                num += 1


# サイドバーに表示（レシピ）
def side_view_recipe(num):
    st.session_state.select_data = recipes[num]
    st.session_state.had_page = "recipe"
    with st.sidebar:
        st.title(recipes[num]["title"])                   # レシピ名
        st.divider()
        display_image(recipes[num]["image"])                # 画像
        st.write(recipes[num]["description"])                   # 説明
        st.divider()
        st.button("続きを見る", key="can_move", use_container_width=True)


# レシピ一覧
def recipe_display(width, height):
    num = 0
    for col in st.columns(width):
        with col:
            for row in range(height):
                if num < len(recipes):
                    display_image(recipes[num]['image'])  # 画像を表示
                    if st.button(recipes[num]["title"], key=recipes[num]["id"], use_container_width=True):
                        side_view_recipe(num)
                    num += 1
                else:
                    break  # レシピがリストの範囲を超えた場合、ループを終了

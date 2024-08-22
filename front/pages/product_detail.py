import streamlit as st
import requests
from PIL import Image, ImageOps
from io import BytesIO
import time
from package import module  # 自作モジュールをインポート

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

# APIからレシピデータを取得する関数
def fetch_recipe_data(recipe_id):
    recipe_api_url = f"http://django-back:8000/api/recipe/{recipe_id}/"
    response = requests.get(recipe_api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"レシピID {recipe_id} のデータを取得できませんでした。")
        return None

# 商品詳細ページ
module.header("ショッピング")  # ヘッダー

if st.button("＜　ホーム"):
    st.session_state.select_data = None
    st.switch_page("pages/home.py")

try:
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.select_data['image']:
            display_image(st.session_state.select_data['image'])  # 画像表示
        else:
            st.error("画像が見つかりません。")
    with col2:
        st.subheader(f"**{st.session_state.select_data['title']}**")  # 商品名
        st.title(f"¥ {st.session_state.select_data['price']}")  # 価格
        if st.button("購入手続きへ", use_container_width=True):
            st.session_state.purchase_data = st.session_state.select_data
            st.switch_page("pages/purchase.py")
        st.divider()
        st.write("**商品の説明**")
        st.write(st.session_state.select_data["description"])  # 商品情報

    st.divider()

    # 関連レシピ
    st.subheader("関連レシピ")
    recipe_ids = st.session_state.select_data.get('recipes', [])
    cols = st.columns(4)  # 4列に設定

    for i, recipe_id in enumerate(recipe_ids):
        recipe_data = fetch_recipe_data(recipe_id)
        if recipe_data:
            col = cols[i % 4]  # 4列に均等に配置
            with col:
                if recipe_data.get('image'):
                    display_image(recipe_data['image'])  # 画像表示
                else:
                    st.error("レシピの画像が見つかりません。")
                # ページ遷移（レシピ詳細ページ）
                if st.button(recipe_data['title'], key=recipe_data['id'], use_container_width=True):
                    st.session_state.had_data = st.session_state.select_data
                    st.session_state.select_data = recipe_data
                    st.session_state.had_page = "product_detail"
                    st.switch_page('pages/recipe_detail.py')

except Exception as e:
    st.warning("**エラー**\n\n申し訳ございません。\n\nブラウザの「ページ更新」や「戻る・進む」を押すとページを表示できません。\n\n5秒後に自動で画面が切り替わります。")
    time.sleep(5)
    st.switch_page("pages/home.py")  
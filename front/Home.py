import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from package import module  # 自作モジュールをインポート

product_api_url = "http://django-back:8000/api/product/"

# APIからデータを取得
product_response = requests.get(product_api_url)
if product_response.status_code == 200:
    products = product_response.json()
else:
    st.error("APIからデータを取得できませんでした。")
    products = []

module.header("ショッピング")  # ヘッダー

# 保持変数 初期化
if 'page' not in st.session_state:
    st.session_state.page = 'home'
    st.session_state.selected_product = None

if 'can_move' not in st.session_state: 
    st.session_state.can_move = False

# ページ遷移用関数
def navigate_to(page, product=None):
    st.session_state.page = page
    st.session_state.selected_product = product

# サイドバー
def side_view(product):
    with st.sidebar:
        st.title(product["title"])  # 商品名
        st.divider()
        image_url = product["image"]
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            try:
                # バイトストリームを使用して画像を開く
                image = Image.open(BytesIO(image_response.content))
                st.image(image, use_column_width=True)  # 画像を表示
            except Exception as e:
                st.error(f"画像を開く際にエラーが発生しました: {e}")
        else:
            st.error(f"画像を取得できませんでした: {product['title']}")

        st.subheader(product["title"])  # 商品名
        st.title(f'¥ {product["price"][:-3]}')  # 価格
        st.divider()
        st.write("**商品の説明**")
        #st.write(product["description"])  # 商品情報
        st.divider()
        if st.button("続きを見る", key='can_move', use_container_width=True):
            navigate_to('product_page', product=product)

# 商品カードを表示
cols = st.columns(3)  # 3列レイアウト

for i, product in enumerate(products):
    with cols[i % 3]:  # 各列に商品を配置
        try:
            image_url = product['image']

            # 画像を取得
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                try:
                    # バイトストリームを使用して画像を開く
                    image = Image.open(BytesIO(image_response.content))
                    st.image(image, use_column_width=True)

                    # 商品タイトルと価格をボタンにして配置
                    if st.button(f"{product['title']}\n\n¥ {product['price'][:-3]}", key=f"image_{product['id']}", use_container_width=True):
                        side_view(product)
                except Exception as e:
                    st.error(f"画像を開く際にエラーが発生しました: {e}")
            else:
                st.error(f"画像を取得できませんでした: {product['title']}")
        except Exception as e:
            st.error(f"画像を表示中にエラーが発生しました: {e}")

# ページ遷移
if st.session_state.page == 'product_page':
    product = st.session_state.selected_product
    if product:
        st.title(product["title"])
        side_view(product)  # サイドバーでの詳細表示も継続
    else:
        st.warning("商品が選択されていません。")
        if st.button("ホームに戻る"):
            navigate_to('home')

if st.session_state.can_move: 
    st.switch_page('pages/detail.py')

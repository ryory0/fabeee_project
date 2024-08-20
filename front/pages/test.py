import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Django APIのURL
product_api_url = "http://django-back:8000/api/product/"
recipe_api_url = "http://django-back:8000/api/recipe/"

# 初期ページ設定
if 'page' not in st.session_state:
    st.session_state.page = 'home'
    st.session_state.selected_product = None
    st.session_state.selected_recipe = None

# ページ遷移用関数
def navigate_to(page, product=None, recipe=None):
    st.session_state.page = page
    st.session_state.selected_product = product
    st.session_state.selected_recipe = recipe

# APIからデータを取得
product_response = requests.get(product_api_url)
if product_response.status_code == 200:
    products = product_response.json()
else:
    st.error("APIからデータを取得できませんでした。")
    products = []

recipe_response = requests.get(recipe_api_url)
if recipe_response.status_code == 200:
    recipes = recipe_response.json()
else:
    st.error("レシピのAPIからデータを取得できませんでした。")
    recipes = []

# ホームページ
if st.session_state.page == 'home':
    st.title("FudoMarket")

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st.write("ニュース")
    with col2:
        st.text_input("検索", placeholder="検索キーワードを入力")
    with col3:
        st.button("検索")

    # 商品のカードを表示
    cols = st.columns(3)  # 3列レイアウト

    for i, product in enumerate(products):
        with cols[i % 3]:  # 各列に商品を配置
            try:
                # 画像を取得して表示
                image_response = requests.get(product['image'])
                if image_response.status_code == 200:
                    image = Image.open(BytesIO(image_response.content))
                    if st.button(product['title'], key=f"image_{product['id']}"):
                        navigate_to('product_page', product=product)
                    st.image(image, caption=product['title'], use_column_width=True)
                else:
                    st.error(f"画像を取得できませんでした: {product['title']}")
            except Exception as e:
                st.error(f"画像を表示中にエラーが発生しました: {e}")
            
            st.write(f"商品名: {product['title']}")
            st.write(f"値段: ¥{product['price'][:-3]}")

# 商品詳細ページ
elif st.session_state.page == 'product_page':
    product = st.session_state.selected_product
    if product:
        st.title("商品ページ")

        # 商品画像表示
        try:
            image_response = requests.get(product['image'])
            if image_response.status_code == 200:
                image = Image.open(BytesIO(image_response.content))
                st.image(image, caption=product['title'], use_column_width=True)
            else:
                st.error(f"画像を取得できませんでした: {product['title']}")
        except Exception as e:
            st.error(f"画像を表示中にエラーが発生しました: {e}")

        # 商品名と価格
        st.write(f"商品名: {product['title']}")
        st.write(f"値段: ¥{product['price'][:-3]}")

        # レシピを表示
        st.write("関連するレシピ:")
        recipe_cols = st.columns(3)  # 3列レイアウト

        # ProductのレシピIDと一致するレシピを表示
        for i, recipe_id in enumerate(product['recipes']):
            recipe = next((r for r in recipes if r['id'] == recipe_id), None)
            if recipe:
                with recipe_cols[i % 3]:
                    try:
                        # 画像を取得して表示
                        image_response = requests.get(recipe['image'])
                        if image_response.status_code == 200:
                            image = Image.open(BytesIO(image_response.content))
                            if st.button(recipe['title'], key=f"recipe_{recipe['id']}"):
                                navigate_to('recipe_page', recipe=recipe)
                            st.image(image, caption=recipe['title'], use_column_width=True)
                        else:
                            st.error(f"画像を取得できませんでした: {recipe['title']}")
                    except Exception as e:
                        st.error(f"画像を表示中にエラーが発生しました: {e}")
            else:
                st.warning(f"レシピID {recipe_id} に対応するレシピが見つかりませんでした。")

        # カートと購入ボタン
        st.button("カートに入れる", key="cart")
        st.button("購入へ", key="purchase")

        # 戻るボタン
        if st.button("ホームに戻る"):
            navigate_to('home')
    else:
        st.warning("商品が選択されていません。")
        if st.button("ホームに戻る"):
            navigate_to('home')

# レシピ詳細ページ
elif st.session_state.page == 'recipe_page':
    recipe = st.session_state.selected_recipe
    if recipe:
        st.title(recipe['title'])

        # レシピ画像表示
        try:
            image_response = requests.get(recipe['image'])
            if image_response.status_code == 200:
                image = Image.open(BytesIO(image_response.content))
                st.image(image, caption=recipe['title'], use_column_width=True)
            else:
                st.error(f"画像を取得できませんでした: {recipe['title']}")
        except Exception as e:
            st.error(f"画像を表示中にエラーが発生しました: {e}")

        # レシピの詳細情報
        st.write(recipe['description'])

        # 戻るボタン
        if st.button("商品ページに戻る"):
            navigate_to('product_page', product=st.session_state.selected_product)
    else:
        st.warning("レシピが選択されていません。")
        if st.button("商品ページに戻る"):
            navigate_to('product_page', product=st.session_state.selected_product)
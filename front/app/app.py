import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlencode

# Django APIのURL
api_url = "http://django-back:8000/api/recipe/"

# APIからデータを取得
response = requests.get(api_url)
data = response.json()

# クエリパラメータから選択されたレシピIDを取得
query_params = st.query_params
selected_recipe_id = query_params.get("recipe_id", [None])[0]

if selected_recipe_id:
    # 選択されたレシピを表示
    recipe = next((r for r in data if r["id"] == int(selected_recipe_id)), None)
    
    if recipe:
        title = recipe['title']
        image_url = recipe['image']
        description = recipe['description']
        comments = recipe.get('comments', [])

        # 画像データを取得
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))

        # Streamlitで表示
        st.image(image, caption=title, use_column_width=True)
        st.write(description)
        
        # コメントを表示
        st.subheader("コメント")
        if comments:
            for comment in comments:
                st.write(f"- {comment['created_at']}")
                st.write(f"{comment['context']}")
        else:
            st.write("コメントはまだありません。")
        
        # 戻るボタン
        if st.button("戻る"):
            st.experimental_set_query_params()
else:
    # レシピ一覧を表示
    st.title("レシピ一覧")
    
    for recipe in data:
        title = recipe['title']
        image_url = recipe['image']
        recipe_id = recipe['id']

        # 画像をクリック可能にしてリンクを設定
        link_url = "?" + urlencode({"recipe_id": recipe_id})
        st.markdown(f"[![{title}]({image_url})]({link_url})")
        st.write(f"{title}")
        st.write("---")

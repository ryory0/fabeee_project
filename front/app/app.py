import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Django APIのURL
api_url = "http://django-back:8000/api/recipe/"

# APIからデータを取得
response = requests.get(api_url)
data = response.json()[0]

# レシピごとにデータを表示
for recipe in data:
    title = recipe['title']
    image_url = recipe['image']
    description = recipe['description']

    # 画像データを取得
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    # Streamlitで表示
    st.header(title)
    st.image(image, caption=title, use_column_width=True)
    st.write(description)
    st.write("---")  # 区切り線
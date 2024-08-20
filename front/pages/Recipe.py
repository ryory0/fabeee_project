import streamlit as st
from package import module

recipe_api_url = "http://django-back:8000/api/recipe/"

module.header("レシピ") # ヘッダー

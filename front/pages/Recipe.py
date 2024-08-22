import streamlit as st
from package import module
from PIL import Image

# レシピページ
st.set_page_config(layout="wide")                          # ワイドモード
st.image(Image.open("img/sub.png"), use_column_width=True) # サブビジュアル
module.header("レシピ")    

# 保持変数 初期化
if 'can_move' not in st.session_state: st.session_state.can_move = False

# レシピ一覧
module.recipe_display(3,3)

# ページ遷移（サイドバー → レシピ詳細ページ）
if st.session_state.can_move: st.switch_page('pages/recipe_detail.py')
import streamlit as st
from PIL import Image
from package import module  # 自作モジュールをインポート




# ホームページ
st.set_page_config(layout="wide")                           # ワイドモード
st.image(Image.open("img/main.png"), use_column_width=True) # メインビジュアル
module.header("ショッピング")                                # ヘッダー

# 保持変数 初期化
if "can_move" not in st.session_state: st.session_state.can_move = False # ページ遷移フラグ

# 商品一覧
module.product_display(3,2)

# ページ遷移（サイドバー → 商品詳細ページ）
if st.session_state.can_move: st.switch_page("pages/product_detail.py")
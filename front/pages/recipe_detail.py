import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from io import BytesIO
import time
import requests
from package import module  # 自作モジュールをインポート

# レシピ詳細ページ
st.set_page_config(layout="wide")                          # ワイドモード
st.image(Image.open("img/sub.png"), use_column_width=True) # サブビジュアル
module.header("レシピ")                                     # ヘッダー

try :
    button_label = "＜　"
    button_label += "レシピ" if st.session_state.had_page == 'recipe' else st.session_state.had_data['title']
    if st.button(button_label):
        if st.session_state.had_page == 'product_detail':
            st.session_state.select_data = st.session_state.had_data
            st.session_state.had_data = 'エラー'
        st.switch_page(f'pages/{st.session_state.had_page}.py')  # 戻るボタン

    col1, col2 = st.columns(2)
    with col1:
        # 画像URLから画像データを取得
        image_url = st.session_state.select_data['image']
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, use_column_width=True)  # 画像を表示

    with col2:
        st.subheader(f"**{st.session_state.select_data['title']}**")  # レシピ名
        st.write(st.session_state.select_data['description'])  # 説明
    st.divider()
    st.write("**材料（１人分）**")
    st.write(st.session_state.select_data["ingredients"]) # 材料
    st.divider()
    st.write("**料理手順**")
    st.write(st.session_state.select_data['process'])
    st.divider()

except Exception as e:
    st.warning("**エラー**\n\n申し訳ございません。\n\nブラウザの「ページ更新」や「戻る・進む」を押すとページを表示できません。\n\n5秒後に自動で画面が切り替わります。")
    time.sleep(5)
    st.switch_page("pages/recipe.py")
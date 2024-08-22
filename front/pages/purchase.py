import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from package import module # 自作モジュールをインポート
import time

# 画像を表示する関数
def display_image(url=None, image_file=None, use_column_width=True):
    if url:
        try:
            image_response = requests.get(url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, use_column_width=use_column_width)
        except Exception as e:
            st.error(f"画像を表示できませんでした: {e}")
    elif image_file:
        try:
            image = Image.open(image_file)
            st.image(image, use_column_width=use_column_width)
        except Exception as e:
            st.error(f"画像を開けませんでした: {e}")
    else:
        st.error("画像のURLまたはファイルが指定されていません。")

# 購入ページ
st.set_page_config(layout="wide") # ワイドモード
display_image(image_file="img/sub.png") # サブビジュアル
module.header("購入手続き") # ヘッダー



try:
    # 戻るボタン
    if st.button(f'＜　{st.session_state.purchase_data["title"]}'):
        st.switch_page("pages/product_detail.py")
    
    # 購入商品
    col1, col2, col3, col4 = st.columns([1, 3, 1, 5])
    with col2:
        display_image(url=st.session_state.purchase_data["image"]) # 画像
    with col4:
        st.subheader(f'**{st.session_state.purchase_data["title"]}**') # 商品名
        col1, col2, col3 = st.columns([1.5,1,5])
        with col1: st.title(f'¥ {st.session_state.purchase_data["price"]}') # 価格
        with col2:
            st.write('')
            st.write('')
            st.write("送料込み")
    st.divider()

    # クーポン
    st.text_input("**クーポンコード**")
    col1, col2, col3, col4 = st.columns([6,1.5,1.5,1])
    with col2:
        st.write('')
        st.write('')
        st.write("**ポイントの使用**")
    with col3: pt = st.number_input(" ", min_value=0, ) # ポイント使用
    with col4:
        st.write('')
        st.write('')
        st.write("**pt**")
    st.divider()

    # 支払方法
    st.selectbox("**支払方法**", ["コンビニ支払い", "あと払い・クレジットカード払い", "PayPay", "d払い", "au/UQ mobile", "ソフトバンクまとめて支払い", "Apple Pay", "FamiPay"])
    
    price = int(st.session_state.purchase_data["price"])
    
    # 支払い金額と還元予定ポイント
    col1, col2, col3 = st.columns([6, 1.5, 2])
    with col2:
        st.write('')
        st.write("**支払い金額**")
        st.write('')
        st.write("**還元予定ポイント**")
    with col3:
        st.subheader(f'**¥ {price - pt}**') # 支払い金額
        st.subheader(f'**{price*0.01}** pt') # 還元予定ポイント
    st.divider()

    # 配送先
    st.subheader("配送先")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("**姓（全角）**", placeholder="例）山田", max_chars=15)
        st.text_input("**姓カナ（全角）**", placeholder="例）ヤマダ", max_chars=15)
    with col2:
        st.text_input("**名（全角）**", placeholder="例）彩", max_chars=15)
        st.text_input("**名カナ（全角）**", placeholder="例）アヤ", max_chars=15)
    st.divider()
    st.text_input("**郵便番号（数字）**", placeholder="例）1234567")
    st.divider()
    st.selectbox("**都道府県**", [
        "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
        "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
        "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県",
        "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県",
        "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県",
        "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県",
        "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"])
    st.text_input("**番地**", placeholder="例）青山 1-1-1")
    st.text_input("**市区町村**", placeholder="例）横浜市緑区")
    st.text_input("**建物名（任意）**", placeholder="例）柳ビル 103")
    st.divider()
    st.text_input("**電話番号**", placeholder="09012345678")
    st.divider()

    # 置き配の指定
    col1, col2 = st.columns(2)
    with col1: st.subheader("置き配")
    with col2:
        st.selectbox(" ", ["玄関", "宅配ボックス", "メーターボックス", "物置", "車庫", "置き配を利用しない"])
    st.divider()

    # 購入確認
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        with st.form(key="confirmation"):
            col1, col2, col3, col4 = st.columns([2, 2, 1, 5])
            with col2: display_image(url=st.session_state.purchase_data["image"]) # 画像
            with col4: st.write(f'**{st.session_state.purchase_data["title"]}**') # 商品名
            col1, col2, col3, col4 = st.columns([2, 2, 1, 5])
            with col2:
                st.write("商品代金")
                st.write("ポイント")
            with col4:
                st.write(f'¥ {price}') # 価格
                st.write(f'ー {pt}') # ポイント使用
            st.divider()
            col1, col2, col3, col4 = st.columns([2, 2, 1, 5])
            with col2: st.write("**支払い金額**")
            with col4: st.subheader(f'**¥ {price-pt}**') # 支払い金額

            # 購入ボタン
            submit_btn = st.form_submit_button("**購入**", use_container_width=True)
            if submit_btn: st.success("**購入しました**\n\nご購入ありがとうございます！ 今後ともよろしくお願いします!")

except Exception as e:
    st.warning("**エラー**\n\n申し訳ございません。\n\nブラウザの「ページ更新」や「戻る・進む」を押すとページを表示できません。\n\n5秒後に自動で画面が切り替わります。")
    time.sleep(5)
    st.switch_page("pages/home.py")
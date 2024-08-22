import streamlit as st
from package import module
from PIL import Image

# トピックページ設定
st.set_page_config(layout="wide")                          # ワイドモード
st.image(Image.open("img/sub.png"), use_column_width=True) # サブビジュアル
module.header("トピック")    

# データベース
topic = [
    {"id":201,
     "title":"おいしいと評判！そうめんギフトのおとりよせなら島原！",
     "date":"2022/10/22",
     "img":"https://www.shimabara-soumen.com/_p/1517/images/pc/1a93a64f.jpg",
     "url":"https://www.shimabara-soumen.com/"
    },
    {"id":202,
     "title":"【在住者厳選】島原名物『かんざらし』オススメ店5選！",
     "date":"2023/09/20",
     "img":"https://dodon-shimabara.com/wp-content/uploads/2023/09/%E3%81%8B%E3%82%93%E3%81%96%E3%82%89%E3%81%97-%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1%E5%BA%97.jpg",
     "url":"https://dodon-shimabara.com/2023/09/20/kanzarashi/"
    },
    {"id":203,
     "title":"姫松屋：島原名物 元祖 具雑煮",
     "date":"2010/01/31",
     "img":"https://www.himematsuya.jp/img/guzouni-rogo2.jpg",
     "url":"https://www.himematsuya.jp/"
    },
    {"id":204,
     "title":"雲仙にある六兵衛が食べれるお店",
     "date":"2021/06/14",
     "img":"https://www.kirishima.co.jp/aji/2011/autumn/25/images/index/img_01.jpg",
     "url":"https://www.rokubecyaya.co.jp/shop"
    },
    {"id":205,
     "title":"年末年始にはゲン担ぎで”ガンバ”を食って”ふく”を招きに島原市へ!",
     "date":"2019/12/01",
     "img":"https://ljmarche.jp/my_image.php?m=Blog&id=470&f=blog_img_1&tmp_fname=&key=b1&size=l",
     "url":"https://ljmarche.jp/blog/article_470.html"
    },
    {"id":206,
     "title":"島原の「イギリス」、英国とは無縁",
     "date":"2014/10/01",
     "img":"https://article-image-ix.nikkei.com/https%3A%2F%2Fimgix-proxy.n8s.jp%2FDSXDZO7770501029092014EL1P02-17.jpg?ixlib=js-3.8.0&w=1445&h=802&auto=format%2Ccompress&fit=crop&bg=FFFFFF&s=8bd0e9c1c0c458958693605add546889",
     "url":"https://www.nikkei.com/article/DGXDZO77704980Z20C14A9EL1P02/"
    }
]

for i in range(len(topic)):
    col1, col2 = st.columns([2, 8])
    with col1:
        st.image(topic[i]['img'])
    with col2:
        st.markdown(f"[**{topic[i]['title']}**]({topic[i]['url']})")
        st.write(topic[i]['date'])
    st.divider()

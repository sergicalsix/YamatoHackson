import streamlit as st
from animation import *
import time

st.set_page_config(
   page_title="超スケジューリングくん",
   page_icon=":shark:",
   layout="wide",
 )

st.title("超スケジューリングくん")
st.write('<style>h1 {color: green;}</style>', unsafe_allow_html=True)

st.markdown('<style>' + open('icons.css').read() + '</style>', unsafe_allow_html=True)
st.markdown('<i class="material-icons">face</i>', unsafe_allow_html=True)

#st.image('<i class="material-icons"> ":face:" </i>', unsafe_allow_html=True)

#password = st.text_input('パスワードを入力してください')


#選択肢の作成
#area_option = st.sidebar.radio(
#     "配達場所を選択(今後入力に変える？)",
#    ('東京','大阪')
#)
area_option = "Tokyo"
user_option = st.sidebar.radio(
    "属性を選択してください",
    ('運転手','管理者')
)

if user_option == '運転手':
    name = st.sidebar.radio(
        "氏名",
        ('大久保','Chou','渋谷','渡辺','高橋')
    )

st.markdown(
"""
-----
"""
)

#area_option

st.sidebar.markdown("""-----""")

go = st.sidebar.checkbox('実行!!')
# ここは変える、
if go == True :

    #st.image('test.gif')

    if user_option == '運転手':
        #ガントチャートの描画
        fig = my_gantt_chart(name = name)
        st.plotly_chart(fig)
        #地図の描画

        st.write(f"{name}さんに配達をお願いしている場所です！本日はよろしくお願いいたします！")
        fig = my_task_view(name = name)
        st.pydeck_chart(fig)

        #st.write("配送アニメーション")

        #frame = st.slider('経過時間(分)')
        #fig = my_animation(frame = frame)
        #st.pydeck_chart(fig)
        #time.sleep(1)

    else:
        fig = my_CO2_chart()
        st.plotly_chart(fig)
        st.write(f"本日の{area_option}エリアの配達")
        fig = my_task_view(name = "all")
        st.pydeck_chart(fig)

        st.write("配送アニメーション")
        st.image('all.gif')


st.markdown(
"""
-----
"""
)

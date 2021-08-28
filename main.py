import streamlit as st
from animation import *


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
area_option = st.sidebar.radio(
     "配達場所を選択(今後入力に変える？)",
    ('東京','大阪')
)
user_option = st.sidebar.radio(
    "属性を選択(氏名に変える?)",
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


go = st.button('実行!!')
# ここは変える、
if go == True :
    #st.image('test.gif')

    if user_option == '運転手':
        #ガントチャートの描画
        fig = my_gantt_chart(name = name)
        st.plotly_chart(fig)
        #地図の描画
        fig = my_task_view(name = name)
        st.pydeck_chart(fig)

    else:
        fig = my_CO2_chart()
        st.plotly_chart(fig)
        fig = my_task_view(name = "hoge")
        st.pydeck_chart(fig)


st.markdown(
"""
-----
"""
)

import streamlit as st
from animation import *

st.title("超スケジューリングくん")


#password = st.text_input('パスワードを入力してください')


#選択肢の作成
area_option = st.radio(
     "配達場所を選択(今後入力に変える？)",
    ('東京','大阪')
)
user_option = st.radio(
    "属性を選択(氏名に変える?)",
    ('運転手','管理者')
)

if user_option == '運転手':
    name = st.radio(
        "氏名",
        ('okubo','shibuya','tyo','saito','takahashi')
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
        fig = my_task_view(name = name)
        st.pydeck_chart(fig)


st.markdown(
"""
-----
"""
)

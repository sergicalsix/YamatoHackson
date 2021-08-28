import streamlit as st

st.title("配送最適化アプリver1")

#選択肢の作成
area_option = st.radio(
     "配達場所を選択(今後入力に変える？)",
    ('東京','大阪')
)
user_option = st.radio(
    "属性を選択(氏名に変える?)",
    ('運転手','管理者')
)
st.markdown(
"""
-----
"""
)
go = st.button('実行!!')

# ここは変える、
if go == True :
    st.image('test.gif')

    if area_option == '東京':
        st.write("hoge")

    else:
        st.write('まだ！')


st.markdown(
"""
-----
"""
)

import streamlit as st
from animation import *
import time

st.set_page_config(
   page_title="超スケジューリングくん",
   page_icon=":cat:",
 )

st.title("超スケジューリングくん　(渋谷駅周辺)")
st.write('<style>h1 {color: green;}</style>', unsafe_allow_html=True)

#st.markdown('<style>' + open('icons.css').read() + '</style>', unsafe_allow_html=True)
#st.markdown('<i class="material-icons">face</i>', unsafe_allow_html=True)
st.image('img/icons/sch.png')
#st.image('<i class="material-icons"> ":face:" </i>', unsafe_allow_html=True)
#password = st.text_input('パスワードを入力してください')
#選択肢の作成
#area_option = st.sidebar.radio(
#     "配達場所を選択(今後入力に変える？)",
#    ('東京','大阪')
#)
area_option = "渋谷駅"

st.sidebar.image('img/icons/flag.png')
user_option = st.sidebar.radio(
    "属性を選択してください",
    ('セールスドライバー','センター長')
)

if user_option == 'セールスドライバー':
    name = st.sidebar.radio(
        "氏名",
        ('大久保','Chou','渋谷','渡辺','高橋')
    )

st.markdown("""-----""")

#area_option

st.sidebar.markdown("""-----""")

go = st.sidebar.checkbox('実行!!')

if go == True :
    if user_option == 'セールスドライバー':
        #ガントチャートの描画
        st.warning(f'本日の{name}さんの配達予定です！！')
        fig = my_gantt_chart(name = name)
        st.plotly_chart(fig)
        #地図の描画

        st.info(f"{name}さんに配達をお願いしている場所です！本日はよろしくお願いいたします！")
        fig = my_task_view(name = name)
        st.pydeck_chart(fig)


        st.success("配送場所")
        df = my_driver_place(name = name)

        index_list = []
        for i in range(len(df)):
            tmp = "Task" + str(i+1)
            index_list.append(tmp)
        df.index = index_list
        st.dataframe(df, width=500 , height = 100)
        st.image('img/icons/mapIcon.png')

        #frame = st.slider('経過時間(分)')
        #fig = my_animation(frame = frame)
        #st.pydeck_chart(fig)
        #time.sleep(1)

    else:

        st.info(f"本日の{area_option}周辺の配達")
        fig = my_task_view(name = "all")
        st.pydeck_chart(fig)

        st.success("配送アニメーション")
        st.image('all.gif')

    
        #df = pd.read_csv('data/guests_tokyo.csv')
        #df = df.drop(['ゲスト番号','希望時間帯'],axis = 1)
        #st.dataframe(df.head(20), width = 1000000)

        st.error("時間を指定した顧客の数を変更した時のシミュレーション結果")
        fig = my_CO2_chart()
        st.plotly_chart(fig)


st.markdown("""-----""")

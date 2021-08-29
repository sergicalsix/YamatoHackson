import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pydeck as pdk

from typing import List,Dict
import datetime

import streamlit as st #テスト用

#df = pd.read_csv('data/results.csv')
def my_gantt_chart(name:str = "大久保" , area_option = "Tokyo") -> object:

    if area_option == "Tokyo":
        move_seconds:list = [[9, 11, 5, 11], [9, 12, 8, 11, 6], [8, 5, 6, 8, 3, 9, 3], [6, 9, 5, 11, 8], [6, 3, 5, 6]]
    name_to_num:dict = {'大久保':0,'Chou':1,'渋谷':2,'渡辺':3,'高橋':4}
    move_second:list = move_seconds[ name_to_num[name] ]  #ex. [9, 11, 5, 11]
    #st.write(task)

    gantt_chart_list:List[Dict] = []
    start:object = datetime.datetime(2021,8,29,9,00)
    now_min:int = 0


    for i in range(len(move_second)):
        task_name:str = 'Task' + str(i+1)
        now_min += move_second[i]
        end = datetime.datetime(2021,8,29,9,now_min)

        #end = start + datetime.time_delta( seconds = task[i] )

        gantt_chart_list.append(dict( Task=task_name, Start= start, Finish= end, Kind='Task'))
        start = end

    #最後にあまり時間を休憩にする
    task_name:str = 'Rest'
    end = datetime.datetime(2021,8,29,10,00)
    gantt_chart_list.append(dict( Task=task_name, Start= start, Finish= end, Kind='Rest'))


    """demo_df = pd.DataFrame([
        dict(Task='Task1', Start= datetime.datetime(2021,8,29,7,00), Finish='2021-08-29 7:30', Kind='Task'),
        dict(Task='Task2', Start='2021-08-29 9:00', Finish='2021-08-29 11:25', Kind='Task'),
        #dict(Task='Rest', Start='2021-01-01 11:30', Finish='2021-01-01 12:00', Kind='Rest'),
    ])"""
    demo_df = pd.DataFrame(gantt_chart_list)

    colors = dict(#Cardio = 'rgb(46, 137, 205)',
                  Task = 'rgb(114, 44, 121)',
                  #Sleep = 'rgb(198, 47, 105)',
                  #Brain = 'rgb(58, 149, 136)',
                  Rest = 'rgb(107, 127, 135)'
                  )

    fig = px.timeline(demo_df, x_start="Start", x_end="Finish", y="Task", color="Kind")
    fig.update_yaxes(autorange="reversed")
    #fig.show()
    return fig

def my_task_view(name:str = "大久保", area_option = "Tokyo") -> object:
    """
    nameが指定された文字以外の場合は、全員表示

    out:pdk.Deck
    """
    if area_option == "Tokyo":
        df = pd.read_csv('data/guests_tokyo.csv')
        df_yamato = pd.read_csv('data/host_tokyo.csv')
        visited_places = {1: [0, 2, 5, 16, 0], 2: [0, 3, 6, 11, 17, 0], 3: [0, 4, 1, 7, 14, 15, 19, 0], 4: [0, 8, 13, 12, 18, 0], 5: [0, 10, 9, 20, 0]}
        x,y = 35.66062359622924,139.704968885932

    # 運転手が訪問する場所の適用
    name_to_num:dict = {'大久保':0,'Chou':1,'渋谷':2,'渡辺':3,'高橋':4}
    if name in name_to_num:
        key_ = name_to_num[name] + 1
        visited_place:list = visited_places[key_]
        #visited_places.remove(0)
        #visited_places.remove(0)

        df = df[df["ゲスト番号"].isin(visited_place)]


    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[経度, 緯度]',
            #get_fill_color="ward_color",
            get_fill_color=[180, 0, 200,150],
            get_radius=30,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df_yamato,
            get_position='[経度, 緯度]',
            #get_fill_color="ward_color",
            get_fill_color=[55, 200, 255,150],
            get_radius=50
        ),
       ]


    fig = pdk.Deck(
            map_style='mapbox://styles/mapbox/streets-v11',
            initial_view_state=pdk.ViewState(
                latitude= x,
                longitude= y,
                zoom=14,
                max_zoom = 16,
                min_zoom = 8,
                pitch=50,
            ),
            layers = layers
            )

    return fig


def my_CO2_chart() -> object:
    df = pd.DataFrame()

    df['time'] = [str(i+6) + ":00" for i in range(10)]
    df['a'] = [i*3 for i  in range(10)]
    df['b'] = [i*2 for i  in range(10)]
    x = df['time']
    y0 = df['a']
    y1 = df['b']
    #trace
    trace0 = go.Bar(x=x,y=y0,name="Past")
    trace1 = go.Bar(x=x,y=y1,name="Ours")
    traces = [trace0,trace1]
    #layout
    layout = go.Layout(title=(dict(text="CO2 排出量",x=0.5)),
                  xaxis=(dict(title="time")),
                  yaxis=(dict(title="cost")))
    #figure
    fig = go.Figure(data=traces,layout=layout)

    return fig


def my_animation(frame = 0) -> object:
    """
    アニメーションはこの関数で表示しようかな〜
    frameは親で処理する。

    """
    x,y = 35.66062359622924,139.704968885932
    df = pd.read_csv('data/guests_tokyo.csv')
    df_yamato = pd.read_csv('data/host_tokyo.csv')

    df_frame = my_make_frame(total_frame = 60,area_option = "Tokyo")
    df_frame = df_frame.iloc[frame,:].T

    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[経度, 緯度]',
            #get_fill_color="ward_color",
            get_fill_color=[180, 0, 200,150],
            get_radius=30,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df_yamato,
            get_position='[経度, 緯度]',
            #get_fill_color="ward_color",
            get_fill_color=[55, 200, 255,150],
            get_radius=50
        )
       ]


    fig = pdk.Deck(
            map_style='mapbox://styles/mapbox/streets-v11',
            initial_view_state=pdk.ViewState(
                latitude= x,
                longitude= y,
                zoom=14,
                max_zoom = 14,
                min_zoom = 8,
                pitch=50,
            ),
            layers = layers
            )

    return fig


def my_make_frame(total_frame = 60,area_option = "Tokyo") -> object:
    """
    アニメーション用のフレームを作る.
    60分で、移動時間の最小値が3だがプログラムの都合上
    1フレーム1分とする

    out: 5(トラック)×60のデータフレーム <- グラフを描画しやすいから
    """
    if area_option == "Tokyo":
        pos_df = pd.read_csv('data/guests_tokyo.csv')
        visited_places = {1: [0, 2, 5, 16, 0], 2: [0, 3, 6, 11, 17, 0], 3: [0, 4, 1, 7, 14, 15, 19, 0], 4: [0, 8, 13, 12, 18, 0], 5: [0, 10, 9, 20, 0]}
        move_seconds:list = [[9, 11, 5, 11], [9, 12, 8, 11, 6], [8, 5, 6, 8, 3, 9, 3], [6, 9, 5, 11, 8], [6, 3, 5, 6]]
        name_to_num:dict = {'大久保':0,'Chou':1,'渋谷':2,'渡辺':3,'高橋':4}
        x,y = 35.66062359622924,139.704968885932

    #ひとまず大久保さんのデータのみを作ることに注力


    name = "大久保"
    #if name in name_to_num:
    key_ = name_to_num[name]
    move_second:list = move_seconds[key_]
    visited_place:list = visited_places[key_ + 1]

    #print(move_second, visited_place)
    pos_x, pos_y = [x], [y]
    pre_x, pre_y = x,y
    for i , v in enumerate( visited_place[1:]):
        if v == 0:
            next_x, next_y = x,y
        else:
            place_ = pos_df[pos_df["ゲスト番号"] == v]
            next_x, next_y = place_["緯度"].values[0], place_["経度"].values[0]
        #print(v)
        #print(next_x)
        time:int = move_second[i]

        delta_x = ( next_x - pre_x ) / time
        delta_y = ( next_y - pre_y ) / time

        for _ in range(time):
            pre_x += delta_x
            pre_y += delta_y

            pos_x.append(pre_x)
            pos_y.append(pre_y)

    #休憩の追加
    for _ in range(61 - len(pos_x)):
        pos_x.append(pre_x)
        pos_y.append(pre_y)


    #    pre_x, pre_y = next_x , next_y
    df = pd.DataFrame()
    df["経度"] = pos_x
    df["緯度"] = pos_y

    return df

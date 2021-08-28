import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#df = pd.read_csv('data/results.csv')
def my_gantt_chart() -> object:
    colors = dict(#Cardio = 'rgb(46, 137, 205)',
                  Task = 'rgb(114, 44, 121)',
                  #Sleep = 'rgb(198, 47, 105)',
                  #Brain = 'rgb(58, 149, 136)',
                  Rest = 'rgb(107, 127, 135)'
                  )

    #fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule',
    #                      show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)

    demo_df = pd.DataFrame([
        dict(Task='Task1', Start='2021-01-01 7:00:00', Finish='2021-01-01 7:30:00', Kind='Task'),
        dict(Task='Task2', Start='2021-01-01 9:00:00', Finish='2021-01-01 11:25:00', Kind='Task'),
        dict(Task='Rest', Start='2021-01-01 11:30:00', Finish='2021-01-01 12:00:00', Kind='Rest'),
    ])

    fig = px.timeline(demo_df, x_start="Start", x_end="Finish", y="Task", color="Kind")
    fig.update_yaxes(autorange="reversed")
    #fig.show()
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

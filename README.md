## アプリ名
配送最適化アプリ ~超スケジューリングくん

## What is
ヤマト運輸ハッカソン(2021/8/28, 2021/8/29)優勝アプリケーションです!!

(配送シミュレーションを含む一部のバックエンドのコードはpushしていません。)

## URL

https://share.streamlit.io/sergicalsix/yamatohackson/main.py

## 概観
![](overview.pdf)


---
## 機能
- 配送シミュレーション結果(gif)
- ガントチャート
- 配送場所一覧(dataframe)
- 顧客の時間指定の人数を変化させた時のCO2排出量のシミュレーション結果
- 配送map(mapbox)

## 使用技術(フロント)
- streamlit(フレーム)
- plotly(ガントチャート、棒グラフの作成)
- pydeck(地図の描画)
- css(文字の色付けだけ)

## 使用技術(バックエンド)
- matplotlib, Pillow(配送アニメーションのgifの作成)
- gurobi(配送計画の計算)
- Google Map API

---
### 環境構築
```
$ python -m venv venv
$ source venv/bin/activate
(venv)$ pip install -r requirement.txt
```

### Run
```
$ streamlit run main.py
```

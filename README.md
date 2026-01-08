# ROS2_wear 気温から服装アドバイス
![test](https://github.com/ken116610/ROS2_wear/actions/workflows/test.yml/badge.svg)

## 何をするもの?
今日の気温を送ると服装のアドバイスを出力するROS2パッケージです。

##ノード
- `outfit_suggester`：`/temp_c` を購読して、`/outfit_advice` を配信します
- `temp_cli`：温度を手入力して `/temp_c` に配信します

## トピック


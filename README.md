# ROS2_wear 気温から服装アドバイス
![test](https://github.com/ken116610/ROS2_wear/actions/workflows/test.yml/badge.svg)

## 何をするもの?
今日の気温を送ると服装のアドバイスを出力するROS2パッケージです。

## ノード
- `outfit_suggester`：`/temp_c` を購読して、`/outfit_advice` を配信します
- `temp_cli`：温度を手入力して `/temp_c` に配信します

## トピック
- Subscribe：`/temp_c`(`std_msgs/msg/Float32`)
- Publish：`/outfit_advice`(`std_msgs/msg/String`)

## 使い方

### ビルド
任意のワークスペースでビルドして反映
```
$ colcon build --symlink-install
$ source install/setup.bash
```

### 実行方法
3つのターミナルを使用します。

#### ターミナル1（受け側）
```
$ ros2 run ROS2_wear outfit_suggester
```

#### ターミナル2（気温入力）
```
$ ros2 run ROS2_wear temp_cli
```

#### ターミナル3（出力確認）
```
$ ros2 topic echo /outfit_advice
```

### 実行例
例）気温を 4℃ と入力した場合（出力例）\
data: 4.0°C -> 厚手コート / 手袋 / マフラー

## 動作環境
Ubuntu 22.04 LTS\
Python3 系\
GitHub Actions\
ROS2 Humble

## ライセンス
・本コマンドは三条項BSDライセンスの下にて、使用および複製が許可されています>。\
・© 2025 Yuken Ro

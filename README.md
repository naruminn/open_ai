# OpenAI Gym サンプル

## 必要環境
* Docker
* Docker Compose

## Jupyter Notebookの起動

```
% cp .env.sample .env
% cat .env
WORKSPACE=hoge # 書き換えてください
```

```
% docker-compose build
% docker-compose run
```

http://localhost:8888

## サンプル

### simulation
CartPole のシミュレーションを表示します。

### q_leaning
Q学習とSARSA法のサンプルです。

docker build -t my-django-app .

docker run -d --name my-django-container -p 8000:8000 my-django-app

django-admin startproject django_rest_framework_test

django-admin startapp app

superuser aroma pass too

python manage.py makemigrations myproject

python manage.py migrate

docker exec -it django-back bash

docker exec -it react-front bash

npm list --depth=0

python manage.py runserver 0.0.0.0:8000

streamlit run Home.py --server.address 0.0.0.0 --server.port 8080


- compose

version: "3.8"//docker composerのバージョンの指定
services:
  front:
    build: ./　//buildするdockerfileの位置
    container_name: node　//作成するdockerコンテナの名前
    volumes:
      - ./front:/front　//docker内と共有するフォルダの指定
    working_dir: /front　//docker内に入った時の初期パスの指定
    ports:
      - 3000:3000　//コンテナにバインドするポートの指定（左:自分のPCポート、右:dookerコンテナのポート）
    tty: true　//コンテナが勝手に終了しないための設定
    stdin_open: true　//標準入出力とエラー出力をコンテナに結びつける設定
    environment:
      - CHOKIDAR_USEPOLLING=true //ホットリロードを行う設定

- dockerfile

FROM node:16.13.0-alpine3.12 //dockerHubから持ってくるImageの指定
ENV NODE_VERSION 14.18.1 //使用するnodeのバージョンの指定
WORKDIR /front  //docker内に入った時の初期パスの指定
COPY ./front /front　//ローカル側のファイルをdocker内にコピーする
EXPOSE 3000　//コンテナの使用ポート指定
ENV CI=true　//コンテナが勝手に終了してしまわないようにする設定

- git

git fetch
git rebase origin/main
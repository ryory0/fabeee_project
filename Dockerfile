# ベースイメージを指定
FROM python:3.9-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    gcc

# 作業ディレクトリを指定（コンテナ内）
WORKDIR /key_type

# Pythonのパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトファイルをコンテナにコピー
COPY . .

# ポートを指定（コンテナ内のポートを公開）
EXPOSE 8000

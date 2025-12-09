FROM python:3.13.6-alpine

# 時間設定
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
    && echo "Asia/Taipei" > /etc/timezone

# 安裝 uv
RUN pip install uv --no-cache-dir

# 安裝 ffmpeg, opus 依賴
RUN apk add --no-cache ffmpeg libsodium libsodium-dev opus opus-dev build-base

WORKDIR /app

COPY . .

RUN uv sync
FROM python:3.13.6-alpine

# 時間設定
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
    && echo "Asia/Taipei" > /etc/timezone

# 安裝 uv
RUN pip install uv --no-cache-dir

# 安裝其他依賴
RUN apk add --no-cache ffmpeg libsodium opus deno

WORKDIR /app

COPY pyproject.toml uv.lock .python-version ./

RUN uv sync --frozen --no-install-project

COPY . .

CMD ["uv", "run", "main.py"]
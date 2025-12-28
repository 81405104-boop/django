# 使用官方 Python 映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 安裝必要套件
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 複製 requirements.txt 並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案全部檔案
COPY . .

# 使用 Gunicorn 啟動 Django 伺服器
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]

from pathlib import Path

# -----------------------------
# 專案根目錄
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# 安全設定（⚠️ 正式上線請更換金鑰）
# -----------------------------
SECRET_KEY = 'dev-secret-key-change-me'
DEBUG = True

# -----------------------------
# 允許的主機來源
# -----------------------------
ALLOWED_HOSTS = [
    '192.168.1.145',          # 本機 NAS IP
    'localhost',
    '127.0.0.1',
    'django2.tw.cpolar.io',   # ✅ 你的外部公開網址
]

# -----------------------------
# CSRF 信任來源（HTTPS 必須寫 https://）
# -----------------------------
CSRF_TRUSTED_ORIGINS = [
    'http://192.168.1.145',
    'http://localhost',
    'http://127.0.0.1',
    'https://django2.tw.cpolar.io',  # ✅ 加入 cpolar HTTPS 網址
]

# -----------------------------
# 已安裝的 App
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自訂應用
    'products',
    'cart',
    'accounts',
]

# -----------------------------
# 中介層設定
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# URL 入口
# -----------------------------
ROOT_URLCONF = 'mysite.urls'

# -----------------------------
# 模板設定
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -----------------------------
# WSGI / ASGI
# -----------------------------
WSGI_APPLICATION = 'mysite.wsgi.application'
ASGI_APPLICATION = 'mysite.asgi.application'

# -----------------------------
# 資料庫設定（預設 SQLite）
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------
# 密碼驗證（上線建議開啟）
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# 語系 / 時區
# -----------------------------
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_TZ = True

# -----------------------------
# 靜態檔案（CSS / JS / 圖片）
# -----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# -----------------------------
# 媒體檔案（使用者上傳）
# -----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------------
# 主鍵型別
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------
# 登入 / 登出導向
# -----------------------------
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

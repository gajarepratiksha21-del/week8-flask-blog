class Config:

    SECRET_KEY = "my-secret-key-12345"

    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SECURE = False

    SESSION_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SAMESITE = "Lax"

    SESSION_COOKIE_NAME = "myblog_session"

    PERMANENT_SESSION_LIFETIME = 86400
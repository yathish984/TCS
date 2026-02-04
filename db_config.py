from sqlalchemy import create_engine # type: ignore

DB_USER = "root"
DB_PASSWORD = "yathi@984"
DB_HOST = "localhost"
DB_NAME = "ml_financial"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

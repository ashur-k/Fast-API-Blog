from sqlalchemy import create_engine

from config import settings

DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ Database connection successful")
except Exception as e:
    import ipdb; ipdb.set_trace()  # noqa: E702, I001
    print("❌ Connection failed:", e)


# uv run python database_test.py
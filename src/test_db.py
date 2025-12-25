from db import get_connection
from sqlalchemy import text


engine = get_connection()

with engine.connect() as conn:
    result = conn.execute(text("SELECT DATABASE();"))
    print(result.fetchone())

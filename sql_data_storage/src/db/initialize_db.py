from sqlalchemy import create_engine
from models import Base

# Example: SQLite database (change the URL for other DBs)
engine = create_engine('sqlite:///finmark_database.db')

# Create all tables defined in your models
Base.metadata.create_all(engine)

print("Database tables created successfully.")
from app.database import engine
from app.models import Base

def init():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")

if __name__ == "__main__":
    init()
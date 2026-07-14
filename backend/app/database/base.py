from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Import models so SQLAlchemy knows about them
from app.users import model

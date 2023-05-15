from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


class Venue(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None)
    address: Optional[str] = Field(default=None)
    city: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    lat: Optional[float] = Field(default=None)
    lng: Optional[float] = Field(default=None)


def create_database():
    engine = create_engine("sqlite:///venues.db")
    SQLModel.metadata.create_all(engine)

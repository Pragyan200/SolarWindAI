from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime
from app.database.database import Base

class Project(Base):
    __tablename__="projects"

    id=Column(Integer,primary_key=True,index=True)
    project_name=Column(String,nullable=False)
    description=Column(String)
    location=Column(String)
    state=Column(String)
    latitude=Column(Float)
    longitude=Column(Float)
    created_at=Column(DateTime,
    default=datetime.utcnow)
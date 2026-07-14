from pydantic import BaseModel

class ProjectCreate(BaseModel):
    project_name:str
    location:str

class ProjectResponse(ProjectCreate):
    id:int

    class Config:
        from_attributes=True
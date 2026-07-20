from pydantic import BaseModel,Field

class ProjectCreate(BaseModel):
    project_name:str=Field(...,min_length=1)
    location:str

class ProjectResponse(ProjectCreate):
    id:int

    class Config:
        from_attributes=True
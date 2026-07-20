from fastapi import APIRouter
from app.schemas.project import ProjectCreate

from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.project import Project

router=APIRouter()

@router.get("/projects")
def get_projects(db:Session=
Depends(get_db)):
    projects=db.query(Project).all()
    return projects


@router.post("/project")
def create_project(project:ProjectCreate,
db:Session=Depends(get_db)):
    new_project=Project(
        project_name=project.project_name,
        location=project.location
    )
    
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project
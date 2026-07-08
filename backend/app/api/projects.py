from fastapi import APIRouter

router=APIRouter()

@router.get("/projects")
def get_projects():
    return[
        {
            "id":1,
            "project_name":"Odisha Solar Farm",
            "status":"Created"
        }
    ]
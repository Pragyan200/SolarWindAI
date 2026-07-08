from fastapi import APIRouter

router=APIRouter()

@router.get("/")
def home():
    return{
        "message:" "Solar & Wind Deployment Intelligence Platform"
    }
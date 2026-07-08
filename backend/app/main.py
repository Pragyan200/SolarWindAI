from fastapi import FastAPI
from app.api.home import router as home_router
from app.api.projects import router as projects_router
from app.api.sites import router as sites_router

app=FastAPI()

app.include_router(home_router)
app.include_router(projects_router)
app.include_router(sites_router)

@app.get("/health")
def health():
    return{
        "status":"Running"
    }
@app.get("/about")
def about():
    return{
        "project":"Solar & Wind Deployment Intelligence Platforms"
    }
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{
        "message":"Solar & Wind Deployment Intelligence Platform"
    }
@app.get("/health")
def health():
    return{
        "status":"Running"
    }
@app.get("/about")
def about():
    return{
        "project":"Solar & Wind Deployment Intelligence Platform"
    }
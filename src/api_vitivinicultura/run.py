import uvicorn

def dev():
    uvicorn.run("api_vitivinicultura.main:app", reload=True, app_dir="src")
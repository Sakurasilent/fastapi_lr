from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello World"}

#终端启动命令 uvicorn fastapi_v1:app --reload
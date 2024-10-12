from fastapi import FastAPI
from app.controller import application_controller, base_controller

app = FastAPI()

app.include_router(base_controller.router)
app.include_router(application_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)

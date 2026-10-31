from fastapi import FastAPI
from routes import base_router ,upload_router


app = FastAPI()
app.include_router(base_router)
app.include_router(upload_router)
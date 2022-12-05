from fastapi import FastAPI

from api.v1.routers import router as v1_routers
from api.v2.routers import router as v2_routers

app = FastAPI()
app.include_router(v1_routers)
app.include_router(v2_routers)
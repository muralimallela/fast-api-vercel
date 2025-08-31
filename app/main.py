from fastapi import FastAPI
from app.db import session, base
from app.api.v1.endpoints import users, items

# Create tables
base.Base.metadata.create_all(bind=session.engine)

app = FastAPI()

# Register routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])


@app.get("/")
def root():
    return {"msg": "FastAPI + JWT + SQLite running 🚀"}

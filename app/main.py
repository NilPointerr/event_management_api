from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import events, attendees
from app.core import database

def create_tables():
    database.Base.metadata.create_all(bind=database.engine)

def create_application() -> FastAPI:
    app = FastAPI(title="Event Management API")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    create_tables()

    app.include_router(events.router, prefix="/api/v1")
    app.include_router(attendees.router, prefix="/api/v1")

    return app

app = create_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
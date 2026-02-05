import logging
from fastapi import FastAPI
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.core.middleware import RequestIDMiddleware
from app.api.v1 import auth_route as auth


settings = get_settings()
setup_logging()

logger = logging.getLogger(__name__)
logger.info("Application started")
logger.warning("Something looks odd")
logger.error("Something failed")
logger.debug("Debugging information")
logger.critical("Critical issue occurred")
logger.info(f"Environment: {settings.ENV}, Debug: {settings.DEBUG}, Name: {__name__}")

app = FastAPI(
        title="Resume Maker API",
        debug=settings.DEBUG
    )

app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "environment": settings.ENV, "debug": settings.DEBUG}

app.middleware("http")(RequestIDMiddleware) # Registering the middleware - har request per call hoga - ye global middleware h


# app.include_router(user.router)
# app.include_router(resume.router)

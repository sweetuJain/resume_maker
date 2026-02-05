import uuid

import logging
from fastapi import Request
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


async def RequestIDMiddleware(req: Request, call_next):
    req_id = str(uuid.uuid4())
    req.state.req_id = req_id
    logger.info(f"Request ID {req_id} - Start processing request: {req.method} {req.url}")
    
    response = await call_next(req)
    response.headers["X-Request-ID"] = req_id
    
    return response


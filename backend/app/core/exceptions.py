from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timezone

class ApiException(HTTPException):
    def __init__(self, status_code: int, detail: str,  error_code: str):
        super().__init__(
            status_code=status_code,
            detail=detail,
            headers={"X-Error-Code": error_code}
        )

async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "error_code": exc.headers["X-Error-Code"],
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )

handlers = {
    ApiException: api_exception_handler
}
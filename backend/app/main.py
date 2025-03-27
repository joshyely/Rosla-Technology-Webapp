from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .api import api_routes


app = FastAPI(
    name=settings.PROJECT_NAME
)
app.include_router(api_routes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def ping_api():
    """Test function for checking if the the API can be remotely called.

    On success, endpoint sends response 200 OK and the project name.
    """
    return JSONResponse(
        status_code=status.HTTP_200_OK, 
        content={
            'name': settings.PROJECT_NAME,
            'version': app.version,
        }
    )
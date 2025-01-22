from fastapi import APIRouter
from fastapi.responses import JSONResponse

misc_routes = APIRouter()


@misc_routes.get('/api/')
def api():
	return JSONResponse({ "message": "I am the root of the backend ♨️"}, status_code=200)

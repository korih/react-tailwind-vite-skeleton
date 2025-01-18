from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.sqlite_helpers import get_all_rows, add_row, remove_row, update_row

leaderboard_routes = APIRouter()


@leaderboard_routes.get('/api/get-scores')
def api_get_score():
	try:
		return JSONResponse({ "message": get_all_rows() }, status_code=200)
	except Exception as e:
		print("Error in /api/get-scores")
		print(e)
		return JSONResponse({ "error": "Error getting all rows" }, status_code=500)


class AddScoreBody(BaseModel):
	name: str
	score: int

@leaderboard_routes.post('/api/add-score')
def api_add_score(body:AddScoreBody):
	try:
		add_row(body.name, body.score)
		return JSONResponse({ "message": "Added score"}, status_code=200)
	except Exception as e:
		print("Error in /api/add-score")
		print(e)
		return JSONResponse({ "error": "Error adding score"}, status_code=500)

class RemoveScoreBody(BaseModel):
	id: int
@leaderboard_routes.delete('/api/remove-score')
def api_remove_score(body: RemoveScoreBody):
	try:
		remove_row(body.id)
		return JSONResponse({ "message": "Removed score"}, status_code=200)
	except Exception as e:
		print("Error in /api/remove-score")
		print(e)
		return JSONResponse({ "error": "Error removing score" }, status_code=500)

class ChangeScoreBody(BaseModel):
	id: int
	new_score: int
@leaderboard_routes.patch('/api/change-score')
def api_change_score(body: ChangeScoreBody):
	try:
		update_row(body.id, body.new_score)
		return JSONResponse({ "message": "Updated score"}, status_code=200)
	except Exception as e:
		print("Error in /api/change-score")
		print(e)
		return JSONResponse({ "error": "Error changing score"}, status_code=400)

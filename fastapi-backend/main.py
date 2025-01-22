import os
# Set working directory to this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.misc_routes import misc_routes
from routes.leaderboard_routes import leaderboard_routes
from utils.sqlite_helpers import init_db

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(misc_routes)
app.include_router(leaderboard_routes)

if __name__ == "__main__":
	init_db()
	uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)

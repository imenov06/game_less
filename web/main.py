from fastapi import FastAPI

from data import insert_users, insert_games, insert_courses_and_topics, delete_all_data
from users.router import router as users_router
from courses.router import router as courses_router
from games.router import router as game_router

app = FastAPI()

app.include_router(users_router)
app.include_router(courses_router)
app.include_router(game_router)


@app.post("/insert_data")
async def insert_base_data():
    await insert_users()
    await insert_games()
    await insert_courses_and_topics()


@app.post("/delete_data")
async def delete_base_data():
    await delete_all_data()

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root():
    return {"Главная страница"}

@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]) -> dict:
    return {"Вы вошли как пользователь №": user_id}

@app.get("/user/{username}/{age}")
async def user_name(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="UrbanUser'")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter Age", example=24)]) -> dict:
    return {"Информация о пользователе": f"Имя: {username}, Возраст: {age}"}
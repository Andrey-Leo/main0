from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Главная страница"}

@app.get("/user/admin")
async def admin():
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"Вы вошли как пользователь №": user_id}

@app.get("/user/{username}/{age}")
async def user_name(username: str, age: int) -> dict:
    return {"Информация о пользователе": f"Имя: {username}, Возраст: {age}"}





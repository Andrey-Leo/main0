from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import *
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
def all_user(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get('/user_id')
def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int ):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user

@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id))
    return tasks

@router.post('/create')
def create_user(db: Annotated[Session, Depends(get_db)], create_u: CreateUser):
    db.execute(insert(User).values(
        username=create_u.username,
        firstname=create_u.firstname,
        lastname=create_u.lastname,
        age=create_u.age,
        slug=slugify(create_u.username))
    )
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
    }


@router.put('/update')
def update_user(db: Annotated[Session, Depends(get_db)], update_u: UpdateUser, user_id: int):
    user_db = db.scalars(select(User).where(User.id == user_id)).first()
    if user_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_u.firstname,
        lastname=update_u.lastname,
        age=update_u.age)
    )
    db.commit()
    return {
        'status_code': status.HTTP_202_ACCEPTED,
        'transaction': 'User update is successful!'
    }


@router.delete('/delete')
def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_delete = db.scalars(select(User).where(User.id == user_id)).first()
    if user_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(delete(User).where(User.id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_202_ACCEPTED,
        'transaction': 'User delete is successful!'
    }





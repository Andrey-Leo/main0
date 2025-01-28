from fastapi import APIRouter


router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
def all_user():
    pass

@router.get('/user_id')
def user_by_id():
    pass

@router.post('/create')
def create_user():
    pass

@router.put('/update')
def update_user():
    pass

@router.delete('/delete')
def delete_user():
    pass

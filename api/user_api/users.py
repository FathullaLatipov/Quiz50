from fastapi import APIRouter

from database.usersevice import get_all_users_db, register_user_db, user_answer_db, result_db

user_router = APIRouter(prefix='/user', tags=['API for users'])


# Получить всех пользователей
@user_router.get('/all-users')
async def all_users():
    return get_all_users_db()

@user_router.get('/result')
async def all_users(user_id: int):
    return result_db(user_id)


@user_router.post('/register')
async def register(name: str, phone_number: int, level: str):
    reg = register_user_db(name, phone_number, level)
    return reg


@user_router.post('/answer-done')
async def get_leaders(user_id: int, id: int, level: str, correct_answer: str):
    leaders = user_answer_db(user_id, id, level, correct_answer)
    return f'Ответ {leaders}'

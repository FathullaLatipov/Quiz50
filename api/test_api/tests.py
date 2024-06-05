from fastapi import APIRouter
from database.testservice import get_question_db, add_questions_db, get_10_leaders_db

from database import get_db

test_router = APIRouter(prefix='/test', tags=['API for tests'])


@test_router.get('/all_questions')
async def all_questions():
    result = get_question_db()
    return result


@test_router.get('/10_leaders')
async def get_10_leaders():
    return f'Топ 10 Лидеров {get_10_leaders_db()}'


@test_router.post('/add_question')
async def add_question(main_question: str, v1: str, v2: str, v3: str, v4: str, correct_answer: str):
    add = add_questions_db(main_question, v1, v2, v3, v4, correct_answer)
    return add
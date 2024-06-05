from .models import Result, Questions
from database import get_db


# Топ 10 лидеров
def get_10_leaders_db():
    db = next(get_db())
    leaders = db.query(Result.user_id).order_by(Result.correct_answers.desc())
    return leaders[:10]


# получить только 20 тестов

def get_question_db():
    db = next(get_db())

    questions = db.query(Questions).all()

    return questions[:20]


# Мы сами добавляем вопросы и варианты
def add_questions_db(main_question, v1, v2, v3, v4, correct_answer):
    db = next(get_db())
    new_question = Questions(main_question=main_question, v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
    db.add(new_question)
    db.commit()
    return 'Вопрос успешно добавлен!'

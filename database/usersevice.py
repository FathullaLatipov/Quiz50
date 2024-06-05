from database.models import User, UserAnswers, Questions, Result
from datetime import datetime

from database import get_db


def get_all_users_db():
    db = next(get_db())

    users = db.query(User).all()

    return users


# Регистрация пользователя
def register_user_db(name, phone_number, level):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return f'Уже есть такой номер телефона и вот его ID {checker.id}'
    else:
        new_user = User(name=name, phone_number=phone_number, level=level, datetime=datetime.now())
        db.add(new_user)
        db.commit()
        return f'Успешно. Вот ID нового пользователя {new_user.id}'


# Ответы пользователя
def user_answer_db(user_id, id, level, correct_answer):
    db = next(get_db())
    exact_question = db.query(Questions).filter_by(id=id).first()
    print(exact_question)
    if exact_question:
        if exact_question.correct_answer == correct_answer:
            correctness = True
        else:
            correctness = False
        # Создание объекта в БД
        new_answer = UserAnswers(user_id=user_id, q_id=id, level=level, correctness=correctness)
        print(f'this is new answer {new_answer}')
        db.add(new_answer)
        db.commit()
        if correctness:
            user_result = db.query(Result).filter_by(user_id=user_id).first()
            print(f'this is user {user_result}')
            if user_result:
                user_result.correct_answers += correct_answer
                db.commit()
                return 'Плюс один балл'
        else:
            print('не сработало')
            return False
    else:
        return 'Вопрос не найден :('


def result_db(user_id):
    db = next(get_db())
    user = db.query(Result).filter_by(user_id=user_id).first()
    return user

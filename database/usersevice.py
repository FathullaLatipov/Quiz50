from database.models import User, UserAnswers, Questions, Result
from datetime import datetime

from database import get_db


# Получения всех пользователей
def get_all_users_db():
    # Соединения с нашим БД
    db = next(get_db())

    users = db.query(User).all()  # Ivan,Donik......

    return users

from typing import Optional
from belong import db
from belong.models import Users
from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    """
    Users 테이블 관련 CRUD 담당.
    """

    def get_by_id(self, user_id: int) -> Optional[Users]:
        return Users.query.get(user_id)

    def get_by_username(self, username: str) -> Optional[Users]:
        return Users.query.filter_by(username=username).first()

    def get_by_email(self, email: str) -> Optional[Users]:
        return Users.query.filter_by(email=email).first()

    def save(self, user: Users) -> Users:
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user: Users) -> None:
        db.session.delete(user)
        db.session.commit()

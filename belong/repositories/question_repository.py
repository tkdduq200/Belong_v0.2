from typing import Optional, List
from belong import db
from belong.models import Question
from .base_repository import BaseRepository


class QuestionRepository(BaseRepository):
    """
    Question 도메인의 DB 접근을 전담하는 Repository.
    """

    def get_by_id(self, question_id: int) -> Optional[Question]:
        return Question.query.get(question_id)

    def save(self, question: Question) -> Question:
        db.session.add(question)
        db.session.commit()
        return question

    def delete(self, question: Question) -> None:
        db.session.delete(question)
        db.session.commit()

    def list_all(self) -> List[Question]:
        return Question.query.order_by(Question.create_date.desc()).all()

    def get_paginated(self, page: int, per_page: int = 10):
        """
        페이지네이션 지원 목록 조회.
        Flask-SQLAlchemy의 paginate를 그대로 래핑.
        """
        query = Question.query.order_by(Question.create_date.desc())
        return query.paginate(page=page, per_page=per_page)

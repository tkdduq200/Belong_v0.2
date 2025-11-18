from typing import Optional
from datetime import datetime

from belong.models import Question
from belong.repositories.question_repository import QuestionRepository


class QuestionService:
    """
    질문(Question) 도메인 비즈니스 로직 담당.
    """

    def __init__(self, question_repository: QuestionRepository):
        self._questions = question_repository

    def get_question(self, question_id: int) -> Optional[Question]:
        return self._questions.get_by_id(question_id)

    def get_question_list(self, page: int, per_page: int = 10):
        """
        페이징된 질문 목록 반환.
        Flask-SQLAlchemy의 Pagination 객체 그대로 반환.
        """
        return self._questions.get_paginated(page=page, per_page=per_page)

    def create_question(self, subject: str, content: str) -> Question:
        question = Question(
            subject=subject,
            content=content,
            create_date=datetime.now(),
        )
        return self._questions.save(question)

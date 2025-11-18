from typing import Optional
from belong import db
from belong.models import Answer
from .base_repository import BaseRepository


class AnswerRepository(BaseRepository):
    """
    Answer 도메인의 DB 접근을 전담.
    """

    def get_by_id(self, answer_id: int) -> Optional[Answer]:
        return Answer.query.get(answer_id)

    def save(self, answer: Answer) -> Answer:
        db.session.add(answer)
        db.session.commit()
        return answer

    def delete(self, answer: Answer) -> None:
        db.session.delete(answer)
        db.session.commit()

from typing import Optional
from datetime import datetime

from belong.models import Answer
from belong.repositories.answer_repository import AnswerRepository
from belong.repositories.question_repository import QuestionRepository


class AnswerService:
    """
    답변(Answer) 도메인 비즈니스 로직 담당.
    """

    def __init__(
        self,
        answer_repository: AnswerRepository,
        question_repository: QuestionRepository,
    ):
        self._answers = answer_repository
        self._questions = question_repository

    def create_answer(self, question_id: int, content: str) -> Optional[Answer]:
        """
        질문 ID 기준으로 답변 생성.
        질문을 찾을 수 없으면 None 반환.
        """
        question = self._questions.get_by_id(question_id)
        if question is None:
            return None

        answer = Answer(
            content=content,
            create_date=datetime.now(),
        )

        # 관계 설정: question.answer_set.append(answer)
        question.answer_set.append(answer)

        # answer 저장 (question도 같이 커밋됨)
        return self._answers.save(answer)

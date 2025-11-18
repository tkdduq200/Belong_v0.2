from typing import Optional, Tuple

from werkzeug.security import generate_password_hash, check_password_hash

from belong.models import Users
from belong.repositories.user_repository import UserRepository


class UserService:
    """
    회원(User) 관련 비즈니스 로직 담당.
    - 회원가입
    - 로그인 검증
    """

    def __init__(self, user_repository: UserRepository):
        self._users = user_repository

    def register_user(
        self,
        username: str,
        email: str,
        raw_password: str,
    ) -> Tuple[Optional[Users], Optional[str]]:
        """
        회원가입 처리.
        (user, error_message) 튜플 반환.
        error_message가 None이면 성공.
        """
        # 중복 체크
        if self._users.get_by_username(username) is not None:
            return None, "이미 존재하는 사용자입니다."

        if self._users.get_by_email(email) is not None:
            return None, "이미 사용 중인 이메일입니다."

        user = Users(
            username=username,
            password=generate_password_hash(raw_password),
            email=email,
        )
        user = self._users.save(user)
        return user, None

    def authenticate(
        self,
        username: str,
        raw_password: str,
    ) -> Tuple[Optional[Users], Optional[str]]:
        """
        로그인 인증.
        (user, error_message) 튜플 반환.
        """
        user = self._users.get_by_username(username)
        if user is None:
            return None, "존재하지 않는 사용자입니다."

        if not check_password_hash(user.password, raw_password):
            return None, "비밀번호가 올바르지 않습니다."

        return user, None

    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        return self._users.get_by_id(user_id)

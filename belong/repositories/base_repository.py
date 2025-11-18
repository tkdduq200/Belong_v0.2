from abc import ABC, abstractmethod
from typing import Any, Optional, List


class BaseRepository(ABC):
    """
    모든 Repository가 따라야 하는 추상 인터페이스.
    CRUD 기본 기능을 정의하여 일관성 유지.
    """

    @abstractmethod
    def get_by_id(self, item_id: int) -> Optional[Any]:
        pass

    @abstractmethod
    def save(self, obj: Any) -> Any:
        pass

    @abstractmethod
    def delete(self, obj: Any) -> None:
        pass

    def list_all(self) -> List[Any]:
        """
        선택 구현. 리스트 조회가 필요 없는 Repository는 override 안 해도 됨.
        """
        raise NotImplementedError("list_all() is not implemented.")

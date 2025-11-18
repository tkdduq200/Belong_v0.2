from abc import ABC, abstractmethod


class PredictorStrategy(ABC):
    """
    예측 전략 인터페이스(추상 클래스).
    모든 예측 전략은 predict() 메서드를 구현해야 한다.
    """

    @abstractmethod
    def predict(self, gu: str, year: int) -> float:
        """
        단일 (구, 연도)에 대한 예측값만 float으로 반환.
        """
        pass

    def predict_with_detail(self, gu: str, year: int):
        """
        상세 정보 반환은 선택 기능이므로 기본 None.
        필요하면 하위 클래스에서 재정의.
        """
        return None

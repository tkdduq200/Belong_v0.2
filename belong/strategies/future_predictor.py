from .predictor_strategy import PredictorStrategy


class FuturePredictor(PredictorStrategy):
    """
    향후 새로운 예측 모델(Prophet, LSTM, ARIMA 등)을
    플러그인처럼 끼울 수 있도록 만들어둔 전략 뼈대.
    """

    def predict(self, gu: str, year: int) -> float:
        raise NotImplementedError(
            "FuturePredictor는 아직 구현되지 않았습니다. "
            "새로운 예측 알고리즘을 여기에 추가하세요."
        )

from typing import Optional, List
from belong import db
from belong.models import LonelyPrediction
from .base_repository import BaseRepository


class LonelyPredictionRepository(BaseRepository):
    """
    ML 예측 결과 저장용 Repository.
    """

    def get_by_id(self, record_id: int) -> Optional[LonelyPrediction]:
        return LonelyPrediction.query.get(record_id)

    def get_by_region_year(self, gu: str, year: int) -> Optional[LonelyPrediction]:
        return LonelyPrediction.query.filter_by(
            gu=gu,
            year=year
        ).first()

    def list_by_region(self, gu: str) -> List[LonelyPrediction]:
        return LonelyPrediction.query.filter_by(gu=gu).order_by(LonelyPrediction.year).all()

    def save(self, record: LonelyPrediction) -> LonelyPrediction:
        db.session.add(record)
        db.session.commit()
        return record

    def delete(self, record: LonelyPrediction) -> None:
        db.session.delete(record)
        db.session.commit()

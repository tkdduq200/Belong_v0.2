from datetime import datetime
from belong.extensions import db


class LonelyPrediction(db.Model):
    """
    고독사 예측 결과 엔티티.
    ML 서비스에서 예측한 결과 저장.
    """
    __tablename__ = "lonely_prediction"

    id = db.Column(
        db.Integer,
        db.Sequence("lonely_prediction_seq", start=1, increment=1),
        primary_key=True,
    )
    gu = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    predicted_value = db.Column(db.Float, nullable=False)
    actual_value = db.Column(db.Float, nullable=True)

    created_at = db.Column(db.DateTime(), default=datetime.now)

    __table_args__ = (
        db.UniqueConstraint("gu", "year", name="uq_lonely_prediction_gu_year"),
    )

from belong.extensions import db


class User(db.Model):
    """사용자(회원) 도메인 엔티티."""
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        db.Sequence("users_seq", start=1, increment=1),
        primary_key=True,
    )
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

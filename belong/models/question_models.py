from datetime import datetime
from belong.extensions import db


class Question(db.Model):
    """질문(게시글) 도메인 엔티티."""
    __tablename__ = "question"

    id = db.Column(
        db.Integer,
        db.Sequence("question_seq", start=1, increment=1),
        primary_key=True,
    )
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), default=datetime.now, nullable=False)


class Answer(db.Model):
    """답변 도메인 엔티티."""
    __tablename__ = "answer"

    id = db.Column(
        db.Integer,
        db.Sequence("answer_seq", start=1, increment=1),
        primary_key=True,
    )
    question_id = db.Column(
        db.Integer,
        db.ForeignKey("question.id", ondelete="CASCADE"),
        nullable=False,
    )
    question = db.relationship(
        "Question",
        backref=db.backref("answer_set", lazy="dynamic"),
    )
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), default=datetime.now, nullable=False)

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend.core.database import Base



class Answer(Base):

    __tablename__="answer"


    id=Column(
        Integer,
        primary_key=True,
        index=True
    )


    content=Column(
        Text,
        nullable=False
    )


    question_id=Column(
        Integer,
        ForeignKey(
            "question.id"
        )
    )


    question=relationship(
        "Question",
        back_populates="answers"
    )
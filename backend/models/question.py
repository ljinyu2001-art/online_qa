from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from backend.core.database import Base



class Question(Base):

    __tablename__="question"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    title = Column(
        String(200),
        nullable=False
    )


    description = Column(
        Text
    )


    answer_count = Column(
        Integer,
        default=0
    )


    answers = relationship(
        "Answer",
        back_populates="question",
        cascade="all,delete-orphan"
    )
from fastapi import APIRouter,Depends,HTTPException

from sqlalchemy.orm import Session


from backend.core.database import get_db

from backend.schemas.answer import AnswerCreate

from backend.services.qa_service import add_answer



router=APIRouter(
    prefix="/answers",
    tags=["回复"]
)



@router.post("/{question_id}")

def create_answer(

    question_id:int,

    data:AnswerCreate,

    db:Session=Depends(get_db)

):


    if not data.content:

        raise HTTPException(
            400,
            "回复内容不能为空"
        )


    return add_answer(
        db,
        question_id,
        data.content
    )
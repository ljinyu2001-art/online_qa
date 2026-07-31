from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from backend.core.database import get_db

from backend.schemas.question import (
    QuestionCreate,
    QuestionUpdate,
    QuestionOut,
    QuestionDetail
)

from backend.services.qa_service import *



router=APIRouter(
    prefix="/questions",
    tags=["问答"]
)



# 查询全部

@router.get("")
def list_question(
    db:Session=Depends(get_db)
):

    return get_questions(db)





# 提问

@router.post("")
def add_question(

    data:QuestionCreate,

    db:Session=Depends(get_db)

):

    return create_question(
        db,
        data
    )





# 删除

@router.delete("/{id}")

def delete(

    id:int,

    db:Session=Depends(get_db)

):

    delete_question(
        db,
        id
    )


    return {
        "msg":"删除成功"
    }





# 修改

@router.put("/{id}")

def update(

    id:int,

    data:QuestionUpdate,

    db:Session=Depends(get_db)

):

    return update_question(
        db,
        id,
        data
    )





# 详情

@router.get("/{id}", response_model=QuestionDetail)
def detail(
    id:int,
    db:Session=Depends(get_db)
):

    return get_detail(
        db,
        id
    )
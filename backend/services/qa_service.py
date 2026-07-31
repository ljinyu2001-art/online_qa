from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from backend.models.question import Question
from backend.models.answer import Answer
from backend.core.redis import redis_client

import json



# 查询所有问题

def get_questions(db:Session):


    cache = redis_client.get(
        "question:list"
    )


    if cache:

        return json.loads(cache)



    data = db.query(
        Question
    ).all()



    result=[]


    for q in data:

        result.append({

            "id":q.id,

            "title":q.title,

            "description":q.description,

            "answer_count":q.answer_count

        })



    redis_client.set(
        "question:list",
        json.dumps(result,ensure_ascii=False),
        ex=300
    )


    return result





# 添加问题

def create_question(db,data):


    q=Question(

        title=data.title,

        description=data.description

    )


    db.add(q)

    db.commit()

    db.refresh(q)


    redis_client.delete(
        "question:list"
    )


    return q





# 删除问题

def delete_question(db,id):


    q=db.query(
        Question
    ).filter(
        Question.id==id
    ).first()



    if q:

        db.delete(q)

        db.commit()



    redis_client.delete(
        "question:list"
    )


    return q





# 修改问题

def update_question(db,id,data):


    q=db.query(
        Question
    ).filter(
        Question.id==id
    ).first()



    if q:


        q.title=data.title

        q.description=data.description


        db.commit()

        db.refresh(q)



    redis_client.delete(
        "question:list"
    )


    return q





# 查询详情




def get_detail(db,id):

    question = db.query(
        Question
    ).options(
        joinedload(Question.answers)
    ).filter(
        Question.id==id
    ).first()


    return question




# 添加回答

def add_answer(db,id,content):

    answer=Answer(
        question_id=id,
        content=content
    )

    db.add(answer)


    q=db.query(
        Question
    ).filter(
        Question.id==id
    ).first()


    if q:
        q.answer_count += 1


    db.commit()
    db.refresh(answer)


    # 清除问题列表缓存
    redis_client.delete(
        "question:list"
    )


    return answer
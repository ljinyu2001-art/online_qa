from pydantic import BaseModel

from backend.schemas.answer import AnswerOut



class QuestionCreate(BaseModel):

    title:str

    description:str|None=None



class QuestionUpdate(BaseModel):

    title:str

    description:str|None=None




class QuestionOut(BaseModel):

    id:int

    title:str

    description:str|None

    answer_count:int


    class Config:

        from_attributes=True





class QuestionDetail(BaseModel):

    id:int

    title:str

    description:str|None


    answers:list[AnswerOut]


    class Config:

        from_attributes=True
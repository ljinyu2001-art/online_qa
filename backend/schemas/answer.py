from pydantic import BaseModel



class AnswerCreate(BaseModel):

    content:str



class AnswerOut(BaseModel):

    id:int

    content:str


    class Config:

        from_attributes=True
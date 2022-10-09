from pydantic import BaseModel

class Tasks(BaseModel):
    task_no:int
    description:str
    status:str
    
class TaskUpdate(BaseModel):
    status:str
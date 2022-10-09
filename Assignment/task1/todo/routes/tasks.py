from fastapi import APIRouter
from config.db import sess
from models.task import Task
from schemas.task import Tasks, TaskUpdate
user = APIRouter()


@user.get('/')
async def list_data(skip: int = 0, limit: int = 100):
    obj = sess.query(Task).offset(skip).limit(limit).all()
    return obj


@user.get('/{id}')
async def retrieve_data(id:int):
    obj = sess.query(Task).filter(Task.id==id).first()
    return obj


@user.post('/')
async def create_data(task:Tasks):
    print(task)
    t1 = Task(task_no=task.task_no, description=task.description, status=task.status)
    try:
        sess.add(t1)
        sess.commit()
        sess.refresh(t1)

    except:
        return {'message': 'Could not Add data'}
    finally:
        
        sess.close()
    return t1


@user.patch("/{id}")
async def update_data(id:int, task:TaskUpdate):
    sess.query(Task).filter(Task.id==id).update({
        Task.status:task.status
    })
    sess.commit()
    sess.close()
    return {'message':'Completed'}


@user.delete('/{id}')
def delete_data(id:int):
    sess.query(Task).filter(Task.id==id).delete()
    return {'message':'Delete Done'}

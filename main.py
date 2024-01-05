from fastapi import FastAPI, Body

from cruds import item as item_cruds


app = FastAPI()


@app.get('/items')
async def find_all():
    return item_cruds.find_all()


@app.get('/items/{id}')
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)


@app.get('/items/')
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)


@app.post('/items')
async def create(item_create=Body()):
    return item_cruds.create(item_create)


@app.put('/items/{id}')
async def update(id: int, item_update=Body()):
    return item_cruds.update(id, item_update)


@app.delete('/items/{id}')
async def delete(id: int):
    return item_cruds.delete(id)

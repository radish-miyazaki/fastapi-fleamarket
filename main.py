from fastapi import FastAPI


app = FastAPI()


@app.get('/test')
async def example():
    return {'message': 'Hello World'}

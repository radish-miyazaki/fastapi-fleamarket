import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from routers import item, auth


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.middleware('http')
async def add_process_time_header(req: Request, call_next):
    start_time = time.time()
    resp = await call_next(req)

    process_time = time.time() - start_time
    resp.headers['X-Process-Time'] = str(process_time)
    return resp


app.include_router(item.router)
app.include_router(auth.router)

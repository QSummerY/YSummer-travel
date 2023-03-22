import uvicorn
from fastapi import FastAPI
from views.travel import travel

app = FastAPI()

app.include_router(travel, prefix='/travel', tags=['出行'])


if __name__ == '__main__':
    uvicorn.run(app="app:app", host='127.0.0.1', port=5003, reload=True)

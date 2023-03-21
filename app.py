import uvicorn
from fastapi import FastAPI,responses
from views.travel import travel
from sqlalchemy import create_engine
from config import DB_URI


# pip3 fastapi uvicorn
app = FastAPI()

app.include_router(travel, prefix='/travel', tags=['出行'])

engine = create_engine(DB_URI)

if __name__ == '__main__':
    uvicorn.run(app="app:app", host='127.0.0.1', port=5003, reload=True)

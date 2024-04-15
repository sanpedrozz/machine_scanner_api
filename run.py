# run.py

import uvicorn
from fastapi import FastAPI

from logger import logger

logger.info(f"{'*' * 100}")
logger.info('{:^100}'.format('Запуск сервиса'))
logger.info(f"{'*' * 100}")

from routers import router

app = FastAPI()
app.include_router(router, prefix="/api")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

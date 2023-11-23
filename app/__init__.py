import asyncio
import logging
from sys import stdout
from fastapi import FastAPI

app = FastAPI()

# Setup logger
logger = logging.getLogger(__name__)
formatter = logging.Formatter("\x1b[36;20m%(levelname)s\x1b[0m:     %(message)s [\x1b[36;20m%(asctime)s\x1b[0m]")

# Logger handler
handler = logging.StreamHandler(stdout)
handler.setFormatter(formatter)

# Logger configuration
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Load configuration
from app.core import config 
settings = config.settings

# Setup API routers 
from app.api.v1 import api_router
app.include_router(api_router)

# Setup background loop
from app.core import background_tasks
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(background_tasks.fetch_third_party_data())

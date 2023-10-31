from fastapi import FastAPI

from src.controller import controller_clinicaltrials, controller_log

application = FastAPI()

application.include_router(controller_clinicaltrials.router)
# application.include_router(controller_log.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(application, host="0.0.0.0", port=8000)

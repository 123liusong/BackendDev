
import uvicorn
from fastapi import FastAPI
from apis import test
from apis.user import user

app = FastAPI()


# app.include_router(test.test_app, prefix="/test", tags=["test"])
app.include_router(user.user_api, prefix="/user", tags=["user"])

# uvicorn app.run:app --reload
if __name__ == "__main__":
    uvicorn.run('run:app', host='127.0.0.1',
                port=8000, reload=True)

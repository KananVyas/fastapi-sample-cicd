from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if item_id == 1:
        q = "hello_kanan"
    elif item_id == 2:
        q = "hello_dhruvi"
    elif item_id == 3:
        q = "hello_ruhanii"
    else:
        q = "hello_unknown"
    return {"item_id": item_id, "q": q}
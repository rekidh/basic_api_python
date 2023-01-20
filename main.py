from typing import Union  
# #this line recommendation  from fastapi if you disable no problem

from fastapi import FastAPI
import controllers.Auth as test 



app = FastAPI()


@app.get("/")
def read_root():
    h= test.test("request2")
    return {"Hello": "World","h":{h}}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
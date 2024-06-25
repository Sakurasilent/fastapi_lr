"""
路径参数
"""

from fastapi import FastAPI

app = FastAPI()
"""
经过测试 存在两个相同访问路径 默认会选择第一个进行请求
"""


@app.get("/items/{item_id}")
async def read_item_int(item_id:int):
    print("read_item_int")
    return {"item_id_int":item_id}

@app.get("/items/{item_id}")
async def read_item(item_id):
    print("read_item")
    return {"item_id":item_id}
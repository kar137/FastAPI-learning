from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")  # item_id is the path parameter
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None    # Here needy is a required query parameter, skip has a default int and limit is entirely optional.
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
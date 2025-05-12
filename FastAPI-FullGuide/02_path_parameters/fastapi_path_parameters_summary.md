
# 📌 FastAPI Path Parameters Summary

## 1. Basic Path Parameter
- Declare path parameters using `{}` in the URL path (e.g., `/items/{item_id}`).
- Passed directly as arguments to your function.

```python
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

## 2. Typed Path Parameters
- Use Python type annotations (e.g., `int`) for automatic type conversion and validation.

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

- FastAPI converts `"3"` → `3` (str → int).
- Invalid types return a 422 error with detailed info.

## 3. Interactive Documentation
- Auto-generates Swagger UI (`/docs`) and ReDoc (`/redoc`) using OpenAPI.
- Type annotations reflect directly in docs.

## 4. Path Matching Order
- Declare fixed paths (e.g., `/users/me`) **before** dynamic ones (`/users/{user_id}`) to avoid conflicts.

## 5. Predefined Values with Enums
- Use Python `Enum` to restrict accepted values.

```python
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    ...
```

- Supports `.value` to get raw string, and enum instances can be returned in JSON.

## 6. Path Parameters Containing Paths
- Use `:path` to capture full file paths, including slashes.

```python
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

- Double slashes (`//`) allow leading slashes in path.

## ✅ Key Advantages
With FastAPI, by using short, intuitive and standard Python type declarations, you get:

- Editor support: error checks, autocompletion, etc.
- Data "parsing"
- Data validation
- API annotation and automatic documentation

And you only have to declare them once.

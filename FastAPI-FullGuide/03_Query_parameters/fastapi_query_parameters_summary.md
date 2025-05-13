# 🔍 Query Parameters in FastAPI

## ✅ What Are Query Parameters?
- Parameters not part of the path (`/items/`) but added after a `?` in the URL.
- Example:  
  `http://127.0.0.1:8000/items/?skip=0&limit=10`  
  → `skip` and `limit` are query parameters.

## 🧠 Type Conversion & Validation
- Declared types like `int`, `str`, `bool` are automatically converted and validated.
- FastAPI provides:
  - Editor support
  - Parsing & validation
  - Automatic documentation

## 📦 Default Values & Optional Parameters
- Query parameters can have default values (i.e., optional).
  ```python
  async def read_item(skip: int = 0, limit: int = 10)
  ```
  → `skip` and `limit` are optional with defaults.

- Optional parameters can also be explicitly set as `None`.
  ```python
  q: str | None = None
  ```

## ✅ Boolean Conversion
- FastAPI converts common truthy strings (`true`, `1`, `yes`, `on`, etc.) to `True`.
  ```python
  short: bool = False
  ```

## 🔄 Combining Path and Query Parameters
- You can use multiple path and query parameters together.
  ```python
  @app.get("/users/{user_id}/items/{item_id}")
  async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False)
  ```

## ❗ Required Query Parameters
- Omit the default value to make a query parameter **required**.
  ```python
  async def read_user_item(item_id: str, needy: str)
  ```

## 🧩 Mixed Parameter Types
- You can combine:
  - Required parameters (no default)
  - Optional parameters (default `None`)
  - Parameters with default values

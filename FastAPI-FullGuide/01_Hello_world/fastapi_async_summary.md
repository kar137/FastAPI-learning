
# Concurrency and async / await (FastAPI Summary)

This summary covers the key points about using `async def` and `await` in FastAPI for concurrency and asynchronous programming.

---

## Quick Guidelines

✅ If using third-party libraries requiring `await`:
```python
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```

✅ If using synchronous libraries (most DB libraries):
```python
@app.get('/')
def results():
    results = some_library()
    return results
```

✅ If unsure, use `def` — FastAPI will handle it.

✅ You can mix `def` and `async def` as needed.

---

## Key Concepts

### Asynchronous Code

- Lets the program **wait** for slow tasks (I/O operations) while doing other work.
- Examples: waiting for a database query, file read/write, API call, or network response.
- Opposite: **Synchronous/Sequential**, where it waits and blocks each step.

### Concurrency vs Parallelism

- **Concurrency**: Many tasks managed by switching attention (good for I/O-bound tasks).
- **Parallelism**: Many tasks done *simultaneously* (good for CPU-bound tasks).

Example:
- FastAPI leverages concurrency for handling many web requests efficiently.
- You can also combine it with parallelism (e.g., multiprocessing) for CPU-heavy tasks like machine learning.

### async / await

- Use `async def` to define async functions.
- Use `await` to pause until an async function completes.

Example:
```python
async def get_burgers(number: int):
    return await cook_burgers(number)

@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers
```

> **Note:** You can only use `await` inside `async def`.

### Running async Code Without FastAPI

- FastAPI/Starlette are built on AnyIO, compatible with asyncio and Trio.
- You can use libraries like [Asyncer](https://github.com/tiangolo/asyncer) for easier async + sync mixing.

---

## Summary Takeaway

FastAPI's async capabilities give you:
- **Concurrency** (better I/O handling, like Node.js or Go).
- Option to combine with **parallelism** for CPU-heavy tasks.
- Easy-to-use syntax (`async`/`await`) making async code cleaner and more efficient.

## Note
- Refer to this documentation for more details: https://fastapi.tiangolo.com/async/


from fastapi import FastAPI #FastAPI is a python class that provides all functionality of our api

app = FastAPI()   # app which is an instance will be the main point of interaction to create all our API.


@app.get("/")
async def root():
    return {"message": "Hello World"}


# WorkFlow:
# Import FastAPI.
# Create an app instance.
# Write a path operation decorator using decorators like @app.get("/").
# Define a path operation function; for example, def root(): ....
# Run the development server using the command fastapi dev.
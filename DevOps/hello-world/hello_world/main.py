from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}



# def hello_world():
#     return "Hello World!"

# result : str = hello_world()
# print(result).main
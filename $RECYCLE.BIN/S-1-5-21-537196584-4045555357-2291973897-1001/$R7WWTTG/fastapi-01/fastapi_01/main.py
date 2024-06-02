from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello Sarim'}

@app.get('/about')
def about():
    return {'message': 'This is about page'}
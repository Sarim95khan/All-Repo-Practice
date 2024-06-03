from fastapi import FastAPI
from sqlmodel import SQLModel,Field
from typing import Optional, AsyncGenerator, Union
from contextlib import asynccontextmanager
import asyncio
from pydantic import BaseModel
from aiokafka import AIOKafkaProducer
import asyncio
import json
from kafka_messaging import settings

class Order(SQLModel):
    id:Optional[int] = Field(default=None)
    username:str
    product_id:int
    product_name:str
    product_price:int


@asynccontextmanager
async def lifespan(app: FastAPI)-> AsyncGenerator[None, None]:
    # print("Creating tables..")
    print("Creatomg Kafka.....")
    yield

app = FastAPI(lifespan=lifespan, title="Product Kafka Service", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        },
        ])    

@app.get("/")
def get_all_order():
    return {
        "username":"Yahya",
         "product_id":123,
         "product_name":"Laptop",
         "product_price":33
        }

@app.get("/create-order")
def create_order():
    return {
        "username":"Sarim",
         "product_id":123,
         "product_name":"Laptop",
         "product_price":33
        }

@app.post("/create_order")
async def create_order(order:Order):
    print('Creating AIOKafka Producer')
    producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_SERVER)
    await producer.start()
    print("ORder JSON:")
    orderJSON= json.dumps(order.__dict__).encode('utf-8')
    try:
        # Produce message
        await producer.send_and_wait(settings.KAFKA_TOPIC, b"Sarim Topic")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
    return orderJSON

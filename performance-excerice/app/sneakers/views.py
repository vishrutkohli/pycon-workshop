from loguru import logger
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.core.db.session import get_db , engine
from app.sneakers.models import Sneaker as SneakerModel
from app.sneakers.schema import SneakerSchema
from random import randrange
import time
import requests
import asyncio
import httpx
router = APIRouter()


@router.get("/random_sneakers", status_code=200)
async def get_random_sneakers(db: Session = Depends(get_db)):
    sneaker_ids = [randrange(1,100) for i in range(10)]
    sneaker_details = []
    for sneaker_id in sneaker_ids:
        details = db.query(SneakerModel).filter(SneakerModel.id == sneaker_id).first()
        sneaker_details.append(details)
    return sneaker_details


@router.get("/search_sneaker", status_code=200)
async def get_sneaker_search(db: Session = Depends(get_db) , name: str = 'blah'):  
    sneakers = db.query(SneakerModel).filter(SneakerModel.name ==name).all()
    return sneakers

@router.get("/get-data-from-different-service", status_code=200)
async def get_sneaker_search(db: Session = Depends(get_db)):
    for _ in range(3):
        data = requests.get('http://jsonplaceholder.typicode.com/posts/1').text
        print(data)

    return data

@router.get("/get-data-sync", status_code=200)
def get_sneaker_search(db: Session = Depends(get_db)):
    urls = ['http://jsonplaceholder.typicode.com/posts/{}'.format(i) for i in range(5)]
    data = []
    for url in urls:
         data.append(fetch_data_sync(url))

    return data

def fetch_data_sync(url):
    response = requests.get(url)
    data = response.text
    return data





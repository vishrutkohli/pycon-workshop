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
    sneaker_ids = [randrange(1,10000000) for i in range(100)]
    sneaker_details = []
    for sneaker_id in sneaker_ids:
        details = db.query(SneakerModel).filter(SneakerModel.id == sneaker_id).first()
        sneaker_details.append(details)
    return sneaker_details

@router.get("/search_sneaker", status_code=200)
async def get_sneaker_search(db: Session = Depends(get_db) , name: str = 'blah'):  
    sneakers = db.query(SneakerModel).filter(SneakerModel.name ==name).all()
    return sneakers

@router.get("/get-data", status_code=200)
def get_sneaker_search(db: Session = Depends(get_db)):
    urls = ['http://jsonplaceholder.typicode.com/posts/{}'.format(i) for i in range(1,10)]
    data = []
    for url in urls:
         data.append(fetch_data(url))

    return data

def fetch_data(url):
    response = requests.get(url)
    data = response.text
    return data






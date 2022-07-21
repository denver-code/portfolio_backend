import os

from motor.metaprogramming import asynchronize
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('DATABASE_LOCAL', "mongodb://127.0.0.1:27017"))


db = client["Portfolio"]
posts = db["posts"]


async def insert_db(db, data):
    return await globals()[db].insert_one(data)

async def find_one_query(db, querry):
    return await globals()[db].find_one(querry)

async def find_query(db, querry):
    cursor =  globals()[db].find(querry)
    return await cursor.to_list(length=1000)
    
async def update_db(db, scdata, ndata):
    return await globals()[db].update_one(scdata, {"$set": ndata}, upsert=True)

async def delete_db(db, obj):
    await globals()[db].delete_one(obj)
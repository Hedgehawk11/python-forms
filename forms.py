import pymongo
from pymongo import MongoClient
import sys


def setup(uri):
  global client
  client = MongoClient(uri)
  try:
    client.admin.command('ping')
    print("Connected to server")
  except Exception as e:
    print('ruh roh raggy')

def register(name,answer):
  #edit the names of db and collection to your mongo db and collection names
  db = client.put_yours_here
  collection = db.put_yours_here
  collection.insert_one({"name":name,"answer":answer})
  print("Registered")
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb photos")
os.system("createdb photos")

model.connect_to_db(server.app)
model.db.create_all()

## create 5 new users
for num in range(1, 5):
    fname = f"user{num}"
    lname = f"user{num}"
    email = f"user{num}@test.com"  # Voila! A unique email!
    password = "123"
 
    user = crud.create_user(fname, lname, email, password)

## create 2 albums

album1 = crud.create_album(name='Colorado', date_created=datetime.now())
album2 = crud.create_album(name='Utah', date_created=datetime.now())

## load json data file
with open("data/fake_photos.json") as f:
    photo_data = json.loads(f.read())

## iterate through json data and add each photo as a new photo
photos_in_db = []
for photo in photo_data:
    user_id = photo["user_id"]
    date_uploaded = datetime.now()
    date_taken = datetime.strptime(photo["date_taken"], "%Y-%m-%d %H:%M")
    album_id = photo["album_id"]
    path = photo["path"]

    db_photo = crud.create_photo(user_id, date_uploaded, date_taken, album_id, path)
    photos_in_db.append(db_photo)


## create 5 new users
for num in range(1, 5):
    fname = f"user{num}"
    lname = f"user{num}"
    email = f"user{num}@test.com"  # Voila! A unique email!
    password = "123"

 
    user = crud.create_user(fname, lname, email, password)

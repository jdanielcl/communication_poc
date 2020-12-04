import json
import os
import urllib.request
import urllib.parse
import shutil
from typing import Optional

from fastapi import FastAPI

app = FastAPI()
FILES_URL = os.getenv('FILES_URL', "http://localhost:8000")
UPLOAD_PATH = os.getenv('UPLOAD_PATH', "uploads")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/process_job')
def process_job(request: dict):
    data = request
    url = urllib.parse.urljoin(FILES_URL, data.get("file"))
    file_name = url.split("/")[-1]
    with urllib.request.urlopen(url) as response, open(os.path.join(
            UPLOAD_PATH, file_name), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    return "The file has been saved", 204


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

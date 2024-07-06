from fastapi import FastAPI, File, UploadFile
import shutil
from fastapi.staticfiles import StaticFiles

app=FastAPI()

@app.post("/file")
def get_file(file: UploadFile=File(...)):
    path=f"files/{file.filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {
        "filename":path,
        "type":file.content_type
    }

app.mount("/files", StaticFiles(directory="files"), name="files")
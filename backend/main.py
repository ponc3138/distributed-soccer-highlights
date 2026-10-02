from fastapi import FastAPI, UploadFile, HTTPException
from pathlib import Path

app = FastAPI()

# top row is video extensions, bottom row is audio extensions
allowed_file_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.webm',
                           '.mp3', '.aac', '.flac'}

@app.get("/health")
def health_check():
    return {"server": "healthy"}

@app.post("/uploadfile")
async def file_upload(file : UploadFile):

    file_name = file.filename
    file_extension = Path(file_name).suffix.lower()

    if(file_extension in allowed_file_extensions):
        return {"file" : file_name}
    else: 
        # error code 415 is unsupported media type 
        raise HTTPException(status_code=415, detail="File type not accepted")
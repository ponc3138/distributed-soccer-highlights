from fastapi import FastAPI, UploadFile, HTTPException
from pathlib import Path
import shutil
import uuid


app = FastAPI()

# top row is video extensions, bottom row is audio extensions
allowed_file_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.webm',
                           '.mp3', '.aac', '.flac'}

@app.get("/health")
def health_check():
    return {"server": "healthy"}

@app.post("/uploadfile")
async def file_upload(file : UploadFile):
    # store file name and the extension
    file_name = file.filename
    file_extension = Path(file_name).suffix.lower()

    if(file_extension in allowed_file_extensions):
        # get temporary file object containing the uploaded media 
        stored_file = file.file

        # create new filename with uuid
        file_uuid = uuid.uuid4()
        file_name_uuid = str(file_uuid) + file_extension

        # build the path where the uploaded file will be stored
        upload_dir = Path("uploads")

        # create the uploads directory if it doesn't already exist
        upload_dir.mkdir(parents=False, exist_ok=True)

        # build the full path for uploaded file
        destination = upload_dir / file_name_uuid

        # copy uploaded file to local storage
        # "wb" creates the file if it doesn't exist and overwrites it if it does.
        with open(destination, "wb") as f:
            shutil.copyfileobj(stored_file, f)
        
        return {"file" : file_name}
    else: 
        # error code 415 is unsupported media type 
        raise HTTPException(status_code=415, detail="File type not accepted")
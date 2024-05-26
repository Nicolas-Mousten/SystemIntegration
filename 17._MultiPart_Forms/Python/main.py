from fastapi import FastAPI, Form, File, UploadFile
import aiofiles
from typing import Optional


app = FastAPI()


@app.post("/form")
def basic_form(username: str = Form(...), password: str = Form(default=..., min_length=8)):
    print(username, password)
    return { "username": username }

@app.post("/fileform")
async def file_form(file: UploadFile = File(...), description: Optional[str] = Form(None)):
    print(description)

    safe_filename = file.filename.replace("/", "_").replace("\\", "_")

    #aiofiles er asynchronus mens open ikke er det.
    async with aiofiles.open (safe_filename, 'wb') as f:
        #walrus operator :=        something happens and it overites the operator, this case content. 
        while content := await file.read(1024): #read in 1024 chunks
            await f.write(content)






# async def file_form(file: UploadFile = File(...), description: Optional[str] = Form(None)):
#     safe_filename = file.filename.replace("/", "_").replace("\\", "_")

#     with open (safe_filename, 'wb') as t:
#         #walrus operator :=        something happens and it overites the operator, this case content. 
#         while content := await file.read(1024): #read in 1024 chunks
#             t.write(content)

            




# async def file_form(file: UploadFile = File(...), description: Optional[str] = Form(None)):
#     contents = await file.read()
#     print(contents)
#     return { "filename" : file.filename }
    
    
    # with open("file.py", "wb") as file:
    #     file.write(file)

    # return { "message":"file Uploaded" }

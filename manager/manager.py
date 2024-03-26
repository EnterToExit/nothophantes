from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response 
import requests
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
import requests
import uvicorn


app_manager = FastAPI()


@app_manager.post("/send_audio_to_process")
async def send_audio_to_process(audio_file: UploadFile = File(...)):
    if audio_file.content_type != "audio/mpeg":
        raise HTTPException(status_code=400, detail="Поддерживаются только файлы аудио формата MPEG")
    
    response = requests.post("http://localhost:9000/asr", files={"audio_file": audio_file.file})
    if response.status_code == 200:
        print(response.text)
        process_response = requests.post("http://localhost:9001/nlp", json={"text": response.text})
        if process_response.status_code == 200:
            processed_text = process_response.text
            return {"processed_text": processed_text}
        else:
            error_message = f"Произошла ошибка при обработке текста на сервере: {process_response.status_code}"
            raise HTTPException(status_code=process_response.status_code, detail=error_message)
    else:
        error_message = f"Произошла ошибка при отправке аудиофайла на обработку: {response.status_code}"
        raise HTTPException(status_code=response.status_code, detail=error_message)
    
    

if __name__ == "__main__":
    uvicorn.run(app_manager, host="localhost", port=8000)
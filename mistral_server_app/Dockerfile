FROM python:3.11

WORKDIR /app

COPY mistral_server.py /app/
COPY mistralQ2_K.gguf /app/

RUN pip install fire llama-cpp-python fastapi requests uvicorn pydantic

EXPOSE 9001

ENTRYPOINT ["uvicorn", "mistral_server:app_nlp", "--host", "0.0.0.0", "--port", "9001"]

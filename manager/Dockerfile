FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY manager.py /app/

RUN pip install requests

EXPOSE 8000

ENTRYPOINT ["uvicorn", "manager:app_manager", "--host", "0.0.0.0", "--port", "8000"]

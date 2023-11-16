FROM pytorch/pytorch:latest

WORKDIR /

COPY requirements.txt ./

COPY . .

RUN pip install "uvicorn[standard]"

RUN pip install fastapi

CMD [ "python", "./run.py" ]
FROM python:3.6
WORKDIR /app/IOTAP-Controller
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY configs /app/IOTAP-Controller/configs
COPY mocks /app/IOTAP-Controller/mocks
COPY src /app/IOTAP-Controller/src
COPY README.md /app/IOTAP-Controller/
ENTRYPOINT ["python", "./src/main.py"]
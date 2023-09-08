FROM python:3.11

WORKDIR /

COPY . /

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000
CMD ["python", "main.py"]
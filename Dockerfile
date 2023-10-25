FROM python:3.11.2-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && \
    apt-get install -y tesseract-ocr \
                       libtesseract-dev \
                       libsm6 libxext6 libxrender-dev
COPY . .
ENV TESSDATA_PREFIX /usr/share/tesseract-ocr/4.00/tessdata
EXPOSE 8080
CMD ["python3","manage.py","runserver","0.0.0.0:8080"] 

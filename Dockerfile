FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install nano && apt-get install ffmpeg -y
RUN pip install -r requirements.txt
ENTRYPOINT ["tail", "-f", "/dev/null"]
#CMD python ./videoPlaylist.py

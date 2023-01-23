FROM python:3.10.9
USER root

ENV TRANSFORMERS_OFFLINE 1

WORKDIR /app

# install
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip3 install transformers pandas

COPY hugging_face_sentiment_test/resources /app/hugging_face_sentiment_test/resources
COPY hugging_face_sentiment_test/model_benchmark.py /app/hugging_face_sentiment_test

ENV PYTHONPATH /app

CMD python hugging_face_sentiment_test/model_benchmark.py
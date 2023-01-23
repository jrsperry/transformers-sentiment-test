FROM tensorflow/tensorflow:2.11.0

USER root

ENV TRANSFORMERS_OFFLINE 1

WORKDIR /app

COPY docker_requirements.txt /app
RUN pip install -r docker_requirements.txt

COPY hugging_face_sentiment_test/resources /app/hugging_face_sentiment_test/resources
COPY hugging_face_sentiment_test/test_models.py /app/hugging_face_sentiment_test

ENV PYTHONPATH /app

CMD python hugging_face_sentiment_test/test_models.py

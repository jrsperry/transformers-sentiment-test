import logging
from transformers import pipeline

import os
import pandas as pd
import time
import sys

logger = logging.getLogger("sentiment_tester")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(levelname)-8s :   %(message)s'))
logger.addHandler(handler)
log_level = os.environ.get("LOGGING_LEVEL", "INFO")
logger.setLevel(log_level)

# if you don't have the model downloaded, set MODEL_PATH to 'cardiffnlp/twitter-roberta-base-sentiment'
# and set TRANSFORMERS_OFFLINE to 0
os.environ['TRANSFORMERS_OFFLINE'] = '1'
MODEL_PATH = "./hugging_face_sentiment_test/resources/model"

logger.info("loading model")
classifier = pipeline(task="sentiment-analysis", model=MODEL_PATH, tokenizer=MODEL_PATH, max_length=512,
                      truncation=True)

number_sentences = os.environ.get('NUMBER_SENTENCES', '100')
number_sentences_int = int(number_sentences)

text_sentences = list(pd.read_csv('./hugging_face_sentiment_test/resources/amazon_sentences.csv')['text'])[:number_sentences_int]

iterations = os.environ.get('ITERATIONS', '25')
iterations_int = int(iterations)
logger.info(f"running {iterations_int} iterations on {len(text_sentences)} sentences")

for i in range(iterations_int):
    beforeAll = time.time()
    preds = classifier(text_sentences)
    afterall = time.time()
    logger.info(f"time to do {len(text_sentences)} sentences:  {afterall - beforeAll}s")
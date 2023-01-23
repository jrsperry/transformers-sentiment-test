# Huggingface Sentiment Test

This is designed to be a test project to test the performance of out-of-the-box transformers. The model is stored here 
in the project to decrease startup time when running in the cloud but i can't store those large of files in my github...

## Docker tags

There are 6 tags available at [sperry/1996 docker hub](https://hub.docker.com/repository/docker/sperry1996/transformers-sentiment-test/general). 
All the tags are run with a pytorch backend unless otherwise noted. A couple have a tensorflow backend. The docker images were
built with the model on the image to avoid downloading on startup. 

Env vars:
- ITERATIONS = how many iterations to run (default 25)
- NUMBER_SENTENCES = how many sentences per iteration (default 100)
- MODEL_PATH = which model to load, by default it will load the cardiffnlp/twitter-roberta-base-sentiment stored locally in the image. 

### Primary Images
The 0.0.1-CPU has python 3.10.9, torch 1.13.1, and transformers 4.25.1
(see Dockerfile for more details)

The 0.0.1 has python 3.10.8, torch 1.12.1, and transformers 4.24.0. (see Dockerfile.multi for more details)

### Other Images
the 0.0.1-INTEL has a pytorch intel optimized runtime with python 3.8.16, torch 1.12.1+cpu, and transformers 4.25.1
(see Dockerfile.intel for more details)

The 0.0.1-PYTORCH has python 3.9.12, torch 1.13.0, and transformers 4.25.1 (see Dockerfile.pytorch for more details)

0.0.1-HF is using the huggingface docker image, transformers version 4.23.1, pytorch (see Dockerfile.hf for more details)

0.0.1-TF has tensorflow 2.11.0 installed (see Dockerfile.tf for more details)

0.0.1-HFTF is using the huggingface docker image with tensorflow backend (see Dockerfile.hftf for more details)



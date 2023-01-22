# Huggingface Sentiment Test

This is designed to be a test project to test the performance of out-of-the-box transformers. The model is stored here 
in the project to decrease startup time when running in the cloud but i can't store those large of files in my github...

## Docker tags

There are 3 tags available at [sperry/1996 docker hub](https://hub.docker.com/repository/docker/sperry1996/transformers-sentiment-test/general)

The 0.0.1 has python 3.10.8, torch 1.12.1, and transformers 4.24.0 (see Dockerfile.multi for more details)

the 0.0.1-INTEL has a pytorch intel optimized runtime with python 3.8.16, torch 1.12.1+cpu, and transformers 4.25.1
(see Dockerfile.intel for more details)

The 0.0.1-CUDA has python 3.9.12, torch 1.13.0, and transformers 4.25.1 (see Dockerfile.cuda for more details)

Env vars:
- ITERATIONS = how many iterations to run (default 25)
- NUMBER_SENTENCES = how many sentences per iteration (default 100)
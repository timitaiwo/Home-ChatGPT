# An LLM Web Application 
A simple flask application that runs a local copy of the [AMD OLMo language model](https://huggingface.co/amd/AMD-OLMo).

## Instructions
- run ```python main.py``` in the terminal then open http://127.0.0.1:5000 or localhost:5000 in your browser.

## Warnings
- The model is roughly 5GB and has to be downloaded the first time the application is run. Please account for your device storage and download speed as appropriate.
- A test run I did had the model load in 16 seconds and give a response in 1 minute 17 seconds to get a response on my system (an Intel Core i5, 8GB laptop). Model response times would vary based on your device specifications e.g RAM size, CPU speed etc.

# Sample
A running sample is given below

![Screenshot of the application homepage](images/AMD_OLMo_question.png)

The response is 

![Screenshot of the response to the question "What is the Nicene creed?"](images/AMD_OLMo_response.png)

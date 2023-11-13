## Company: AI Camp/ Rakugo Media
## Authors: Elian Ahmar, Lucas Wat, Cash Popik

## This file handles all of the external calls to different api's

"""
Implement api.py which establishes the connection to the openAI api.
Make sure you hide api keys.
You never want to commit api keys to github.
Also, add backoff to your api calls.
If you have questions about this please ask.
**Cash, Lucas**
"""

# NOTE: DO NOT REVEAL API KEYS. 

import pandas as pd
import numpy as np
import math
import requests
import openai
import os
from bs4 import BeautifulSoup
import requests
import re
import argparse
import backoff

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

# this is the backoff flag that will slow down api calls
# (exponentially) until success
@backoff.on_exception(backoff.expo, openai.RateLimitError)
def gpt(model_name, syst_msg, user_input):
    """
    This method queries the openai api

    model_name -> string denoting what model to deploy
    syst_msg -> string denoting what role the chatbot should take
    user_input -> text input you want the model to respond to
    """
    #openai.api_key = os.environ["OPENAI_API_KEY"]  #initialize our api keys
    # SET:
    # windows:  set OPENAI_API_KEY=hi
    # apple:    export OPENAI_API_KEY="hi"
    # VIEW:
    # windows:  echo %OPENAI_API_KEY%
    # apple:    echo $OPENAI_API_KEY
    
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": syst_msg}, #this tells GPT what role we want it to play
            {"role": "user", "content": user_input}, #this is the prompt demonstrating how we want GPT to scrape
        ],
        temperature=0, #we want low temperature. This makes the output less random and more deterministic
    )
    return response.choices[0].message.content #return the first generated response

# this is probably the use case:

# if __name__ == "__main__":
#     syst_msg = "You are an assistant for a lawyer."
#     model="gpt-4"
#     prompt="Draft a legal contract that states that Mr. Beast must create 4 new youtube videos that promote Toyota cars."
#     print(gpt(model, syst_msg, prompt))
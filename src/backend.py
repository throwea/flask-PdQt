## Company: AI Camp/ Rakugo Media
## Authors: Elian Ahmar

## this file should contain the function needed to run our entire backend pipeline. After we finish the backend we will add other functions in here to connect our backend to the front end

import argparse
import input_file
import structure
import api

def main(payload): #
    '''
    This function should run our backend pipeline from end-2-end and return the output from our LLM

    params --> you guys decide ;D
    '''
    # prompt
    prompt = open("sys_prompt.txt", "r", encoding="utf-8").read()
    #payload is our pdf for now. Read in the pdf
    text = input_file.extract_text(payload)
    #make api request to gpt
    response = (api.gpt("gpt-4-1106-preview", prompt, text))
    #return the aggregated response
    return response


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog='main',
        description='What the program does')
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args.filename)




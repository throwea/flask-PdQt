## Company: AI Camp/ Rakugo Media
## Authors: Elian Ahmar, Lucas Wat, Steven Wang

## This file handles the extraction of text from our pdf document

import fitz  # imports the pymupdf library
import docx2txt


def extract_text(path_to_file):
    pages = []
    if path_to_file.endswith('.pdf'):
        doc = fitz.open(path_to_file)  # open a document
        for page in doc:  # iterate the document pages
            pages.append(page.get_text())  # get plain text encoded as UTF-8

    elif path_to_file.endswith('.txt'):
        with open(path_to_file, "r", encoding="utf-8") as file:
            pages.append('\n'.join(file.readlines()))

    elif path_to_file.endswith('.docx'):
        text = docx2txt.process(path_to_file)
        pages.append(text)

    else:
        return "invalid file type"

    return pages

# def chunk_text(text):
#     '''
#     This method needs to take in the text that we get from reading the pdf
#     and it needs to chunk it such that the number of tokens
#     '''
#     # create a new list that will store the chunks of text
#     # aggregate 2 pages of text and turn them into one string
#     # send that string to the newly initialized list
#     # return that list
#     chunks = []
#     # get system prompt token size
#     with open('sys_prompt.txt', 'r', encoding="utf-8") as f:
#         sys_prompt_size = len(encode_tokens(f.read()))

#     text = "".join(text) # take the separated pages into one stream of text
#     text = text.replace("  ", " ")  # in case the previous line or any other cases have any double spaces

#     tokens = encode_tokens(text)  # encode into tokens
#     token_count = len(tokens)  # count them

#     chunk_size = 4096 - sys_prompt_size  # amount of tokens minus prompt size

#     chunk_count = token_count / chunk_size  # amount of chunks we have

#     # return text with no chunking if there are less tokens in text than chunk_size
#     if chunk_count <= 1:
#         chunks = [text]

#     else:
#         chunk_count = math.trunc(chunk_count)  # cuts off decimals from chunk_count; determines how many full (4096-sys_prompt_size) chunks to make
#         start = 0
#         for i in range(chunk_count):  # add each chunk decoded
#             chunk = tokens[start:start + chunk_size]
#             chunks.append(decode_tokens(chunk))
#             start += chunk_size

#         # creates the last chunk that isn't full
#         chunk = tokens[start:]
#         chunks.append(decode_tokens(chunk))

#     return chunks  # yay


# def encode_tokens(text):
#     enc = tiktoken.encoding_for_model("gpt-4")
#     tokens = enc.encode(text)
#     return tokens


# def decode_tokens(tokens):
#     enc = tiktoken.encoding_for_model("gpt-4")
#     text = enc.decode(tokens)
#     return text









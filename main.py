import os
from transformers import AutoTokenizer

os.getenv("HF_TOKEN")

toekinzer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it") 
toekinzer("diaz this is!!")
import argparse
import os 
import yaml 
import torch
from torch import package
from ftlangdetect import detect
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("--file-path", default='./sample-docs/text-1.txt', type=pathlib.Path )
parser.add_argument("--lang", default="en")
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if not os.path.isfile('latest_silero_models.yml'):
    torch.hub.download_url_to_file('https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml',
                                   'latest_silero_models.yml', 
                                   progress=False) 

with open('latest_silero_models.yml') as model_file:
    models = yaml.load(model_file, Loader=yaml.SafeLoader)
models_conf = models.get("te_models").get("latest")


with open(args.file_path, 'r') as file:
    input_text = file.read()

print("--------------- Unformatted text -----------------\n{}".format(input_text))

lang = args.lang

if lang == "detect":
    print('Detecting language...')
    lang = detect(text=input_text.replace('\n',''), low_memory=True)['lang']
    print(f"Language detected: {lang.title()}")

if args.debug:
  pass 
   




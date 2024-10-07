# OllamaModelTesting
A really really easy way to test various prompts in various models

## Usage
Put your prompts in the prompt file, the models you want to run in your model file. You can't use a model with "/" in it, otherwise you need to put a folder(s) with the name(s) of the left part.

Every prompt needss it's own line, so does every model. You can put blank lines they will be ignored. 

`python test_models_v0.11.py model_list.txt prompt_list.txt`

Outputs will be in the output folder.

##
The output has 3 tests of each prompt for each model.

## Warning: New runs squish the old output

###### There's probably a lot of optimisations and variants (not squish the old output, have the number of runs as a parameter, etc.) But I'm lazy in a min-max way, and this form is probably the easiest to modify and adapt, so don't expect any improvements.

## Requirements
I don't have a clue. Works in Python==3.12.6 and requires ollama obviously.

All code is GPLv3. MIT or BSD type licenses available for $.

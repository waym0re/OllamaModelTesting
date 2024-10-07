# OllamaModelTesting
A really really easy way to test various prompts in various models

## Usage
Put your prompts in the prompt file, the models you want to run in your model file. You can't use a model with "/" in it, otherwise you need to put a folders with the names of the left part.

Every prompt is it's own line, so is every model. 

`python test_models_v0.11.py model_list.txt prompt_list.txt`

Outputs will be in the output folder.

##
The output has 3 tests of each prompt for each model.

## Warning: New runs squish the old output

### There's probably a lot of optimisations and variants (not squish the old output, have the number of runs as a parameter, etc.) But I'm lazy in a min-max way, and this form is probably the easiest to modify and adapt, so don't expect any improvements.

All code is GPLv3. MIT or BSD type licenses available for $.

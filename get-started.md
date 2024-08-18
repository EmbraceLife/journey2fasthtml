
# How to get started

- Jeremy's Getting Started [Video](https://youtu.be/Auqrm7WFc0I)
- Jeremy's [interview](https://youtu.be/WuipZMUch18) with HTMX author Carson Gross
- read [htmx reference](https://htmx.org/reference/#attributes) 
- read [fastHTML docs](https://docs.fastht.ml/api/core.html#tests) 

# screen recording 

- start recording: `cmd + shift + 5`  
- end recording: `ctrl + cmd + esc`  

# Issues fixed

## no vpn

> make sure to turn off vpn first

## Internal Server Error

it may cause by inserting error data, like the following

```python
def input_selfCleaning(): 
    return Input(placeholder="Add a new todo", 
                           id='myTodo', 
                           name='title', # if use title1 instead, it will cause such error
                           hx_swap_oob='true') 
```

> create a new database file

```python

# change todos.db to todos1.db
app, rt, todos, Todo = fast_app('todos1.db', live=True, render=render, 
                                id=int, title=str, done=bool, 
                                pk='id')
```

## start a new env
```bash
conda deactivate 

mamba create -n fasthtml "python>=3.10" 

mamba activate fasthtml

pip install python-fasthtml 

or conda install -c conda-forge python-fasthtml

mamba deactivate 
```

## upgrade python to 3.10+

```bash
mamba install "python>=3.10" 
```
## versioning

```bash
pip show fastcore
pip show python-fasthtml
```

## update 
```
pip install --upgrade python-fasthtml
pip install --upgrade fastcore

```

## run local dev mode

```bash
git clone git@github.com:AnswerDotAI/fasthtml.git

cd fasthtml

pip install -e . 

mamba install "python>=3.10" 

pip install -e . 
```

## run example app locally

```bash
cd examples

python basic_app.py 

ctrl + c 

```


## vscode: get python interpreter right to show syntax and docs when hovering

1. cmd + shift + p
2. type: python 
3. type select interpreter
4. make sure it is the latest python version

## vscode: adjust to settings.json for code blocks highlighting


1. cmd + ,
2. click the top right corner with arrow icon button to open settings.json
3. add two lines like below to the file and save it
```json
"editor.bracketPairColorization.enabled": true,

"editor.guides.bracketPairs": "active"
```


## show output of all lines in a cell

```python
from fasthtml import common as fh

from fasthtml.common import *

from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
```

## learn fasthtml with custom chatgpt
https://chatgpt.com/g/g-xPqF9SZjM-fasthtml-helper



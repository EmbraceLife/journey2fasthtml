# 1. Final project appearance

1. Run the code below to reproduce Jeremy's final todo-list project to see the final appearance and 
2. how the interface work: try to click toggle, delete, and type to add

```python 
# my code without comment, the core is the same with Jeremy's. The differences are trivial.

from fasthtml.common import *


def render(todo):
    tid = f'todo-{todo.id}'
    delete = A('Delete',
                hx_delete=f'/delete/{todo.id}',
                hx_swap='outerHTML',
                target_id=tid) 
    toggle = A('Toggle', 
               hx_get=f'/toggle/{todo.id}',
               target_id=tid)
    return Li(toggle, delete,
              todo.title + (' ✅' if todo.done else ''),
              id=tid)
              

app, rt, todos, Todo = fast_app('todos2.db', live=True, render=render, 
                                id=int, title=str, done=bool, 
                                pk='id')


def mk_input():
    return Input(placeholder="Add a new todo", 
                           id='title', 
                           hx_swap_oob='true') 

@rt('/')
def get():
    frm = Form(Group(mk_input(),
                    Button("Add")),
               hx_post='/', 
               target_id='todo-list',
               hx_swap='beforeend') 
    
    return Titled('Todos', 
                  Card(
                      Ul(*todos(), id='todo-list'), 
                      header=frm) 
    )

@rt('/')
def post(todo:Todo): 
	return (todos.insert(todo), 
			mk_input()) 

@rt('/delete/{tid}') 
def delete(tid:int): todos.delete(tid) 

@rt('/toggle/{tid}') 
def get(tid:int): 
    todo = todos[tid] 
    todo.done = not todo.done
    todos.update(todo)
    return todo 

serve()  

```

# 2.  All HTML elements in python

1. paste the code below to jupyter notebook
2. split them into different cells to run 
3. see all the HTML elements of the project to be generated
4. notice it's all in python

```python
from fasthtml import common as fh 
from fasthtml.common import *
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

items = []
for i in range(5):
    if i % 2 == 0:
        items.append(Li(f'{i} is even: ✅'))
    else:
        items.append(Li(f'{i} is even: ❌'))
Ul(*items)


def input_selfCleaning():
    return Input(placeholder="Add a new todo", 
                           id='title', 
                           hx_swap_oob='true')
input_selfCleaning()
show(input_selfCleaning())


frm = Form(Group(input_selfCleaning(),
                    Button("Add")),
               hx_post='/',
               target_id='todo-list', 
               hx_swap='beforeend') 
frm 
show(frm)



card = Titled('Todos', 
                  Card(
                      Ul(*items, id='todo-list'), 
                      header=frm) 
    )
card
show(card)
```

> **But a web app requires to go From Static to Interactive**

We need a few more things to make it interactive and magical...

---

# 3 Get server, router, database ready

## get database ready

```python
# initialize app (the web app), rt (the router), todos (the database), Todo (the table class)
app, rt, todos, Todo = fast_app('todos.db', live=True, render=render,
								# define columns for the todo.db
                                id=int, # id column
                                title=str, # title column
                                done=bool, # done column
                                pk='id') # A primary key is a special relational database table column designated to uniquely identify all table records.
# todos is the database
# Todo is the class of table in the database
```

Use the following code to check what's inside `todos` and `Todo`
```python 
# check what's inside them
Todo?? 
todos.columns
todos??
```

What the data look like inside the database
- id: automatically increment
- done: default to None (auto convert to false later)

```python
todos.insert(title='insert a todo')
todos.insert(title='insert a second todo')
todos.get(1)
todos.get(2)
```
## Initialize server and router

By the way, the server `app` and router `rt` are also initialized at the same time. 

#### what is `app`?

a web application server based on the Starlette framework, with enhanced HTML and session handling capabilities, basically all the tools we need to build a web app is packed inside `app` .

### What is a `rt`?

It defines a route with a path and a function, when the path is accessed, the function is called on the server and the response is sent back to the client

---

# 4. Create a Form for entering and displaying todos

### Components for building Form to submit data

```python
Form(Group(mk_input(), Button("Add"))
```

- Normal HTML Tags 
	- [Input](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) element,
	- [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button) element,
	- [Form](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form) element,

- Picocss component:  
	- [Group](https://picocss.com/docs/group) element for grouping Input and Button together

> The combination of the elements is an easy and good choice, if you are experienced with html and css, the ways for submitting user input are endless.

### Components for displaying todos and Form

```python
Titled('Todos', 
	  Card(
		  Ul(*todos(), id='todo-list'), 
		  header=frm) 
```

- Normal HTML Tags 
	- [Li](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) element,
	- [Ul](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul) element, 
- fastHTML component wrapped round normal html tags and pico components
	- [Titled](https://docs.fastht.ml/api/xtend.html#titled) 
	- [Card](https://docs.fastht.ml/api/xtend.html#card) 

> The more docs you read, the less fear you have to those tags and components


### Design Input to specify name for value

The key is the attr `name` (read more [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name) ) 

```python

# create a Input element, more details at 
def mk_input():
    return Input(placeholder="Add a new todo", # we input data here as the value for the title column
                           id='title', # uniquely identify this Input element
                           name='title', # providing name for the value we input above in the placeholder, to create a pair (name:value). For our database, the value we input should belong to the column 'title'. details at 
                           hx_swap_oob='true') 
```

### Design Form to guide data sending and receiving 

- `Form(Group(mk_input(), Button('Add')))`: 
	- Create a Form and group the input and a button inside
- `hx_post='/'`: 
	- Inside the Form, as a attr of Form, we specify to send the input data to the post function (the func is associated with the root page), when the button is clicked and when we are at the root page
- `target_id='todo-list'`: 
	- But we don't want the response of `post` to be received by the Form itself, instead we want the element with id 'todo-list' to receive it
- `hx_swap='beforeend'`: 
	- To be more specific, the response should be located at the end of the element with id 'todo-list'.

```python

@rt('/')
def get():
    frm = Form(Group(mk_input(), Button("Add")), 
               hx_post='/', 
               target_id='todo-list', 
               hx_swap='beforeend') 
    
    return Titled('Todos', 
                  Card(
                      Ul(*todos(), id='todo-list'), 
                      header=frm) 
    )
```

### Design `post` to process submitted data and decide what to return


```python
@rt('/')
def post(todo:Todo): # the todo from Input is sent to the server
	return (todos.insert(todo), # the todo is inserted into the table
			mk_input()) # both the newly added todo and a new Input are returned as response to ...
```


### Design `get` to present the Form and Todos on front page

```python
frm = Form(Group(mk_input(),
                    Button("Add")),
               hx_post='/', 
               target_id='todo-list',
               hx_swap='beforeend') 

out = Titled('Todos', # create a title named 'Todos'
	  Card( # create a Card to organize Form as header and todos as main content
		  Ul(*todos(), id='todo-list'), 
		  header=frm) 
        )
out # actually has two components, only show the FT format
title, card = out
title # show html format
card
show(out) # show it in actual html component
```

### Design how each todo should look

```python


def render(todo):
    tid = f'todo-{todo.id}'
    delete = A('Delete',
                hx_delete=f'/delete/{todo.id}',
                hx_swap='outerHTML',
                target_id=tid) 
    toggle = A('Toggle', 
               hx_get=f'/toggle/{todo.id}',
               target_id=tid)
    return Li(toggle, delete,
              todo.title + (' ✅' if todo.done else ''),
              id=tid)
```


### 

```python

@rt('/delete/{tid}') 
def delete(tid:int): todos.delete(tid) 

@rt('/toggle/{tid}') 
def get(tid:int): 
    todo = todos[tid] 
    todo.done = not todo.done
    todos.update(todo)
    return todo 

```
# 00 Imports
### all modules needed


```python
from fasthtml.common import *
from pprint import pprint
from starlette.testclient import TestClient
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

# 01 fast_app to initialize the app

### source: how to
## what fast_app offers us

- app: a server everything we need for a web app
- rt: a router to manage the routes or paths to different pages in the app
- todos: a database for the app
- Todo: a data class for the todos

## what parameters for

- fast_app: a function to initialize a web app by giving us all the above
- 'todos1.db': specify the database file name
- `live=True`: specify if the app is live mode or not
- `id=int`, `title=str`, `done=bool` `pk='id'` are custom kwargs to specify the data types for each column of the database
    - `id`, `title`, `done` are the columns of the database, 
    - and `id` is the primary key to uniquely identify each row


```python
from fasthtml.common import *
from pprint import pprint
from starlette.testclient import TestClient
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')


```

# 01.1 `.` `tab` `cmd + click` 
### inspection
### `.` + tab to see what inside
### `cmd + click` to see the source code


```python

# app.
# todos.
# Todo.

```

# 02 TestClient, hxhdr
### inspection
### show the response without lengthy header


```python
from fasthtml.common import *
from pprint import pprint
from starlette.testclient import TestClient
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    return 'Hello World'

hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
# pprint(cli.get('/').text) # same to what displayed in the browser
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser
```

    'Hello World'


# 03 add initial data to database

### data
### delete data rows
### insert data rows
### display data rows


```python
from fasthtml.common import *
from pprint import pprint
from starlette.testclient import TestClient
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

app, rt, todos, Todo = fast_app('data/todos.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

pprint(Todo(id=0, title='new todo', done=False))

# delete all rows
for i, row in enumerate(todos.rows):
    todos.delete(row['id'])

# initialize with 3 rows
todos.insert(title='First todo', done=True)
todos.insert(title='Second todo')
todos.insert(title='Third todo', done=True)

# print all rows
for i, row in enumerate(todos.rows):
    print(f"Row {i}: {row}")
    # todos.get(row['id'])



```

    Items(id=0, title='new todo', done=False)





    <Table items (id, title, done)>






    <Table items (id, title, done)>






    <Table items (id, title, done)>






    <Table items (id, title, done)>






    Items(id=1, title='First todo', done=1)






    Items(id=2, title='Second todo', done=None)






    Items(id=3, title='Third todo', done=1)



    Row 0: {'id': 1, 'title': 'First todo', 'done': 1}
    Row 1: {'id': 2, 'title': 'Second todo', 'done': None}
    Row 2: {'id': 3, 'title': 'Third todo', 'done': 1}


# 04 `@rt('/') def get(): return text`
### show the home page
### just return a plain text


```python
from fasthtml.common import *
from pprint import pprint
from starlette.testclient import TestClient
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    return 'Hello World'


cli = TestClient(app)
pprint(cli.get('/').text)
# serve()
```

    'Hello World'


# 05 `@rt('/') def get()` return UI

### UI 
### display a compound element


```python
from fasthtml.common import *
from pprint import pprint
from starlette.testclient import TestClient
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                 Form(Group(
                     Input(
                            placeholder='type your todo', 
                            name='title', 
                            id='todo-input'), 
                     Button('Add')))
                 )
    return out


cli = TestClient(app)
hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser
# pprint(cli.get('/').text) # same to what displayed in the browser

# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <form enctype="multipart/form-data">\n'
     '    <fieldset role="group">\n'
     '      <input placeholder="type your todo" name="title" id="todo-input">\n'
     '      <button>Add</button>\n'
     '    </fieldset>\n'
     '  </form>\n'
     '</main>\n')


# 05.1: Titled, Title, Main, H1

### source: how to
### Titled: combine Title, Main, H1

```python
@delegates(ft_hx, keep=True)
def Titled(title:str="FastHTML app", *args, **kwargs)->FT:
    "An HTML partial containing a `Title`, and `H1`, and any provided children"
    return Title(title), Main(H1(title), *args, cls="container", **kwargs)
```

The `Title` and `Main` functions in this code are used to create HTML `<title>` and `<main>` elements respectively.

- `Title(title)`: This creates an HTML `<title>` element. The `<title>` tag is used in HTML to specify the title of the webpage. This title is displayed in the title bar or tab of a web browser. It's also used as the title in bookmarks and in search engine results. In this function, the `title` argument is used as the content of the `<title>` tag.

- `Main(H1(title), *args, cls="container", **kwargs)`: This creates an HTML `<main>` element. The `<main>` tag is used to wrap the main content of the body of a document or an application. The content inside the `<main>` tag should be unique to the document, excluding content that is repeated across a set of documents such as site navigation links, header or footer information. In this function, the `H1(title)` creates an `<h1>` element with the title as its content, and this `<h1>` element is included as a child of the `<main>` element. The `cls="container"` sets the class of the `<main>` element to 'container', and `*args` and `**kwargs` allow additional child elements and attributes to be added to the `<main>` element.


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos")
    return out


hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser

# serve()
```

    '<title>Todos</title>\n\n<main class="container">\n  <h1>Todos</h1>\n</main>\n'


# 05.2: Input

### source: how to
### most common attrs: what they do
### default values for the attrs

The `Input` function in this context is likely used to create an HTML `<input>` element. The `<input>` element is one of the most fundamental forms of interaction on the web, allowing users to enter data.

Here are some of the most commonly used attributes for the `<input>` element:

- `type`: This attribute specifies the type of input element to display. The available types include `text` (for text input), `password` (for password input), `checkbox` (for a checkbox), `radio` (for a radio button), `submit` (for a submit button), and many others.

- `name`: This attribute is used to reference the form data after a form is submitted.

- `value`: This attribute specifies the initial value for the input field. It can be changed by the user.

- `placeholder`: This attribute provides a hint that describes the expected value of an input field. It disappears when the user starts typing in the field.

- `required`: This boolean attribute specifies that an input field must be filled out before the user can submit the form.

- `disabled`: This boolean attribute indicates that the input field is disabled and cannot be interacted with.

Here's an example of how you might use the `Input` function to create a text input field with a placeholder:



The `Input` function in this context is likely a wrapper around the HTML `<input>` element. The attributes and their default values can vary depending on the implementation of the `Input` function. However, if we consider the standard HTML `<input>` element, here are some of the most commonly used attributes and their default values:

- `type`: Specifies the type of input control to display. The default value is "text".
- `name`: Specifies the name for the input control. There is no default value.
- `value`: Specifies the initial value for the input control. There is no default value.
- `placeholder`: Provides a hint that describes the expected value of an input field. There is no default value.
- `required`: If present, specifies that an input field must be filled out before the user can submit the form. The default is false (attribute not present).
- `disabled`: If present, specifies that the input field should be disabled. The default is false (attribute not present).
- `readonly`: If present, specifies that the input field is read-only. The default is false (attribute not present).
- `maxlength`: Specifies the maximum number of characters allowed in the input field. There is no default value.
- `min` and `max`: Specifies the minimum and maximum values for an input field. These are only applicable for `number`, `range`, `date`, `datetime-local`, `month`, `time` and `week` input types. There are no default values.
- `autocomplete`: Specifies whether an input field should have autocomplete enabled. The default is "on".
- `autofocus`: If present, specifies that the input field should automatically get focus when the page loads. The default is false (attribute not present).

Please note that not all of these attributes are applicable to every input type. The specific attributes that are applicable depend on the `type` attribute.


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                     Input(
                         placeholder='type your todo', 
                         name='title', 
                         id='todo-input'),
    ) 
                #      Button('Add')))
                #  )
    return out


hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser

# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <input placeholder="type your todo" name="title" id="todo-input">\n'
     '</main>\n')


#### 05.3: Button


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                     Input(placeholder='type your todo', name='title', id='todo-input'),
                     Button('Add'))
                #  )
    return out


hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser

# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <input placeholder="type your todo" name="title" id="todo-input">\n'
     '  <button>Add</button>\n'
     '</main>\n')


#### 05.4: Group


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                     Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add'))
                 )
    return out

hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser

# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <fieldset role="group">\n'
     '    <input placeholder="type your todo" name="title" id="todo-input">\n'
     '    <button>Add</button>\n'
     '  </fieldset>\n'
     '</main>\n')


#### 05.5: Ul


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                     Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                    Ul(*todos())
                 )
    return out

hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser

# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <fieldset role="group">\n'
     '    <input placeholder="type your todo" name="title" id="todo-input">\n'
     '    <button>Add</button>\n'
     '  </fieldset>\n'
     '  <ul>\n'
     "Items(id=1, title='First todo', done=1)\n"
     "Items(id=2, title='Second todo', done=None)\n"
     "Items(id=3, title='Third todo', done=1)\n"
     '  </ul>\n'
     '</main>\n')


#### 05.6: Li


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                     Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                    Ul(Li(t) for t in todos())
                 )
    return out


hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser
# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <fieldset role="group">\n'
     '    <input placeholder="type your todo" name="title" id="todo-input">\n'
     '    <button>Add</button>\n'
     '  </fieldset>\n'
     '  <ul>\n'
     "    <li>Items(id=1, title='First todo', done=1)</li>\n"
     "    <li>Items(id=2, title='Second todo', done=None)</li>\n"
     "    <li>Items(id=3, title='Third todo', done=1)</li>\n"
     '  </ul>\n'
     '</main>\n')


#### But why nothing happens when typing inside Input?

#### 05.7: Form

##### Because Input collect, Form send data

The `<input>` tag in HTML is used to collect user inputs. However, without a surrounding `<form>` tag, the data entered into the `<input>` field will not be sent anywhere when the user presses enter or clicks a submit button.

The `<form>` tag is necessary because it provides the URL (in the `action` attribute) where the form data should be sent, and the method (`GET` or `POST`) of how to send the data.

When a form is submitted using the `GET` method, the form data is appended to the URL in the address bar, which is why you see `http://localhost:5001/?title=this+is`.

Without a `<form>` tag, the browser has no instructions on where to send the data or how to append it to the URL, so you just see `http://localhost:5001/` in the address bar.





##### **Form: `enctype`, `method`**

- `enctype = 'multipart/form-data'`: to work with `<input>` with default `type=file`.

- `method=GET` is default [method](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method) 


#### 05.8 How `GET` and `POST` differ

When you submit a form in a web page, the form data can be sent to the server either via the URL (known as a GET request) or in the body of the HTTP request (known as a POST request).

If the form's method is GET, the form data is encoded in the URL, typically after a ?. For example, http://localhost:5001/?title=this+is. This is useful for non-sensitive data and when you want the results to be bookmarkable or shareable.

If the form's method is POST, the form data is included in the body of the HTTP request, not in the URL. This is useful for sensitive data like passwords, or for large amounts of data.


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add'))),
                    Ul(Li(t) for t in todos())
                 )
    return out


hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
pprint(cli.get('/', **hxhdr).text) 


# serve() # type into the input and enter to see the url change
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <form enctype="multipart/form-data">\n'
     '    <fieldset role="group">\n'
     '      <input placeholder="type your todo" name="title" id="todo-input">\n'
     '      <button>Add</button>\n'
     '    </fieldset>\n'
     '  </form>\n'
     '  <ul>\n'
     "    <li>Items(id=1, title='First todo', done=1)</li>\n"
     "    <li>Items(id=2, title='Second todo', done=None)</li>\n"
     "    <li>Items(id=3, title='Third todo', done=1)</li>\n"
     '  </ul>\n'
     '</main>\n')


# How to pass data from Form to Server

#### hx_post vs hx_get

- Don't worry about `method='POST'` or `method='GET'` in Form, not used here
- only consider `hx_post` or `hx_get` in Form, which is used to send data to the server
- as this is single page app, we won't go to other path or page, so we can choose a arbitrary path for `hx_get`, such as `hx_get('/tryInputData')`
- so does `hx_post`, such as `hx_post('/tryInputData')`
- only `hx_post` can receive data from Form, not `hx_get`

##### 06 `hx_get`: only get response from server

- it has nothing to do with sending data from Form to server


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                        hx_get='/getInputData', # when Form is triggered, the browser will send a GET request to the server with the url '/getInputData'
                        ),
                    Ul(Li(t) for t in todos())
                 )
    return out

@rt('/getInputData') # at page /getInputData, there is a web page with 'Hello World' as the content
def get(): # usually no parameter for get
    return 'Hello World' # server pass this response as the content of the Form
                         # data through Form can't get here



hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
pprint(cli.get('/getInputData', **hxhdr).text) 


# serve() # no typed input displayed on the url bar
```

    'Hello World'



```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                        hx_get='/getInputData'),
                    Ul(Li(t) for t in todos())
                 )
    return out


@rt('/getInputData')
def get(todo:Todo): # no error if you add a parameter here
                    # because we give it a type Todo, the todo is an empty Todo object
                    # but it will always be an empty Todo object
                    # data from Input or Form can't get here
    return todo

hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
pprint(cli.get('/getInputData', **hxhdr).text) 


# serve()
```

    'Items(id=None, title=None, done=None)'


##### 07 `hx_post`: pass data from Form to server



```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                        hx_post='/getInputData'),
                    Ul(Li(t) for t in todos())
                 )
    return out

@rt('/getInputData')
def post(todo:Todo):
    return todo # the todos is not updated with the new todo, only pass it as the content of the Form

hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
pprint(cli.post('/getInputData', data={'id':0, 'title':'me', 'done':0}, **hxhdr).text) 



# serve()
```

    "Items(id=0, title='me', done=0)"



```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                        hx_post='/getInputData'),
                    Ul(Li(t) for t in todos())
                 )
    return out

@rt('/getInputData')
def post(todo:Todo):
    return todos.insert(todo) # add new todo from Form to the database, and return the new todo with a new id from the database

hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
pprint(cli.post('/getInputData', data={'id':0, 'title':'me', 'done':0}, **hxhdr).text) 


# serve()
```

    "Items(id=0, title='me', done=0)"


# How to pass the todo elsewhere than the Form?

#### 08 `target_id` and `hx_swap`

- `target_id`: specify which element we shall pass the response to
- `hx_swap`: specify where exactly to put in relation to the element



#### 08.1 all possible values for `hx_swap`

- innerHTML - Replace the inner html of the target element
- outerHTML - Replace the entire target element with the response
- textContent - Replace the text content of the target element, without parsing the response as HTML
- beforebegin - Insert the response before the target element
- afterbegin - Insert the response before the first child of the target element
- beforeend - Insert the response after the last child of the target element
- afterend - Insert the response after the target element
- delete - Deletes the target element regardless of the response
- none- Does not append content from response (out of band items will still be processed).

#### 08.2 default `hx-swap='innerHTML'`


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                        hx_post='/getInputData',
                        target_id='todo-list'),# give the response to one with the id
                        # see the cell output below: target_id is hx_target
                        # by default, the response replace the content of the element.
                        # in other words, hx_swap='innerHTML'
                    Ul(*[Li(t) for t in todos()],
                        id='todo-list') # the one with the id 'todo-list' is Ul
                 )
    return out

@rt('/getInputData')
def post(todo:Todo):
    return todos.insert(todo) 

hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'id':0, 'title':'me', 'done':0}, **hxhdr).text) 
pprint(cli.get('/', **hxhdr).text)


# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <form enctype="multipart/form-data" hx-post="/getInputData" '
     'hx-target="#todo-list">\n'
     '    <fieldset role="group">\n'
     '      <input placeholder="type your todo" name="title" id="todo-input">\n'
     '      <button>Add</button>\n'
     '    </fieldset>\n'
     '  </form>\n'
     '  <ul id="todo-list">\n'
     "    <li>Items(id=0, title='me', done=0)</li>\n"
     "    <li>Items(id=1, title='First todo', done=1)</li>\n"
     "    <li>Items(id=2, title='Second todo', done=None)</li>\n"
     "    <li>Items(id=3, title='Third todo', done=1)</li>\n"
     '  </ul>\n'
     '</main>\n')


#### 08.3 `hx-swap='beforeend'`


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='todo-input'),
                        Button('Add')),
                        hx_post='/getInputData',
                        target_id='todo-list',
                        hx_swap='beforeend'),# beforeend - Insert the response after the last child of the target element
                    Ul(*[Li(t) for t in todos()],
                        id='todo-list') # next step: to give the new todo or every todo a better look
                 )
    return out

@rt('/getInputData')
def post(todo:Todo):
    return todos.insert(todo) 

hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'id':0, 'title':'me', 'done':0}, **hxhdr).text) 
pprint(cli.get('/', **hxhdr).text)


# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <form enctype="multipart/form-data" hx-post="/getInputData" '
     'hx-swap="beforeend" hx-target="#todo-list">\n'
     '    <fieldset role="group">\n'
     '      <input placeholder="type your todo" name="title" id="todo-input">\n'
     '      <button>Add</button>\n'
     '    </fieldset>\n'
     '  </form>\n'
     '  <ul id="todo-list">\n'
     "    <li>Items(id=0, title='me', done=0)</li>\n"
     "    <li>Items(id=1, title='First todo', done=1)</li>\n"
     "    <li>Items(id=2, title='Second todo', done=None)</li>\n"
     "    <li>Items(id=3, title='Third todo', done=1)</li>\n"
     "    <li>Items(id=4, title='this is one for all', done=None)</li>\n"
     '  </ul>\n'
     '</main>\n')



```python
for i, row in enumerate(todos.rows):
    print(f"Row {i}: {row}")
```

    Row 0: {'id': 0, 'title': 'me', 'done': 0}
    Row 1: {'id': 1, 'title': 'First todo', 'done': 1}
    Row 2: {'id': 2, 'title': 'Second todo', 'done': None}
    Row 3: {'id': 3, 'title': 'Third todo', 'done': 1}
    Row 4: {'id': 4, 'title': 'this is one for all', 'done': None}


##### [clean the data](#03-add-initial-data-for-database)

# How to clear Input or Form after submitting?



#### 08.1 `hx_swap_oob` 

**use case**

- when returning multiple elements as a response from the server to the `target_id` element, 
- and want the second element to be swapped as a replacement for the element (or elements both `Input` and `Button` in the example below) with the same `id`, and will not end up in the target.


htmx [reference](https://htmx.org/attributes/hx-swap-oob/)

- `id` and `hx_swap_oob` together to clear the input after submitting
- together the response will be swapped in as a replacement for the element with the id, and will not end up in the target.
- if the value is true or outerHTML (which are equivalent) the element will be swapped inline.


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', 
                              id='input', # id is for hx-swap-oob
                              hx_swap_oob="true"), # going to where the id is, not to the target_id
                        Button('Add', 
                                id='input', # going to antoher element with the same id
                                hx_swap_oob="true")), 
                        hx_post='/getInputData',
                        target_id='todo-list',
                        hx_swap='beforeend'),
                    Ul(*[Li(t) for t in todos()],
                        id='todo-list') 
                 )
    return out

@rt('/getInputData')
def post(todo:Todo):
    return (
            Input(placeholder='I am reborn', name='title', 
                  id='input', # id is for hx-swap-oob
                  hx_swap_oob="true"), # going to where the input is, not to the target_id 
            todos.insert(todo)) # no matter the order of the elements to be returned

hxhdr = {'headers':{'hx-request':"1"}} 
cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'id':0, 'title':'me', 'done':0}, **hxhdr).text) 
pprint(cli.get('/', **hxhdr).text)


# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <form enctype="multipart/form-data" hx-post="/getInputData" '
     'hx-swap="beforeend" hx-target="#todo-list">\n'
     '    <fieldset role="group">\n'
     '      <input placeholder="type your todo" name="title" hx-swap-oob="true" '
     'id="input">\n'
     '      <button hx-swap-oob="true" id="input" name="input">Add</button>\n'
     '    </fieldset>\n'
     '  </form>\n'
     '  <ul id="todo-list">\n'
     "    <li>Items(id=0, title='me', done=0)</li>\n"
     "    <li>Items(id=1, title='First todo', done=1)</li>\n"
     "    <li>Items(id=2, title='Second todo', done=None)</li>\n"
     "    <li>Items(id=3, title='Third todo', done=1)</li>\n"
     "    <li>Items(id=4, title='this is one for all', done=None)</li>\n"
     '  </ul>\n'
     '</main>\n')


# Why `name='input` is auto added to `Button` when set `id='input'`?

- basically, fastHTML make it a auto process: when `id` is set, `name` is set to the same value
- But when it is used for `Button`, nothing really matters. 
- It is actually designed to use for `Input` where `name` is to pair with value to send data to server, 
- but `Button` can't provide value for that purpose.

# How to make each todo look pretty?

# rending each todo

# origin of render function

### render

- basically, we define render function to render each Todo class object. 
- we pass such render function to fast_app code below
```python
def fast_app(...):

    ...

    db = database(db_file)
    if not tbls: tbls={}
    if kwargs:
        if isinstance(first(kwargs.values()), dict): tbls = kwargs
        else:
            kwargs['render'] = render
            tbls['items'] = kwargs
    dbtbls = [get_tbl(db.t, k, v) for k,v in tbls.items()]
```

- then `render` is passed to `get_tbl` function as below

```python
def get_tbl(dt, nm, schema):
    render = schema.pop('render', None)
    tbl = dt[nm]
    if tbl not in dt: tbl.create(**schema)
    else: tbl.create(**schema, transform=True)
    dc = tbl.dataclass()
    if render: dc.__ft__ = render
    return tbl,dc
```

`tbl.dataclass()`

- Purpose: The dataclass() method automatically generates a Python dataclass based on the *schema* of the table. This dataclass includes attributes corresponding to the table's columns.
- Functionality: The dataclass allows you to instantiate objects that represent rows in the database table. These objects can be easily manipulated in Python and then saved back to the database.

`dc.__ft__ = render`

- Purpose: The assignment dc.__ft__ = render attaches the custom render function to the generated dataclass.
- Functionality: When instances of this dataclass are converted into FastHTML components (likely when rendering HTML), the render function is used. This enables customized, user-defined HTML rendering of each table row based on its data.

# 09 render function


```python
def render(todo):
    return todo

render(todos.get(1))

def render(todo):
    return Li(todo.title + (' ✅' if todo.done else ''))

render(todos.get(1))
```




    Items(id=1, title='First todo', done=1)






```html
<li>First todo ✅</li>

```




```python
from fasthtml.common import *

def render(todo): # it is added to Todo class and auto render every instance of Todo
    return Li(todo.title + (' ✅' if todo.done else ''))

app, rt, todos, Todo = fast_app('todos1.db', live=True, render=render,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='user-input', hx_swap_oob="true"),
                        Button('Add')),
                        hx_post='/getInputData',
                        target_id='todo-list',
                        hx_swap='beforeend'),
                    # Ul(*[Li(t) for t in todos()], # each todo is already rendered as a Li
                    Ul(*todos(), # now todos() is a generator of multiple todo which auto renders as Li already
                        id='todo-list') 
                    )
                 
    return out

@rt('/getInputData')
def post(todo:Todo):
    return (todos.insert(todo), 
            Input(placeholder='add a todo here', name='title', id='user-input', hx_swap_oob="true"))

cli = TestClient(app)
hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser


# serve()
```

    ('<title>Todos</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Todos</h1>\n'
     '  <form enctype="multipart/form-data" hx-post="/getInputData" '
     'hx-swap="beforeend" hx-target="#todo-list">\n'
     '    <fieldset role="group">\n'
     '      <input placeholder="type your todo" name="title" hx-swap-oob="true" '
     'id="user-input">\n'
     '      <button>Add</button>\n'
     '    </fieldset>\n'
     '  </form>\n'
     '  <ul id="todo-list">\n'
     '    <li>me</li>\n'
     '    <li>First todo ✅</li>\n'
     '    <li>Second todo</li>\n'
     '    <li>Third todo ✅</li>\n'
     '    <li>this is one for all</li>\n'
     '    <li>this is her</li>\n'
     '    <li>this is me again</li>\n'
     '    <li></li>\n'
     '    <li></li>\n'
     '  </ul>\n'
     '</main>\n')


# Add toggle link to each todo

#### 10.1 What does the todo with a link look like?


```python
def render(todo):
    return Li(A('toggle'), todo.title + (' ✅' if todo.done else ''))

render(todos.get(1))
show(render(todos.get(1)))
```




```html
<li>
  <a href="#">toggle</a>
First todo ✅
</li>

```






<li>
  <a href="#">toggle</a>
First todo ✅
</li>





```python
from fasthtml.common import *

def render(todo): # it is added to Todo class and auto render every instance of Todo
    return Li(A('toggle'), todo.title + (' ✅' if todo.done else ''))

app, rt, todos, Todo = fast_app('todos1.db', live=True, render=render,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='user-input', hx_swap_oob="true"),
                        Button('Add')),
                        hx_post='/getInputData',
                        target_id='todo-list',
                        hx_swap='beforeend'),
                    # Ul(*[Li(t) for t in todos()], # each todo is already rendered as a Li
                    Ul(*todos(), # now todos() is a generator of multiple todo which auto renders as Li already
                        id='todo-list') 
                    )
                 
    return out

@rt('/getInputData')
def post(todo:Todo):
    return (todos.insert(todo), 
            Input(placeholder='add a todo here', name='title', id='user-input', hx_swap_oob="true"))

cli = TestClient(app)
hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/', **hxhdr).text) # same to what displayed in the browser


# serve()
```

# click the toggle link to change done  status

#### what make the A tag suitable for all todos?

- `hx_get=f'/todo-{todo.id}'`: an unique path using its id for each todo
- `target_id=f'todo-{todo.id}`: give response to the todo with its unique id
- `hx_swap='outerHTML'`: replace the entire todo with the response

#### How to give each todo a unique url to call the same function?

- `hx_get=f'/todo-{todo.id}'`: an unique path using its id for each todo
- `@rt('/todo-{todoId}')`: a route to handle the unique path

The `f'/todo-{todoId}'` syntax is used for string formatting in Python, where `todoId` is a variable that has a value. It's used when you want to include the value of `todoId` in the string.

However, in the route decorator `@rt('/todo-{todoId}')`, `todoId` is not a variable with a value. Instead, it's a placeholder in the URL pattern that will be replaced by the actual value when a request is made.

When you define a route like `@rt('/todo-{todoId}')`, you're telling the web framework to match any URL that follows the pattern `/todo-<some value>`, and to pass that `<some value>` as an argument to the associated function (`get` in this case).

So, you don't use `f'/todo-{todoId}'` because you're not trying to include the value of `todoId` in the string. Instead, you're defining a URL pattern with a placeholder that will be filled in with the actual value when a request is made.

#### 10.2 toggle the done status


```python
from fasthtml.common import *

def render(todo): # it is added to Todo class and auto render every instance of Todo

    return Li(A('toggle', 
                hx_get=f'/todo-{todo.id}', # give each todo a unique url for toggling
                target_id=f'todo-{todo.id}', # give the response to one with the id
                hx_swap='outerHTML'), # replace the whole element with the response
              todo.title + (' ✅' if todo.done else ''),
              id=f'todo-{todo.id}') # give each todo a unique id

app, rt, todos, Todo = fast_app('todos1.db', live=True, render=render,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/todo-{todoId}') # why not use f'/todo-{todoId}'? how does it know todoId?
def get(todoId:int):
    todo = todos.get(todoId)
    todo.done = not todo.done
    return todos.update(todo)


@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='user-input', hx_swap_oob="true"),
                        Button('Add')),
                        hx_post='/getInputData',
                        target_id='todo-list',
                        hx_swap='beforeend'),
                    # Ul(*[Li(t) for t in todos()], # each todo is already rendered as a Li
                    Ul(*todos(), # now todos() is a generator of multiple todo which auto renders as Li already
                        id='todo-list') 
                    )
                 
    return out

@rt('/getInputData')
def post(todo:Todo):
    return (todos.insert(todo), 
            Input(placeholder='add a todo here', name='title', id='user-input', hx_swap_oob="true"))

cli = TestClient(app)
hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/todo-1', **hxhdr).text) # same to what displayed in the browser


# serve()
```

    ('<li id="todo-1">\n'
     '  <a href="#" hx-get="/todo-1" hx-swap="outerHTML" '
     'hx-target="#todo-1">toggle</a>\n'
     'First todo\n'
     '</li>\n')


# add a delete link to each todo

- add a simple link with 'delete' first
- `hx_delete` to delete the todo with a unique url


```python
from fasthtml.common import *

def render(todo): # it is added to Todo class and auto render every instance of Todo

    return Li(A('toggle', 
                hx_get=f'/todo-{todo.id}',
                target_id=f'todo-{todo.id}', 
                hx_swap='outerHTML'), 

              A('delete',
                hx_delete=f'/todo-{todo.id}', # give each todo a unique url for deleting
                target_id=f'todo-{todo.id}', # give response to the A tag but the Li element
                hx_swap='outerHTML', # replace the whole element with the response
                
                ),

              todo.title + (' ✅' if todo.done else ''),

              id=f'todo-{todo.id}') 

app, rt, todos, Todo = fast_app('todos1.db', live=True, render=render,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt('/todo-{todoId}')
def delete(todoId:int):
    todos.delete(todoId)
    # return # no return is needed

@rt('/todo-{todoId}') 
def get(todoId:int):
    todo = todos.get(todoId)
    todo.done = not todo.done
    return todos.update(todo)


@rt('/')
def get():
    out = Titled("Todos",
                    Form(Group(
                        Input(placeholder='type your todo', name='title', id='user-input', hx_swap_oob="true"),
                        Button('Add')),
                        hx_post='/getInputData',
                        target_id='todo-list',
                        hx_swap='beforeend'),
                    # Ul(*[Li(t) for t in todos()], # each todo is already rendered as a Li
                    Ul(*todos(), # now todos() is a generator of multiple todo which auto renders as Li already
                        id='todo-list') 
                    )
                 
    return out

@rt('/getInputData')
def post(todo:Todo):
    return (todos.insert(todo), 
            Input(placeholder='add a todo here', name='title', id='user-input', hx_swap_oob="true"))

cli = TestClient(app)
hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
pprint(cli.get('/todo-1', **hxhdr).text) # same to what displayed in the browser


# serve()
```

#  =========

# Create a html page


```python
from fasthtml.common import *

page = Html(
    Head(Title('Some page')),
    Body(
        Div('Some text, ', 
            A('A link', href='https://example.com'), 
            Img(src="https://placehold.co/200"), 
            cls='myclass')))

pprint(page) # page: is about FT
print("====================")
print(to_xml(page)) # xml format
print("====================")
show(page) # actual html page
```

    ['html',
     (['head', (['title', ('Some page',), {}],), {}],
      ['body',
       (['div',
         ('Some text, ',
          ['a', ('A link',), {'href': 'https://example.com'}],
          ['img', (), {'src': 'https://placehold.co/200'}]),
         {'class': 'myclass'}],),
       {}]),
     {}]
    ====================
    <html>
      <head>
        <title>Some page</title>
      </head>
      <body>
        <div class="myclass">
    Some text, 
          <a href="https://example.com">A link</a>
          <img src="https://placehold.co/200">
        </div>
      </body>
    </html>
    
    ====================



<html>
  <head>
    <title>Some page</title>
  </head>
  <body>
    <div class="myclass">
Some text, 
      <a href="https://example.com">A link</a>
      <img src="https://placehold.co/200">
    </div>
  </body>
</html>




```python
app = FastHTML()

@app.get("/")
def home():
    return Div(
                H1('Hello, World'), 
                P('Some text'), 
                P('Some more text'))


hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
client = TestClient(app)
pprint(client.get("/", **hxhdr).text)
```

    ('<div>\n'
     '  <h1>Hello, World</h1>\n'
     '  <p>Some text</p>\n'
     '  <p>Some more text</p>\n'
     '</div>\n')


# Style with `Main` and `cls="container"`

In HTML, the `<main>` tag is used to wrap the main content of the body of a document or an application. The content inside the `<main>` tag should be unique to the document, excluding content that is repeated across a set of documents such as site navigation links, header or footer information.

When the statement says "we put all of our content inside a `<main>` tag with a class of `container`", it means that all the primary content of the webpage is wrapped inside a `<main>` tag. The `class="container"` attribute is used to apply specific CSS styling to this `<main>` element.

In many CSS frameworks like Bootstrap or PicoCSS, the `container` class is used to center the content and handle the layout in a certain way, often providing a responsive design. The exact styling applied by the `container` class can vary depending on the CSS rules defined in the linked stylesheets.

In the provided Python code, `Main(H1('Hello, World'), cls="container")` is creating a `<main>` HTML element with the class `container`, and inside this `<main>` element, it's placing an `<h1>` element with the text 'Hello, World'.


```python
from fasthtml.common import *

css = Style(':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css)) # custom styling to override the pico defaults

@app.route("/")
def get():
    op1 = Title("Hello World"), Main(H1('Hello, World'), cls="container") 
    op2  = Titled('Hello World') #exactly the same as above, and no need to worry about cls="container"
    return op2

# hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
# client = TestClient(app)
# pprint(client.get("/", **hxhdr).text)

serve()
```

    ('<title>Hello World</title>\n'
     '\n'
     '<main class="container">\n'
     '  <h1>Hello, World</h1>\n'
     '</main>\n')


# Form send data without htmx

## use`action='/'`, `method='POST'` for Form


# How to multi-page app


```python
from fasthtml.common import *

app = FastHTML()
messages = ["This is a message, which will get rendered as a paragraph"]

@app.get("/")
def home():
    return Main(H1('Messages'), 
                *[P(msg) for msg in messages], # spread the list of messages as P elements
                A("Link to Page 2 (to add messages)", 
                  href="/page2")) # go to a new page

@app.get("/page2")
def page2():
    return Main(P("Add a message with the form below:"),
                Form(Input(type="text", 
                           name="data"), # create a (name:value) pair, which is "data":<input>
                     Button("Submit"),
                     action="/", method="post"))

@app.post("/")
def add_message(data:str): # here we can access the data from the form
    messages.append(data)
    return home()

serve()
```


# `hx_target='#count'` is the same  `target_id='count'`

# `global`: how use `count` across all pages


```python
from fasthtml.common import *

app = FastHTML()

count = 0

@app.get("/")
def home():
    return Title("Count Demo"), Main(
        H1("Count Demo"),
        P(f"Count is set to {count}", id="count"),
        Button("Increment", 
            #    hx_get="/increment", 
               hx_post="/increment",
            #    hx_target="#count", 
               target_id="count",
               hx_swap="innerHTML")
    )

# @app.get("/increment")
@app.post("/increment")
def increment():
    print("incrementing") # debug print into the terminal
    global count # access the global variable count
    count += 1
    return f"Count is set to {count}" # return it as the content of the P with id "count"

# serve()
```

# create empty database and empty table


```python
from fasthtml.common import *
db = database('data/todos.db') # empty database
todos = db.t.items # empty table

pprint(f'db.t = {db.t}')
pprint(db.t.items)
pprint(todos)

```

    'db.t = '
    <Table items (does not exist yet)>
    <Table items (does not exist yet)>


# Fill empty table with column names and types


```python
if todos not in db.t: todos.create(id=int, title=str, done=bool, pk='id')

pprint(f'db.t = {db.t}')
pprint(db.t.items)
pprint(todos)
pprint(db.tables[0])
```

    'db.t = items'
    <Table items (id, title, done)>
    <Table items (id, title, done)>
    <Table items (id, title, done)>


# Add data to the table and list all rows


```python
# add rows to the table
todos.insert(title='A todo', done=False)
todos.insert(title='Another one', done=True)

todos() # list all rows of the table
```




    {'id': 1, 'title': 'A todo', 'done': 0}






    {'id': 2, 'title': 'Another one', 'done': 1}






    [{'id': 1, 'title': 'A todo', 'done': 0},
     {'id': 2, 'title': 'Another one', 'done': 1}]



# Create a class for the table row


```python
Todo = todos.dataclass()
Todo(title='From a dataclass', done=False)
todos.insert(Todo(title='From a dataclass', done=False)) # id auto added and done to 0 or 1 not true or false
```




    Items(id=None, title='From a dataclass', done=False)






    Items(id=3, title='From a dataclass', done=0)



# all rows into unordered list


```python
[Li(f'{o.title} {"✅" if o.done else ""}') for o in todos()[:1]]
[Li(f'{o.title} {"✅" if o.done else ""}') for o in todos()] # can't be rendered into html, but just FT objects or lists
```




    [['li', ('A todo ',), {}]]






    [['li', ('A todo ',), {}],
     ['li', ('Another one ✅',), {}],
     ['li', ('From a dataclass ',), {}]]




```python
todolist = Ul(*[Li(f'{o.title} {"✅" if o.done else ""}') for o in todos()])
todolist # rendered into html literal
```




```html
<ul>
  <li>A todo </li>
  <li>Another one ✅</li>
  <li>From a dataclass </li>
</ul>

```



# style notebook with pico


```python
show(picocondlink)
```




<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.conditional.min.css">

<style>:root { --pico-font-size: 100%; }</style>




```python xtend.py
picocss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"
picolink = (Link(rel="stylesheet", href=picocss),
            Style(":root { --pico-font-size: 100%; }"))
picocondcss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.conditional.min.css"
picocondlink = (Link(rel="stylesheet", href=picocondcss),
                Style(":root { --pico-font-size: 100%; }"))
```


```python
set_pico_cls() # apply pico to notebook cells
```




    <IPython.core.display.Javascript object>



```python xtend.py
def set_pico_cls():
    js = """var sel = '.cell-output, .output_area';
document.querySelectorAll(sel).forEach(e => e.classList.add('pico'));

new MutationObserver(ms => {
  ms.forEach(m => {
    m.addedNodes.forEach(n => {
      if (n.nodeType === 1) {
        var nc = n.classList;
        if (nc && (nc.contains('cell-output') || nc.contains('output_area'))) nc.add('pico');
        n.querySelectorAll(sel).forEach(e => e.classList.add('pico'));
      }
    });
  });
}).observe(document.body, { childList: true, subtree: true });"""
    return display.Javascript(js)
```


```python
Card(todolist, header="head", footer="foot")
show(Card(todolist, header="head", footer="foot"))
```




```html
<article>
  <header>head</header>
  <ul>
    <li>A todo </li>
    <li>Another one ✅</li>
    <li>From a dataclass </li>
  </ul>
  <footer>foot</footer>
</article>

```






<article>
  <header>head</header>
  <ul>
    <li>A todo </li>
    <li>Another one ✅</li>
    <li>From a dataclass </li>
  </ul>
  <footer>foot</footer>
</article>





```python
frm = Form(Group(Input(id="title"), Button("Save")),
           Checkbox(id="done", label='Done'))
frm
```




```html
<form enctype="multipart/form-data">
  <fieldset role="group">
    <input id="title" name="title">
    <button>Save</button>
  </fieldset>
  <label>
    <input type="checkbox" value="1" id="done" name="done">
Done
  </label>
</form>

```




```python
show(frm)
```




<form enctype="multipart/form-data">
  <fieldset role="group">
    <input id="title" name="title">
    <button>Save</button>
  </fieldset>
  <label>
    <input type="checkbox" value="1" id="done" name="done">
Done
  </label>
</form>




# Page vs Titled, multi-page with htmx


```python
from fasthtml.common import *

app,rt = fast_app()


@rt("/")
def get():
    contents = Div(
        A('Link', hx_get='/page'),
    )
    return Page('Home', contents) # Page is very similar to Titled, get many attrs get up.

@rt("/page")
def get():
    contents = Div(
        A('Home', hx_get='/'),
    )
    return Page('Page', contents)


serve()
```

# tut simple  ===================

### multi-page, htmx, database


```python
from fasthtml.fastapp import *

app,rt, todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')


@rt("/")
def get():
    todo_list = [
        Li(
            A(todo.title, 
              hx_get=f'/todos/{todo.id}'),
            (' (done)' if todo.done else ''),
            id=f'todo-{todo.id}'
        ) for todo in todos()
    ]
    card = Card(
                Ul(*todo_list, id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Page('Todo list', card) # force to create a new page

@rt("/todos/{id}")
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Back', hx_get='/')
    )
    return Page('Todo details', contents) # force to create a new page

serve()
```

### add Form to post data


```python
from fasthtml.fastapp import *

app,rt, todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')

def TodoRow(todo): # it's like a render function
    return Li(
        A(todo.title, 
          hx_get=f'/todos/{todo.id}'),
        (' (done)' if todo.done else ''),
        id=f'todo-{todo.id}' # give each todo a unique id
    )


def home():
    add = Form(
            Group(
                Input(name="title", 
                      placeholder="New Todo"),
                Button("Add")
            ), 
            hx_post="/"
        )
    card = Card(
                Ul(*map(TodoRow, todos()), # actually rendering all todos
                   id='todo-list'),
                header=add, # put the form in the header of the Card
                footer=Div(id='current-todo') # empty div as the footer
            )
    return Page('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home() # this is bad, to update the home page is a waste of resources; of course, the only good thing is that Input is also refreshed.

@rt("/todos/{id}")
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Back', hx_get='/')
    )
    return Page('Todo details', contents) # return a new page, also kind of waste

serve()
```

# `name:value` pair & `hx_delete` in Button


```python
from fasthtml.fastapp import *

app,rt,todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')


def TodoRow(todo): # rendering the todo as a Li
    return Li(
        A(todo.title, hx_get=f'/todos/{todo.id}'),
        (' (done)' if todo.done else '') + ' | ',
        A('edit',     
          hx_get=f'/edit/{todo.id}'), # click to run the edit page
        id=f'todo-{todo.id}'
    )


@rt("/todos/{id}") # run the edit page for the todo with the id
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Delete', 
               hx_delete='/', # click the button to delete the todo
               value=id,  # create a hidden input with the value of the id
               name="id"), # give the hidden input a name
        Button('Back', hx_get='/') # click the button to go back the home page
    )
    return Page('Todo details', contents)

@rt("/")
def delete(id:int): 
    todos.delete(id)
    return home()

def home():
    add = Form(
            Group(
                Input(name="title", placeholder="New Todo"),
                Button("Add")
            ), hx_post="/"
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Page('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home()

@rt("/edit/{id}")
def get(id:int):
    res = Form(
            Group(
                Input(id="title"),
                Button("Save")
            ),
            Hidden(id="id"),
            Checkbox(id="done", label='Done'),
            Button('Back', 
                   hx_get='/'), # click the button to return the home page
            hx_put="/",  # click edit to update the todo and return the home page
            id="edit"
        )
    frm = fill_form(res, todos[id])
    return Page('Edit Todo', frm)

@rt("/")
def put(todo: Todo):
    todos.update(todo)
    return home()


serve()
```

# `name:value` pair & `hx_get='/delete'` in Button


```python
from fasthtml.fastapp import *

app,rt,todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')


def TodoRow(todo): # rendering the todo as a Li
    return Li(
        A(todo.title, 
          hx_get=f'/todos/{todo.id}'),

        (' (done)' if todo.done else '') + ' | ',

        A('edit',     
          hx_get=f'/edit/{todo.id}'), 

        id=f'todo-{todo.id}'
    )


@rt("/todos/{id}") 
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Delete', 
               hx_get='/delete', # click the button to delete the todo
                                 # hx_get='/' won't work
                                 # probably because there will be two get function under '/' route
               value=id, 
               name="id"), 
        Button('Back', hx_get='/') 
    )
    return Page('Todo details', contents) 

@rt("/delete")
def get(id:int): 
    todos.delete(id)
    return home()

def home():
    add = Form(
            Group(
                Input(name="title", placeholder="New Todo"),
                Button("Add")
            ), hx_post="/"
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Page('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home()





@rt("/edit/{id}")
def get(id:int):
    res = Form(
            Group(
                Input(id="title"),
                Button("Save")
            ),
            Hidden(id="id"),
            Checkbox(id="done", label='Done'),
            Button('Back', 
                   hx_get='/'), # click the button to return the home page
            hx_put="/",  # click edit to update the todo and return the home page
            id="edit"
        )
    frm = fill_form(res, todos[id])
    return Page('Edit Todo', frm)

@rt("/")
def put(todo: Todo):
    todos.update(todo)
    return home()


serve()
```

# how htmx make multi-page app easy

- `Main(..., hx_swap_oob='true', id='main')` is the key


```python 
@delegates(ft_hx, keep=True)
def Titled(title:str="FastHTML app", *args, **kwargs)->FT:
    "An HTML partial containing a `Title`, and `H1`, and any provided children"
    return Title(title), Main(H1(title), *args, cls="container", **kwargs)

def Page(title, *con): return Title(title), ContainerX(H1(title), *con)
def ContainerX(*cs, **kwargs): return Main(*cs, **kwargs, cls='container', hx_push_url='true', hx_swap_oob='true', id='main')
```




```python
from fasthtml.fastapp import *

# experiment the Page setting
def Page(title, *con): return Title(title), ContainerX(H1(title), *con)
def ContainerX(*cs, **kwargs): return Main(*cs, **kwargs, cls='container', 
                                           hx_push_url='true', 
                                           hx_swap_oob='true', 
                                           id='main')



app,rt,todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')


def TodoRow(todo): # rendering the todo as a Li
    return Li(
        A(todo.title, 
          hx_get=f'/todos/{todo.id}'),

        (' (done)' if todo.done else '') + ' | ',

        A('edit',     
          hx_get=f'/edit/{todo.id}'), 

        id=f'todo-{todo.id}'
    )


@rt("/todos/{id}") 
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Delete', 
               hx_get='/delete', 
                                 
                                 
               value=id, 
               name="id"), 
        Button('Back', hx_get='/') 
    )
    return Titled('Todo details', Main(contents, 
                                       cls="container",
                                       hx_push_url="true", 
                                       hx_swap_oob="true", # same in Page's Main
                                       id='main')) # same in Page's Main
            # so this response is not to replace the A tag, but to the whole page

@rt("/delete")
def get(id:int): 
    todos.delete(id)
    return home()

def home():
    add = Form(
            Group(
                Input(name="title", placeholder="New Todo"),
                Button("Add")
            ), hx_post="/"
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Page('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home()


@rt("/edit/{id}")
def get(id:int):
    res = Form(
            Group(
                Input(id="title"),
                Button("Save")
            ),
            Hidden(id="id"),
            Checkbox(id="done", label='Done'),
            Button('Back', 
                   hx_get='/'), # click the button to return the home page
            hx_put="/",  # click edit to update the todo and return the home page
            id="edit"
        )
    frm = fill_form(res, todos[id])
    return Page('Edit Todo', frm)

@rt("/")
def put(todo: Todo):
    todos.update(todo)
    return home()


serve()
```

#  add url history and push the url
- `hx_push_url="true"` is the key


```python
from fasthtml.fastapp import *

# experiment the Page setting
def Page(title, *con): return Title(title), ContainerX(H1(title), *con)
def ContainerX(*cs, **kwargs): return Main(*cs, **kwargs, cls='container', 
                                           hx_push_url='true', 
                                           hx_swap_oob='true', 
                                           id='main')



app,rt,todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')


def TodoRow(todo): # rendering the todo as a Li
    return Li(
        A(todo.title, 
          hx_get=f'/todos/{todo.id}'),

        (' (done)' if todo.done else '') + ' | ',

        A('edit',     
          hx_get=f'/edit/{todo.id}'), 

        id=f'todo-{todo.id}'
    )


@rt("/todos/{id}") 
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Delete', 
               hx_get='/delete', 
               value=id, 
               name="id"), 
        Button('Back', hx_get='/') 
    )
    return Titled('Todo details', Main(contents, 
                                       cls="container", # get the css right with main and cls
                                       hx_push_url="true", # add url history and push the url
                                       hx_swap_oob="true", 
                                       id='main')) 

@rt("/delete")
def get(id:int): 
    todos.delete(id)
    return home()

def home():
    add = Form(
            Group(
                Input(name="title", placeholder="New Todo"),
                Button("Add")
            ), hx_post="/"
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Page('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home()


@rt("/edit/{id}")
def get(id:int):
    res = Form(
            Group(
                Input(id="title"),
                Button("Save")
            ),
            Hidden(id="id"),
            Checkbox(id="done", label='Done'),
            Button('Back', 
                   hx_get='/'), # click the button to return the home page
            hx_put="/",  # click edit to update the todo and return the home page
            id="edit"
        )
    frm = fill_form(res, todos[id])
    return Page('Edit Todo', frm)

@rt("/")
def put(todo: Todo):
    todos.update(todo)
    return home()


serve()
```

# `fill_form`: fill a form with given data 

### Form and htmx: use along with `hx_put`
### `fill_form`: help to fill in the form before update with new info

```python
def fill_form(form:FT, obj)->FT:
    "Fills named items in `form` using attributes in `obj`"
    if is_dataclass(obj): obj = asdict(obj)
    elif not isinstance(obj,dict): obj = obj.__dict__
    return _fill_item(form, obj)

def _fill_item(item, obj):
    if not isinstance(item,FT): return item
    tag,cs,attr = item.list
    if isinstance(cs,tuple): cs = tuple(_fill_item(o, obj) for o in cs)
    name = attr.get('name', None)
    val = None if name is None else obj.get(name, None)
    if val is not None and not 'skip' in attr:
        if tag=='input':
            if attr.get('type', '') in ('checkbox','radio'):
                if val: attr['checked'] = '1'
                else: attr.pop('checked', '')
            else: attr['value'] = val
        if tag=='textarea': cs=(val,)
        if tag == 'select':
            option = next((o for o in cs if o.tag=='option' and o.get('value')==val), None)
            if option: option.selected = '1'
    return FT(tag,cs,attr,void_=item.void_)    

```

The `fill_form` function is designed to populate a form with data from a given object. Here's a high-level overview of what it does:

1. It takes two arguments: `form` and `obj`. `form` is expected to be a form template, and `obj` is an object that contains the data to fill the form.

2. If `obj` is a dataclass, it's converted to a dictionary using the `asdict` function. If `obj` is not a dictionary, it's converted to a dictionary using its `__dict__` attribute. This is done to ensure that the data can be accessed using dictionary syntax.

3. The function then calls the `_fill_item` helper function on the form and the object. This function is responsible for actually filling the form with data.

4. The `_fill_item` function iterates over each item in the form. If the item has a 'name' attribute that matches a key in the `obj` dictionary, the function updates the item with the corresponding value from `obj`.

5. The way the item is updated depends on the type of the item. For example, if the item is an 'input' element of type 'checkbox' or 'radio', the 'checked' attribute is set based on the value from `obj`. If the item is a 'textarea' element, its content is set to the value from `obj`. If the item is a 'select' element, the 'selected' attribute of the matching 'option' element is set.

6. The function returns the filled form.

In summary, `fill_form` is a function that populates a form with data from a given object. It's a way of automating the process of filling out a form based on data that you already have.




```python
from fasthtml.fastapp import *

# experiment the Page setting
def Page(title, *con): return Title(title), ContainerX(H1(title), *con)
def ContainerX(*cs, **kwargs): return Main(*cs, **kwargs, cls='container', 
                                           hx_push_url='true', 
                                           hx_swap_oob='true', 
                                           id='main')



app,rt,todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')


def TodoRow(todo): # rendering the todo as a Li
    return Li(
        A(todo.title, 
          hx_get=f'/todos/{todo.id}'),

        (' (done)' if todo.done else '') + ' | ',

        A('edit',     
          hx_get=f'/edit/{todo.id}'), 

        id=f'todo-{todo.id}'
    )


@rt("/todos/{id}") 
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Delete', 
               hx_get='/delete', 
               value=id, 
               name="id"), 
        Button('Back', hx_get='/') 
    )
    return Titled('Todo details', Main(contents, 
                                       cls="container", # get the css right with main and cls
                                       hx_push_url="true", # add url history and push the url
                                       hx_swap_oob="true", 
                                       id='main')) 

@rt("/delete")
def get(id:int): 
    todos.delete(id)
    return home()

def home():
    add = Form(
            Group(
                Input(name="title", # name is for the form data
                      placeholder="New Todo"), # value is the user input data for Input bar
                Button("Add")
            ), 
            hx_post="/" # post form data to server
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Page('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home()


@rt("/edit/{id}")
def get(id:int):
    res = Form(
            Group(
                Input(id="title",
                      name="title", # name is for the form data
                      ),
                Button("Save")
            ),
            Hidden(id="id"), # to fill in the id of the todo ========================
            Checkbox(id="done", label='Done'),
            Button('Back', 
                   hx_get='/'), # click the button to return the home page
            hx_put="/",  # click to update the todo from Input for title, Hidden for id, Checkbox for done
            id="edit"
        )
    frm = fill_form(res, todos[id]) # fill the form with the todo data
    return Page('Edit Todo', frm)

@rt("/")
def put(todo: Todo):
    todos.update(todo)
    return home()


serve()
```

# `hx_put` must work with Form with value and name

### htmx
### hx_put: when and how to use

`hx_post`: Used for creating new resources; no need for value as new data is entered by the user.

`hx_put`: Used for updating existing resources; requires value to pre-fill the form with existing data



# when to use `value` and `checked` for `CheckBox` 
- we use `value` to passes the value to the server but not to display 
- we use `checked` to display the value of the checkbox 


```python
from fasthtml.fastapp import *

# experiment the Page setting
def Page(title, *con): return Title(title), ContainerX(H1(title), *con)
def ContainerX(*cs, **kwargs): return Main(*cs, **kwargs, cls='container', 
                                           hx_push_url='true', 
                                           hx_swap_oob='true', 
                                           id='main')



app,rt,todos,Todo = fast_app('data/todos.db', id=int, title=str, done=bool, pk='id')


def TodoRow(todo): # rendering the todo as a Li
    return Li(
        A(todo.title, 
          hx_get=f'/todos/{todo.id}'),

        (' (done)' if todo.done else '') + ' | ',

        A('edit',     
          hx_get=f'/edit/{todo.id}'), 

        id=f'todo-{todo.id}'
    )


@rt("/todos/{id}") 
def get(id:int):
    contents = Div(
        Div(todos[id].title),
        Button('Delete', 
               hx_get='/delete', 
               value=id, 
               name="id"), 
        Button('Back', hx_get='/') 
    )
    return Titled('Todo details', Main(contents, 
                                       cls="container", 
                                       hx_push_url="true", 
                                       hx_swap_oob="true", 
                                       id='main')) 

@rt("/delete")
def get(id:int): 
    todos.delete(id)
    return home()

def home():
    add = Form(
            Group(
                Input(name="title", 
                      placeholder="New Todo"), 
                Button("Add")
            ), 
            hx_post="/" 
        )
    card = Card(
                Ul(*map(TodoRow, todos()), id='todo-list'),
                header=add,
                footer=Div(id='current-todo')
            )
    return Page('Todo list', card)

@rt("/")
def get(): return home()

@rt("/")
def post(todo:Todo):
    todos.insert(todo)
    return home()


@rt("/edit/{id}")
def get(id:int):
    res = Form(
            Group(
                Input(id="title",
                      name="title", # name is for the form data
                      value=todos[id].title, # value must be added
                      ),
                Button("Save")
            ),
            Hidden(id="id",
                   value=id), # must add the value of the id
            Checkbox(id="done", 
                     value=todos[id].done, # it passes the value but not to display ########
                     checked=todos[id].done, # to display the value of the checkbox ########
                     label='Done'),
            Button('Back', 
                   hx_get='/'), 
            hx_put="/",  
            id="edit"
        )
    # frm = fill_form(res, todos[id]) 
    return Page('Edit Todo', res)

@rt("/")
def put(todo: Todo):
    todos.update(todo)
    return home()


serve()
```

# ========= fasthtml tut fancy =========

# Title, Main to form a page


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True,      
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

@rt("/")
def get():
  todolist = Ul(*[Li(f'{o.title} {"✅" if o.done else ""}') for o in todos()])
  contents = Main(H1("Hello World!"), todolist)
  return Title("FastHTML"), contents # a page need: a title and a main ==================

serve()
```

# build Card in steps

### UI design
### Input, Button => Group => Form => Header => Card
### Div => Footer => Card
### Head, Card => Main => Titled


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('todos1.db', live=True, 
                                hdrs=(picolink), # add header links for css as a tuple =====
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')


@rt("/")
def get():
  todolist = [Li(f'{o.title} {"✅" if o.done else ""}') for o in todos()]
  todoul = Ul(*todolist, id="todolist")

  group = Group(Input(placeholder="New Todo", 
                      name="title"), # as just name, so use for hx_post
                Button("Add"))
  
  header = Form(group, 
                hx_post="/", 
                target_id="details") # use Form to post data (todo.title) and give response to footer


  footer = Div("Todo details", id="details")

  card = Card(todoul, header=header, footer=footer) # build card step by step

  contents = Main(H1("Hello World!"), card, cls="container")
  return Title("FastHTML"), contents

@rt("/")
def post(todo:Todo):
  todo = todos.insert(todo)
  return todo.title

serve()

# serve()
```

# AX

### source: how to

```python
@delegates(ft_hx, keep=True)
def A(*c, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs)->FT:
    "An A tag; `href` defaults to '#' for more concise use with HTMX"
    return ft_hx('a', *c, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

@delegates(ft_hx, keep=True)
def AX(txt, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs)->FT:
    "An A tag with just one text child, allowing hx_get, target_id, and hx_swap to be positional params"
    return ft_hx('a', txt, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)
```


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('data/todos.db', live=True, 
                                hdrs=(picolink), 
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

def render_todo(todo:Todo):
   done = "✅" if todo.done else ""
   link2 = AX(todo.title, 
            hx_get=f'/todo/{todo.id}', 
            target_id='details')
   link = A(todo.title, 
            hx_get=f'/todo/{todo.id}', 
            target_id='details')
   return Li(link, done, id=f'todo-{todo.id}') # test AX and A

@rt("/")
def get():
  todolist = Ul(*map(render_todo, todos()), id="todolist")
  group = Group(Input(placeholder="New Todo", name="title"), Button("Add"))
  header = Form(group, 
                hx_post="/", 
                target_id="todolist", # give response to todolist
                hx_swap="beforeend") # put it at the last of the todolist
  footer = Div(id="details")
  card = Card(todolist, header=header, footer=footer)
  contents = Main(H1("Hello World!"), card, cls="container")
  return Title("FastHTML"), contents

@rt("/")
def post(todo:Todo): return render_todo(todos.insert(todo)) 

@rt("/todo/{id}")
def delete(id:int):
   todos.delete(id)
   return ('',  
           Div(hx_swap_oob='innerHTML', id='details')) 

@rt("/todo/{id}")
def get(id:int):
  todo = todos[id]
  btn = Button('Delete', 
                hx_delete=f'/todo/{id}', 
                target_id=f'todo-{id}',
                hx_swap="delete") 
  return P(todo.title), btn

serve()
```

# hx_swap_oob='innerHTML' vs 'true'

### htxm [reference](https://htmx.org/attributes/hx-swap-oob/)
### `hx-swap-oob='true'` is the same as `hx-swap-oob='outerHTML'`: to swap the target element with the response element which share the same id
### `hx-swap-oob='innerHTML'` is to only swap the innerHTML of the target element with content from the response element


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('data/todos.db', live=True, 
                                hdrs=(picolink), 
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

def render_todo(todo:Todo):  # rendering each todo =================
   done = "✅" if todo.done else ""
   link2 = AX(todo.title, 
            hx_get=f'/todo/{todo.id}',
            target_id='details') 
   link = A(todo.title, 
            hx_get=f'/todo/{todo.id}', 
            target_id='details')
   return Li(link, done, id=f'todo-{todo.id}')

@rt("/") # render the home page =================
def get():
  todolist = Ul(*map(render_todo, todos()), id="todolist")
  group = Group(Input(placeholder="New Todo", name="title"), Button("Add"))
  header = Form(group, 
                hx_post="/", 
                target_id="todolist", 
                hx_swap="beforeend") 
  
  footer = (Div(id="details"), # element to be swapped by hx_swap_oob ✨✨✨
            A('I am a link inside footer', id='details'))

  card = Card(todolist, header=header, footer=footer)
  contents = Main(H1("Hello World!"), card, cls="container")
  return Title("FastHTML"), contents

@rt("/") # post data to server =================
def post(todo:Todo): return render_todo(todos.insert(todo)) # return a rendered todo


@rt("/todo/{id}") # render when a todo is clicked =================
def get(id:int):
  todo = todos[id]
  btn = Button('Delete', 
                hx_delete=f'/todo/{id}', # the delete action at the url (where) 🕯️🕯️🕯️
                target_id=f'todo-{id}', # send teh delete response to the todo Li (whom)🕯️🕯️🕯️
                hx_swap="outerHTML") # replace the todo Li with the response (how)🕯️🕯️🕯️
                
  return P(todo.title), btn


@rt("/todo/{id}") # render when a todo is deleted =================
def delete(id:int):
   todos.delete(id)
   return ('',  # replace the entire todo Li with nothing 🕯️🕯️🕯️
           Div( # ✨✨✨ swap itself with the element share the same id ✨✨✨
              hx_swap_oob='innerHTML', # ✨✨✨ swap between content of two elements which share the same id, the content here is nothing ============
            #   hx_swap_oob='true', # to swap elements  ============= ✨✨✨
              id='details')) # make sure they share the same id ✨✨✨

serve()
```

# hx_swap='delete' vs 'outerHTML'

### htxm [reference](https://htmx.org/attributes/hx-swap/)
### `hx-swap='delete'` is to delete the target element regardless of the response
### `hx-swap='outerHTML'` is to replace the entire target element with the response


```python
from fasthtml.common import *

app, rt, todos, Todo = fast_app('data/todos.db', live=True, 
                                hdrs=(picolink), 
                                id=int,
                                title=str,
                                done=bool,
                                pk='id')

def render_todo(todo:Todo):
   done = "✅" if todo.done else ""
   link2 = AX(todo.title, 
            hx_get=f'/todo/{todo.id}', 
            target_id='details') 
   link = A(todo.title, 
            hx_get=f'/todo/{todo.id}', 
            target_id='details')
   return Li(link, done, id=f'todo-{todo.id}')

@rt("/")
def get():
  todolist = Ul(*map(render_todo, todos()), id="todolist")
  group = Group(Input(placeholder="New Todo", name="title"), Button("Add"))
  header = Form(group, 
                hx_post="/", 
                target_id="todolist", 
                hx_swap="beforeend") 
  footer = Div(id="details")
  card = Card(todolist, header=header, footer=footer)
  contents = Main(H1("Hello World!"), card, cls="container")
  return Title("FastHTML"), contents

@rt("/")
def post(todo:Todo): return render_todo(todos.insert(todo)) 

@rt("/todo/{id}")
def delete(id:int):
   todos.delete(id)
   return ('',  
           Div(
              hx_swap_oob='innerHTML', 
            
              id='details')) 

@rt("/todo/{id}")
def get(id:int):
  todo = todos[id]
  btn = Button('Delete', 
                hx_delete=f'/todo/{id}', 
                target_id=f'todo-{id}', # give response "" to the content of todo Li
                hx_swap="outerHTML") # make sure to remove the Li entirely 
                # hx_swap="delete") # delete - Deletes the target element regardless of the response ===========
  return P(todo.title), btn

serve()
```

# ===========================

# fasthtml examples 01_todo_app

### [code source](https://github.com/AnswerDotAI/fasthtml-example/blob/main/01_todo_app/main.py)

# add Style inside fast_app

### Style the web
### hrds defined as tuple but provided as a list below, why?

- tuple is immutable, but list is mutable


```python
from fasthtml.common import *

app,rt,todos,Todo = fast_app(
    'data/todos.db',
    hdrs=[Style(':root { --pico-font-size: 100%; }')], # style ==================
    id=int, title=str, done=bool, pk='id')

id_curr = 'current-todo'
def tid(id): return f'todo-{id}'

@patch
def __ft__(self:Todo):
    show = AX(self.title, f'/todos/{self.id}', id_curr)
    edit = AX('edit',     f'/edit/{self.id}' , id_curr)
    dt = ' ✅' if self.done else ''
    return Li(show, dt, ' | ', edit, id=tid(self.id))

def mk_input(**kw): return Input(id="new-title", name="title", placeholder="New Todo", required=True, **kw)

@rt("/")
async def get():
    add = Form(Group(mk_input(), Button("Add")),
               hx_post="/", target_id='todo-list', hx_swap="beforeend")
    card = Card(Ul(*todos(), id='todo-list'),
                header=add, footer=Div(id=id_curr)),
    title = 'Todo list'
    return Title(title), Main(H1(title), card, cls='container')

@rt("/todos/{id}")
async def delete(id:int):
    todos.delete(id)
    return clear(id_curr)

@rt("/")
async def post(todo:Todo): return todos.insert(todo), mk_input(hx_swap_oob='true')

@rt("/edit/{id}")
async def get(id:int):
    res = Form(Group(Input(id="title"), Button("Save")),
        Hidden(id="id"), CheckboxX(id="done", label='Done'),
        hx_put="/", target_id=tid(id), id="edit")
    return fill_form(res, todos.get(id))

@rt("/")
async def put(todo: Todo): return todos.upsert(todo), clear(id_curr)

@rt("/todos/{id}")
async def get(id:int):
    todo = todos.get(id)
    btn = Button('delete', hx_delete=f'/todos/{todo.id}',
                 target_id=tid(todo.id), hx_swap="outerHTML")
    return Div(Div(todo.title), btn)

# serve()
```

# Create database and class in fast_app

### database
### create a database with multiple table
### create a class for the table

```python
app,rt,todos,Todo = fast_app( # how todos and Todo is made behind the scene ==================
    'data/todos.db',
    hdrs=[Style(':root { --pico-font-size: 100%; }')], 
    id=int, title=str, done=bool, pk='id')

```


```python
from fasthtml.common import *

app = FastHTML(hdrs=[Style(':root { --pico-font-size: 100%; }')]) # create an app
rt = app.route # create a route decorator

# remove the data/todosNotebook.db file if it exists
if os.path.exists('data/todosNotebook.db'): os.remove('data/todosNotebook.db')

db = database('data/todosNotebook.db') # create an empty database
print('db = ', db) # print the database
print('db.t = ', db.t) # print the tables in the database

if 'todos' not in db.t:  # create a table if it doesn't exist
    print('creating table todos: ')
    db.t['todos1'].create(id=int, title=str, done=bool, pk='id') # create a table named todos
    db.t['todos2'].create(id=int, title=str, done=bool, pk='id') # create a table named todos

print('db.t = ', db.t) # print the tables in the table
print("db.t['todos2'] = ", db.t['todos2']) # print the table itself
print("todos = ", todos) # print the table itself
print('todos.c = ', todos.c)
Todo = db.t['Todo'].dataclass()
print('Todo = ', Todo)
```

    db =  <Database <sqlite3.Connection object at 0x105f25240>>
    db.t =  
    creating table todos: 





    <Table todos1 (id, title, done)>






    <Table todos2 (id, title, done)>



    db.t =  todos1, todos2
    db.t['todos2'] =  "todos2"
    todos =  "items"
    todos.c =  done, id, title
    Todo =  <class 'types.Todo'>


# define `__ft__` to render Todo
### Render
### use `__ft__`, we can define it as we go along




```python
from fasthtml.common import *

app,rt,todos,Todo = fast_app(
    'data/todos.db',
    # render=renderFunc,
    hdrs=[Style(':root { --pico-font-size: 100%; }')], 
    id=int, title=str, done=bool, pk='id')

id_curr = 'current-todo'
def tid(id): return f'todo-{id}'

@patch
def __ft__(self:Todo): # render the Todo object is to define __ft__ method ==================
    show = AX(self.title, f'/todos/{self.id}', id_curr)
    edit = AX('edit',     f'/edit/{self.id}' , id_curr)
    dt = ' ✅' if self.done else ''
    return Li(show, dt, ' | ', edit, id=tid(self.id))

def renderFunc(todo:Todo): # define render func for using inside fast_app
    show = AX(todo.title, f'/todos/{todo.id}', id_curr)
    edit = AX('edit',     f'/edit/{todo.id}' , id_curr)
    dt = ' ✅' if todo.done else ''
    return Li(show, dt, ' | ', edit, id=tid(todo.id))

def mk_input(**kw): return Input(id="new-title", name="title", placeholder="New Todo", required=True, **kw)

@rt("/")
async def get():
    add = Form(Group(mk_input(), Button("Add")),
               hx_post="/", target_id='todo-list', hx_swap="beforeend")
    card = Card(Ul(*todos(), id='todo-list'),
                header=add, footer=Div(id=id_curr)),
    title = 'Todo list'
    return Title(title), Main(H1(title), card, cls='container')

@rt("/todos/{id}")
async def delete(id:int):
    todos.delete(id)
    return clear(id_curr)

@rt("/")
async def post(todo:Todo): return todos.insert(todo), mk_input(hx_swap_oob='true')

@rt("/edit/{id}")
async def get(id:int):
    res = Form(Group(Input(id="title"), Button("Save")),
        Hidden(id="id"), CheckboxX(id="done", label='Done'),
        hx_put="/", target_id=tid(id), id="edit")
    return fill_form(res, todos.get(id))

@rt("/")
async def put(todo: Todo): return todos.upsert(todo), clear(id_curr)

@rt("/todos/{id}")
async def get(id:int):
    todo = todos.get(id)
    btn = Button('delete', hx_delete=f'/todos/{todo.id}',
                 target_id=tid(todo.id), hx_swap="outerHTML")
    return Div(Div(todo.title), btn)

# serve()
```

# use `renderFunc` vs `__ft__` disadvantages
### using `renderFunc` instead of `__ft__` directly
### we have to put `renderFunc` to the very top


```python
from fasthtml.common import *

def renderFunc(todo): # using renderFunc for fast_app must put it in the very beginning ==================
    show = AX(todo.title, f'/todos/{todo.id}', id_curr)
    edit = AX('edit',     f'/edit/{todo.id}' , id_curr)
    dt = ' ✅' if todo.done else ''
    return Li(show, dt, ' | ', edit, id=tid(todo.id))

app,rt,todos,Todo = fast_app(
    'data/todos.db',
    render=renderFunc,
    hdrs=[Style(':root { --pico-font-size: 100%; }')], 
    id=int, title=str, done=bool, pk='id')

id_curr = 'current-todo'
def tid(id): return f'todo-{id}'

# @patch
# def __ft__(self:Todo): # render the Todo object is to define __ft__ method ==================
#     show = AX(self.title, f'/todos/{self.id}', id_curr)
#     edit = AX('edit',     f'/edit/{self.id}' , id_curr)
#     dt = ' ✅' if self.done else ''
#     return Li(show, dt, ' | ', edit, id=tid(self.id))



def mk_input(**kw): return Input(id="new-title", name="title", placeholder="New Todo", required=True, **kw)

@rt("/")
async def get():
    add = Form(Group(mk_input(), Button("Add")),
               hx_post="/", target_id='todo-list', hx_swap="beforeend")
    card = Card(Ul(*todos(), id='todo-list'),
                header=add, footer=Div(id=id_curr)),
    title = 'Todo list'
    return Title(title), Main(H1(title), card, cls='container')

@rt("/todos/{id}")
async def delete(id:int):
    todos.delete(id)
    return clear(id_curr)

@rt("/")
async def post(todo:Todo): return todos.insert(todo), mk_input(hx_swap_oob='true')

@rt("/edit/{id}")
async def get(id:int):
    res = Form(Group(Input(id="title"), Button("Save")),
        Hidden(id="id"), CheckboxX(id="done", label='Done'),
        hx_put="/", target_id=tid(id), id="edit")
    return fill_form(res, todos.get(id))

@rt("/")
async def put(todo: Todo): return todos.upsert(todo), clear(id_curr)

@rt("/todos/{id}")
async def get(id:int):
    todo = todos.get(id)
    btn = Button('delete', hx_delete=f'/todos/{todo.id}',
                 target_id=tid(todo.id), hx_swap="outerHTML")
    return Div(Div(todo.title), btn)

serve()
```

# AX's keyword args used as positional args

### `hx_get` and `target_id` are used as positional args
### put a Div into the footer of Card and give it `id_curr`


```python
from fasthtml.common import *

app,rt,todos,Todo = fast_app(
    'data/todos.db',
    hdrs=[Style(':root { --pico-font-size: 100%; }')], 
    id=int, title=str, done=bool, pk='id')

id_curr = 'current-todo'
def tid(id): return f'todo-{id}'

@patch
def __ft__(self:Todo): # render the Todo object is to define __ft__ method ==================

    show = AX(self.title, f'/todos/{self.id}', id_curr) # keyword args used as positional args
    # show = AX(self.title, hx_get=f'/todos/{self.id}', target_id=id_curr)

    edit = AX('edit',     f'/edit/{self.id}' , id_curr)
    # edit = AX('edit',     hx_get=f'/edit/{self.id}', target_id=id_curr)

    dt = ' ✅' if self.done else ''
    return Li(show, dt, ' | ', edit, id=tid(self.id))



def mk_input(**kw): return Input(id="new-title", name="title", placeholder="New Todo", required=True, **kw)

@rt("/")
async def get():
    add = Form(Group(mk_input(), Button("Add")),
               hx_post="/", target_id='todo-list', hx_swap="beforeend")
    card = Card(Ul(*todos(), id='todo-list'),
                header=add, 

                footer=Div(id=id_curr)), # footer is the Div with id_curr
    title = 'Todo list'
    return Title(title), Main(H1(title), card, cls='container')

@rt("/todos/{id}")
async def delete(id:int):
    todos.delete(id)
    return clear(id_curr)

@rt("/")
async def post(todo:Todo): return todos.insert(todo), mk_input(hx_swap_oob='true')

@rt("/edit/{id}")
async def get(id:int):
    res = Form(Group(Input(id="title"), Button("Save")),
        Hidden(id="id"), CheckboxX(id="done", label='Done'),
        hx_put="/", target_id=tid(id), id="edit")
    return fill_form(res, todos.get(id))

@rt("/")
async def put(todo: Todo): return todos.upsert(todo), clear(id_curr)

@rt("/todos/{id}")
async def get(id:int):
    todo = todos.get(id)
    btn = Button('delete', hx_delete=f'/todos/{todo.id}',
                 target_id=tid(todo.id), hx_swap="outerHTML")
    return Div(Div(todo.title), btn)

serve()
```

# Project Structure

### UI design
### rendering vs actions

- rendering: create or add page or new sections with action planning embedded
- action: no page or section added, just delete or replace/swap content or elements



```python
from fasthtml.common import *

app,rt,todos,Todo = fast_app(
    'data/todos.db',
    hdrs=[Style(':root { --pico-font-size: 100%; }')], 
    id=int, title=str, done=bool, pk='id')

id_curr = 'current-todo'
def tid(id): return f'todo-{id}'

@patch
def __ft__(self:Todo): # rendering each todo ==================

    show = AX(self.title, 
            # show action planning =====================
            f'/todos/{self.id}',  # click the link to talk with server  
                                # get request with a unique url (path itself is arbitrary)
            id_curr)  # give response to the footer div with id_curr
    # show = AX(self.title, hx_get=f'/todos/{self.id}', target_id=id_curr)

    edit = AX('edit',     
              
            # edit action planning =====================
            f'/edit/{self.id}' , # click the link to talk with server  
            id_curr) # give response to the footer div with id_curr
    # edit = AX('edit',     hx_get=f'/edit/{self.id}', target_id=id_curr)
 
    # UI design for each todo ====================
    dt = ' ✅' if self.done else ''
    return Li(show, dt, ' | ', edit, id=tid(self.id))

@rt("/todos/{id}")
async def get(id:int): # show action defined ================== or
                       # show section rendering ==================
    
    todo = todos.get(id)
    btn = Button('delete', # delete action planning ==================
                hx_delete=f'/todos/{todo.id}',
                 
                target_id=tid(todo.id), 
                hx_swap="outerHTML")
    
    return Div(Div(todo.title), btn) # UI design for show section ===========

@rt("/todos/{id}") # delete action defined ==================
async def delete(id:int):
    todos.delete(id)
    return clear(id_curr) # use empty div to swap/replace the content of current todo
                          # meaning the show section for the selected todo is cleared


def mk_input(**kw): return Input( # prepare the input bar 
                                id="new-title", 
                                name="title", 
                                placeholder="New Todo", 
                                required=True, 
                                **kw)

@rt("/")
async def get(): # rendering the home page ==================
    add = Form(Group(mk_input(), 
                     Button("Add")),

                # post action planning ==================
               hx_post="/", # pass data to server 
               target_id='todo-list', # give response to the todo-list Ul
               hx_swap="beforeend") # put the response at the end of the todo-list Ul
    
    # UI design for the home page ==================
    card = Card(Ul(*todos(), id='todo-list'), 
                header=add, 
                footer=Div(id=id_curr)), # footer is the Div with id_curr
    
    title = 'Todo list'
    return Title(title), Main(H1(title), card, cls='container') # like Titled

@rt("/") # post action defined ==================
async def post(todo:Todo): 
    return (todos.insert(todo), # return the added todo
            mk_input(hx_swap_oob='true')) # swap the input bar with a new one



@rt("/edit/{id}") # render edit UI section ==================
async def get(id:int):
    res = Form( Group(
                    Input(id="title"), 
                    Button("Save")),
                Hidden(id="id"), 
                CheckboxX(id="done", 
                          label='Done'),

                # put action planning ==================
                hx_put="/", 
                target_id=tid(id), 
                id="edit")
    return fill_form(res, todos.get(id))

@rt("/") # put action defined ==================
async def put(todo: Todo):  
    return (todos.upsert(todo), # either update or insert a todo
            clear(id_curr)) # clear the show section for the selected todo



serve()
```

# why htmx not change url in browser address bar
### htmx
### why hx_get run a request to a url without going there in browser address bar

The `hx-get` attribute in htmx allows you to make a GET request to a specified URL when a certain event occurs (like clicking a button or submitting a form). However, this does not change the URL in the browser's address bar.

This is because `hx-get` uses AJAX (Asynchronous JavaScript and XML) to make the GET request. AJAX allows a web page to update and display new data without refreshing the page. This means that the URL in the browser's address bar does not change, because the page itself is not being reloaded.

This is different from clicking a link or manually entering a URL in the address bar, which would load a new page and update the URL in the address bar. With `hx-get`, the request is made in the background, and only certain parts of the page are updated with the new data.

# hx_put to update a form

### htmx
### hx_put: when and how
### hx_post: when and how


In the context of RESTful APIs, "updating" a resource typically means modifying an existing resource, while "posting" new information usually refers to creating a new resource.

Here's a more detailed explanation:

- **POST**: This HTTP method is typically used to create a new resource on the server. For example, if you have a blog application, you might use a POST request to create a new blog post. The server would receive the POST request, create a new blog post with the data provided in the request, and then return a response indicating that the new post was created successfully.

- **PUT**: This HTTP method is typically used to update an existing resource on the server. For example, in the same blog application, you might use a PUT request to update an existing blog post. The server would receive the PUT request, find the existing blog post that matches the ID provided in the request, update that post with the new data provided in the request, and then return a response indicating that the post was updated successfully.

So, when we say "update a resource", we mean using a PUT request to modify an existing resource on the server. And when we say "post new information", we mean using a POST request to create a new resource on the server.

Yes, that's correct. When a PUT request is made to a server to update a resource, the server typically performs the following steps:

1. **Identify the Resource**: The server uses the identifier provided in the request (usually part of the URL) to find the existing resource that should be updated.

2. **Load the Resource**: The server retrieves the current state of the resource from wherever it's stored (like a database).

3. **Update the Resource**: The server updates the loaded resource with the new data provided in the PUT request. This could involve changing one or more fields of the resource.

4. **Save the Resource**: The server saves the updated resource back to the storage system, replacing the old version of the resource.

5. **Respond to the Request**: The server sends a response back to the client to indicate that the update was successful (or that an error occurred).

So, in essence, a PUT request does involve loading the current state of the resource, updating it with new information, and then saving the updated resource.


# CheckboxX

### UI design
### CheckboxX: how it is better than Checkbox


```python
@delegates(ft_hx, keep=True)
def CheckboxX(checked:bool=False, label=None, value="1", id=None, name=None, **kwargs)->FT:
    "A Checkbox optionally inside a Label, preceded by a `Hidden` with matching name"
    if id and not name: name=id
    if not checked: checked=None
    res = Input(type="checkbox", id=id, name=name, checked=checked, value=value, **kwargs)
    if label: res = Label(res, label)
    return Hidden(name=name, skip=True, value=""), res
```

The `CheckboxX` function in your code is a custom implementation of a checkbox input that provides some additional features compared to a pure HTML checkbox.

Here are the key differences:

1. **Default Value Handling**: In a pure HTML checkbox, if the checkbox is not checked when the form is submitted, no value is sent for that checkbox. This can make it difficult to determine on the server whether the checkbox was unchecked or if it was not included in the form at all. The `CheckboxX` function addresses this by including a hidden input with the same name as the checkbox. This hidden input has a default value that is sent when the form is submitted, regardless of whether the checkbox is checked. This allows the server to distinguish between an unchecked checkbox and a missing checkbox.

2. **Label Handling**: The `CheckboxX` function allows you to easily include a label with the checkbox. If a label is provided, the checkbox is wrapped in a label element. This can improve accessibility and make it easier for users to interact with the checkbox.

3. **ID and Name Handling**: The `CheckboxX` function allows you to specify an ID and a name for the checkbox. If an ID is provided but no name is, the name is set to the same value as the ID. This can make it easier to manage and reference the checkbox in your code.

4. **Additional Attributes**: The `CheckboxX` function allows you to specify additional attributes for the checkbox using the `**kwargs` argument. This makes it more flexible and customizable than a pure HTML checkbox.

In summary, `CheckboxX` provides more flexibility and better handling of default values, labels, IDs, names, and additional attributes compared to a pure HTML checkbox.

# clear

### htmx
### make easy to swap with `hx_swap_oob='innerHTML'` to clear the input
```python
def clear(id): return Div(hx_swap_oob='innerHTML', id=id)
```



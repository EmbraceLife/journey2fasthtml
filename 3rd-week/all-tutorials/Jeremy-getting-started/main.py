
from fasthtml.common import *

def render(): ...

# initialize the app
app, rt, todos, Todo = fast_app('todos.db', live=True, render=render, id=int,
                title=str,
                done=bool)

# build the root page

serve()  
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

# cli = TestClient(app)
# hxhdr = {'headers':{'hx-request':"1"}} # mock to remove the headers
# # pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
# pprint(cli.get('/todo-1', **hxhdr).text) # same to what displayed in the browser


serve()
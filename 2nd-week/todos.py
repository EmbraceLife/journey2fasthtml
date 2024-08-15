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
                              hx_swap_oob="true"), # going to where the input is, not to the target_id
                        Button('Add', id='input', # so, the input can replace button as long as it has the same id and hx-swap-oob
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
    return (todos.insert(todo),
            Input(placeholder='I am reborn', name='title', # going to replace itself which is different from target_id
                  id='input', # id is for hx-swap-oob
                  hx_swap_oob="true")) # going to where the input is, not to the target_id 

# cli = TestClient(app)
# pprint(cli.post('/getInputData', data={'title':'put in the end'}).text) 
# pprint(cli.get('/').text) # same to what displayed in the browser


serve()
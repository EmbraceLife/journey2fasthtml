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
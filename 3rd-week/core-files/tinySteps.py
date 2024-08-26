
from fasthtml.common import *

def render(subject):
    return Li(
        Group(subject.name,
        P(f"Total time: {subject.total_time} minutes")),
        id=f"subject-{subject.id}"
    )

app, rt, subjects, Subject = fast_app(
    'data/ten_thousand_hours.db',
    render=render,
    id=int,
    name=str,
    total_time=int,
    pk='id'
)

@rt("/")
def get():
    create_form = Form(
        Group(  # added Group to make it nicer
            Input(id="new-subject", name="name", placeholder="Enter a new subject"),
            Button("Create", type="submit")
            ),
        hx_post="/subjects",
        hx_target="#subjects-list",
        hx_swap="afterbegin"
    )
    subjects_list = Ul(*subjects(order_by='id DESC'), id='subjects-list')
    return Titled(
        "Ten Thousand Hours",
        P("Track your progress towards mastery"),
        Card(subjects_list, # body is positional argument
             header=create_form,
            footer=Div())
    )
    
@rt("/subjects")
def post(name: str):
    new_subject = subjects.insert(name=name, total_time=0)
    return Li(
        Group( # added Group to make it nicer
            new_subject.name,
            "   |   ",
            P(f"Total time: {new_subject.total_time} minutes"),
            Button("Start", hx_post=f"/subjects/{new_subject.id}/start", hx_swap="outerHTML")),
        id=f"subject-{new_subject.id}",
        
    )


from datetime import datetime

@rt("/subjects/{id}/start")
def post(id: int):
    subject = subjects[id]
    start_time = datetime.now().isoformat()
    
    return Li(
	    Group(
	        subject.name,
	        P(f"Total time: {subject.total_time} minutes"),
	        P("Current session: ", Span("0:00", id=f"timer-{subject.id}")),
	        Button("Stop", 
	               hx_post=f"/subjects/{subject.id}/stop",
                   hx_vals=f'{{"start_time": "{start_time}"}}',
                   target_id=f"subject-{subject.id}",
	               hx_swap="outerHTML"),
	        Script(f"""
	            var startTime = new Date("{start_time}");
	            var timerId = setInterval(function() {{
	                var now = new Date();
	                var diff = Math.floor((now - startTime) / 1000);
	                var minutes = Math.floor(diff / 60);
	                var seconds = diff % 60;
	                var display = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
	                document.getElementById("timer-{subject.id}").textContent = display;
	            }}, 1000);
	            document.getElementById("subject-{subject.id}").dataset.timerId = timerId;
	        """),
	        ),
        id=f"subject-{subject.id}",
        hx_swap_oob="true"
    )



from datetime import datetime, timedelta

@rt("/subjects/{id}/stop")
def post(id: int, start_time: str):
    subject = subjects[id]
    end_time = datetime.now()
    start_time = datetime.fromisoformat(start_time)
    duration = end_time - start_time
    minutes_spent = round(duration.total_seconds() / 60, 2)
    
    subject.total_time += minutes_spent
    subjects.update(subject)

    return Li(
        subject.name,
        P(f"Total time: {subject.total_time:.2f} minutes"),
        Button("Start", 
               hx_post=f"/subjects/{subject.id}/start",
               hx_swap="outerHTML"),
        Script(f"""
            clearInterval(document.getElementById("subject-{subject.id}").dataset.timerId);
        """),
        id=f"subject-{subject.id}"
    )


serve()
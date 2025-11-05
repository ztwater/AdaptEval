from dataclasses import dataclass
from fastapi import FastAPI, Form, Depends
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get("/form", response_class=HTMLResponse)
def form_get():
    return '''<form method="post"> 
    <input type="text" name="no" value="1"/> 
    <input type="text" name="nm" value="abcd"/> 
    <input type="submit"/> 
    </form>'''


@dataclass
class SimpleModel:
    no: int = Form(...)
    nm: str = Form(...)


@app.post("/form")
def form_post(form_data: SimpleModel = Depends()):
    return form_data


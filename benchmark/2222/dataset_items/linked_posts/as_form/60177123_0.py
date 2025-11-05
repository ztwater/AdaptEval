@app.post("/form", response_model=SimpleModel)
def form_post(no: int = Form(...),nm: str = Form(...)):
    return SimpleModel(no=no,nm=nm)

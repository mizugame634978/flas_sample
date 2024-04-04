from flaskr import app
from flask import render_template #faskrはフォルダ名

@app.route('/')
def index():
    return render_template(
        'index.html'
    )
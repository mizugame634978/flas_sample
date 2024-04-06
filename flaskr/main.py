from flaskr import app#faskrはフォルダ名
from flask import render_template ,request,redirect,url_for
import sqlite3
DATABASE = 'db.sqlite3'


@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()#listとして取得
    con.close()

    books = []
    for row in db_books:
        books.append({
                'title':row[0],
                'price':row[1],
                'arrival_day':row[2]
        })
        
    return render_template(
        'index.html',
        books = books
    )


@app.route('/form')
def form():
    return render_template(
        'form.html'
    )


@app.route('/register',methods=["POST"])
def register():
    """form.htmlからデータを受け取って、DBに本を登録
    
    """
    
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?,?,?)',
                [title,price,arrival_day])
    print("debug中")
    con.commit()
    con.close()
    return redirect(url_for('index'))
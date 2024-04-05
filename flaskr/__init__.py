from flask import Flask
app = Flask(__name__)
import flaskr.main #flaskrはフォルダ名

# dbをインポート #
from flaskr import db
db.create_books_table()
from tinydb import TinyDB

DB_PATH = 'app/templates.json'

def get_templates():
    db = TinyDB(DB_PATH)
    return db.all()

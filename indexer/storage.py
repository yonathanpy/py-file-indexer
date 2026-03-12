import sqlite3


class IndexStorage:

    def __init__(self, db_path):

        self.conn = sqlite3.connect(db_path)

        self.create_schema()

    def create_schema(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents(
            id INTEGER PRIMARY KEY,
            path TEXT,
            name TEXT,
            content TEXT
        )
        """)

        self.conn.commit()

    def add_document(self, doc):

        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO documents(path,name,content) VALUES(?,?,?)",
            (doc["path"], doc["name"], doc["content"])
        )

    def search(self, term):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT path,name FROM documents WHERE content LIKE ?",
            ("%" + term + "%",)
        )

        return cursor.fetchall()

    def commit(self):
        self.conn.commit()

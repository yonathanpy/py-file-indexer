from indexer.scanner import scan_directory
from indexer.parser import parse_file
from indexer.storage import IndexStorage


class IndexEngine:

    def __init__(self, db_path="index.db"):
        self.storage = IndexStorage(db_path)

    def index_directory(self, path):

        files = scan_directory(path)

        for file_path in files:

            data = parse_file(file_path)

            if data:
                self.storage.add_document(data)

        self.storage.commit()

    def search(self, query):

        return self.storage.search(query)

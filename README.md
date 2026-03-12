# py-file-indexer

A Python based file indexing and search engine designed for fast local document discovery.

The system scans directories, indexes file contents and metadata, and allows searching through a command line interface.

## Features

- Recursive file indexing
- SQLite storage backend
- Full text search
- Modular architecture
- Command line interface
- Extensible indexing pipeline

## Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/py-file-indexer
cd py-file-indexer
```

Install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

Index a directory.

```bash
python main.py index /path/to/folder
```

Search for content.

```bash
python main.py search keyword
```

## Architecture

```
CLI
│
Index Engine
│
Scanner → Parser → Storage
│
Search Engine
```

## Project Layout

```
indexer/
search/
cli/
utils/
```

## License

MIT License

## Author

Yonathan  
Python Developer

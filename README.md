<p align="center">
  <img src="https://cdn.jsdelivr.net/npm/simple-icons@v16/icons/python.svg" width="256" height="256" alt="Py File Indexer Logo" />
</p>

Py File Indexer is a modular file indexing and search system implemented in Python.  
The project provides a framework for recursively scanning file systems, extracting document content, and building a searchable index over file metadata and textual data.

The repository demonstrates how indexing engines organize document ingestion pipelines, storage layers, and query execution systems. The architecture separates scanning, parsing, storage, and query evaluation into independent modules.

The system is designed to resemble the internal architecture of small scale search engines and document indexing systems.

---

# System Architecture

The system is composed of multiple subsystems responsible for document ingestion, indexing, and query execution.

```
Filesystem
   │
Directory Scanner
   │
File Parser
   │
Document Index
   │
Storage Backend
   │
Search Engine
   │
Command Interface
```

Each component is designed to operate independently while communicating through well defined data structures.

---

# Core Components

## Filesystem Scanner

The scanner is responsible for discovering files within a directory hierarchy.  
It recursively traverses directory structures and collects file paths for indexing.

Responsibilities include:

- recursive directory traversal
- file discovery
- path normalization
- filesystem abstraction

The scanner produces a list of files that are passed to the parsing stage.

---

## File Parsing System

The parser extracts document content and metadata from files discovered during scanning.

Extracted attributes include:

- file path
- file name
- raw text content

The parsing module is intentionally modular so that additional parsers can be implemented for structured file formats such as JSON, CSV, or XML.

---

## Document Index

The index subsystem organizes document information in a searchable structure.

Documents inserted into the index contain:

- document identifier
- file path
- file name
- textual content

The current implementation stores documents within a persistent database while allowing simple text search operations.

---

## Storage Layer

The storage backend persists indexed documents.  
The system currently uses SQLite as the underlying storage engine.

Responsibilities include:

- document insertion
- index persistence
- query retrieval
- transaction management

Although SQLite is used by default, the architecture allows storage backends to be replaced with more scalable systems.

---

## Query Engine

The query engine performs document search operations.  
User queries are evaluated against the stored document index.

The search process includes:

1. parsing the query string
2. executing search operations on indexed content
3. retrieving matching document paths

The current implementation performs substring matching against document content.

---

## Command Interface

The command line interface provides access to indexing and search functionality.

Supported operations include:

- indexing directories
- performing keyword searches
- displaying indexed file paths

The CLI is implemented using the Click framework.

---

# Data Flow

The document ingestion pipeline follows the sequence below.

1. user requests indexing of a directory
2. scanner discovers files
3. parser extracts document content
4. storage engine records document entries
5. search engine queries stored documents

This pipeline resembles simplified search indexing workflows used in document retrieval systems.

---

# Repository Layout

```
indexer/
    engine.py
    scanner.py
    parser.py
    storage.py

search/
    query.py
    ranking.py

cli/
    commands.py

utils/
    hashing.py
    filesystem.py
```

Each module encapsulates a specific subsystem of the indexing architecture.

---

# Installation

Clone the repository.

```
git clone https://github.com/YOUR_USERNAME/py-file-indexer
cd py-file-indexer
```

Install required dependencies.

```
pip install -r requirements.txt
```

---

# Indexing Files

Index a directory using the CLI.

```
python main.py index /path/to/directory
```

This operation scans the directory and inserts discovered documents into the index database.

---

# Searching the Index

Search for files containing a specific keyword.

```
python main.py search keyword
```

The engine returns file paths of documents whose contents match the query.

---

# Design Goals

The repository demonstrates the design of a modular indexing engine with clearly separated components.

Design objectives include:

- modular indexing pipeline
- separation of scanning and parsing logic
- persistent storage abstraction
- command line driven workflow
- extensible indexing architecture

---

# Potential Extensions

The architecture allows the addition of advanced indexing features.

Possible extensions include:

- inverted index implementation
- TF-IDF ranking algorithms
- distributed indexing
- multi format document parsing
- parallel file scanning
- full text search engines
- metadata indexing

---

# License

MIT License

---

# Author

Yonathan  
aka Witwizard

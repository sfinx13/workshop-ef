# workshop-ef
Correction of the exercises proposed by an organism.

## Prerequisites
You have to install minimum Python 3.10 and related packages

## Getting started

```bash
$ python -m venv venv
$ pip install -r requirements.txt
```

## Usage

### Merge pdf
Merges two PDF documents into a single file. Each of them has a cover page that must be removed before combining the PDF documents.

```bash
$ python merge-pdf/main.py
```

### 2010 US census
Script that reads the census spreadsheet file while calculating statistics for each county.
```bash
$ python census/main.py
```

## Documentation
* https://pypdf2.readthedocs.io/en/latest/
* https://openpyxl.readthedocs.io/en/stable/

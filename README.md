# ics2mail

This short Python script reads an ICS file and creates a PDF agenda for the weekly AV meeting. Fully configurable by changing values in config.py

## Requirements

- Python 3.x
  - icalevents
- pango
  
## Installation

Setup the virtualenv (pango needs to be installed *before* this step):

```bash
virtualenv -p python3 .env && source .env/bin/activate && pip install -r requirements.txt
``` 

Or, if you're brave, just run install the requirements into your base python install:

```bash
pip install -r requirements.txt
```

Copy config.py.dist to config.py and enter the ics url into config.py.

## Usage

```bash
source .env/bin/activate && python ics2doc.py
```
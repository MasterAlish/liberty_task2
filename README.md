# Python Assignment task solution

### Requirements

python >= 3.6

`pip install -r requirements.txt`

### Run

XML Data files must be in the `ingest` directory

**Run ETL process:**

`python main.py`

**Run API for data:**

`uvicorn api.server:app`


### API Docs

Api docs are available from here http://127.0.0.1:8000/docs/

Available query parameters:

**sort_by** - Sort by some field [title, episode_title, start_of_availability]

**start_date_from**, **start_date_to**  - Filter by start_of_availability

**page**, **per_page** - Pagination. By default per_page=10
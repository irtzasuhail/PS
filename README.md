# API Code Test

## Introduction

This is the solution to the Code Test in which I was asked to parse CSV and JSON files, and create APIs to find items based on ID or the N cheapest items. To do this, I implemented a basic FLASK web app which would first parse the files, and then start the server with the information required. 

## How to

1. Download the CSV file into the same directory as the code. 
2. `cd` into the directory via the command prompt.
3. Create a venv using the instructions found [here].(https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
4. Install the FLASK framework with the command `pip install flask`
5. Start the script with the command `python main.py`

When the initial parsing of the information is complete, you will see the line `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`. This means that the server is now up and runnning. 

## URLs

### Search by ID

To search by ID. The URL is `localhost:5000/search/<id>` where `<id>` is the ID of the item you want to search for. The item's JSON object will be returned if it exists. 

### Get Cheapest

To get the N cheapest items avaiable, the url is `localhost:5000/cheapest/<count>` where `<count>` is the number of cheapest items you would like to see. A list of JSON objects will be returned with as many items as you asked for. 


## Assumptions

### Get Cheapest

- Items with no price included are ignored in this case. Only items with a price >= 0.0 will be considered. 

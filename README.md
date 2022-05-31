# NVD-API-Search
Search tool for NVD API using CVE IDs

## Usage

The code for the tool is on the file main.py.

To run your the search tool, first you'll have to fill your authentication information (API Key) in the headers{ } array.

    headers = {
        'apiKey': '###API KEY###'
    }
    
Save the file and run it with the command

> - python3 main.py

The outuput will be generated on a file with the name as <CVE-ID>.json.

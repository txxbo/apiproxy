from app import settings
import json
from xmltodict import unparse
from fastapi import Response


class Database:
    """Modify me to use your own method of data storage.
    
    This 'database' is a JSON file."""
    
    def __init__(self):
        # Load database path from settings
        self.db_path = settings.DATABASE_PATH
    
    # Write items to "database" (JSON format for this example)
    def write_items(self, data: dict) -> None:
        with open(self.db_path, "w") as f:
            f.write(json.dumps(data))
    
    # Read items and output in JSON or XML
    def read_items(self, output_type:str="JSON") -> dict:
        if output_type not in OUTPUT_TYPES:
            output_type = "JSON"

        # Find function for formatting output type
        func = OUTPUT_TYPES[output_type]       
        with open(self.db_path, "r") as f:
            # Read data and format
            data = f.read()
            return func(data)
    

def jsonify(data: str) -> dict:
    # Return JSON format
    return json.loads(data)


def xmlify(data: str) -> str:
    # Load data and transform into XML response
    data_dict = json.loads(data)
    xml_data = unparse(data_dict,  pretty=True, indent='  ')
    return Response(content=xml_data, media_type="application/xml")


# Find proper formatting funciton
OUTPUT_TYPES = {
    "JSON": jsonify,
    "XML": xmlify
}


# Create database object 
db = Database()
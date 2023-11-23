import asyncio
import xmltodict
import requests
import xml.etree.ElementTree as ET
from app.core.utility import divide_chunks
from app import logger, settings
from app.dependencies import db


async def fetch_third_party_data():
    """Continuous loop to run background tasks.
    
    Output from example get_metars() is saved to file.
    """
    while True:
        # Your code to fetch and process data
        result = get_metars(settings.STATION_IDS)
        # Do something with result - store using database from dependencies.py
        db.write_items(result)
        # Wait before refetching from API
        await asyncio.sleep(settings.BACKGROUND_TASK_INTERVAL)


def get_metars(airports:list[str], url:str=settings.BASE_URL) -> dict:
    """API call to retrieve METAR data.
    
    Args:
        airports (list[str]): List of airport station IDs
        url (str): URL to API
        
    Returns:
        dict: Dictionary holding response
    """
    # Store trees for each API call
    trees = []
    
    # Divide the airports into chunks
    chunks = divide_chunks(airports, settings.CHUNK_SIZE)

    # Send API call for each chunk of airports
    for airport_codes in chunks:
        # Create string from airport list
        stationList = ",".join(airport_codes)
        
        try:
            # Create URL and send API call
            next_url = f"{url}{stationList}"
            # Log url accessed during API call
            logger.debug(f"API URL Chunk: {next_url}")
            
            # Send API call
            response = requests.get(next_url, timeout=10)            
            if response.status_code != 200:
                # assert error or print
                return {}
            
            # Collect XML element from response
            tree = ET.fromstring(response.text)
            trees.append(tree)
                
        except Exception as e:
            logger.error(f"Failed to retrieve data: {str(e)}")
            return {}
    
    # Success
    logger.info(f"Data updated")
    
    # Nothing collected, return nothing
    if len(trees) < 1:
        return {}
    
    # Create XML root and return
    root = trees[0]
    
    # Append all data to the root XML element
    for tree in trees[1:]:
        data = root.find('./data')
        data.extend(tree.findall(".//METAR"))
    
    # Convert XML to JSON
    xml_string = ET.tostring(root, encoding='utf8')
    json_dict = xmltodict.parse(xml_string)
    
    # Return data
    return json_dict

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Background tasks repeated every x seconds
    # 15 minutes in seconds
    BACKGROUND_TASK_INTERVAL: int = 15 * 60 
    
    # Path to data folder
    DATA_PATH: str = "app/data/"
    
    # Example configuration
    BASE_URL: str = "https://aviationweather.gov/api/data/dataserver?requestType=retrieve&dataSource=metars&hoursBeforeNow=2.5&format=xml&mostRecentForEachStation=constraint&stationString="
    STATION_FILE: str = "airports"
    IGNORE_IDS: list[str] = ["NULL", "LGND"]
    STATION_IDS: list[str] = []
    CHUNK_SIZE: int = 300
    
    # Path to "database" 
    DATABASE_PATH: str = "app/data/data.json"
    
settings = Settings()

# Load data for example
with open(f"{settings.DATA_PATH}{settings.STATION_FILE}", "r") as f:
    # Load station ID list, de-duplicate and ignore as required
    settings.STATION_IDS = list(set([
        s.strip() for s in f.readlines()
        if s.strip() not in settings.IGNORE_IDS
        ]))
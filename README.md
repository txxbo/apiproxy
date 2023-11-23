# apiproxy

An API proxy. By integrating this proxy into your own server, it allows for a developer to account for changes in a third party API without forcing users to update code.

Integration with aviation weather was used to illustrate how the proxy can work. Further integrating with a proper database, schemas, and models is recommended for a larger project. 

## Execution
After building your environment and configuration, run from command line with the following:
```bash
uvicorn app:app --reload
```

## Example Proxy
- This code is setup to connect to a third party API call from Aviation Weather
- Resulting data is stored in database
- Call to this API will work as a proxy to the data retrieve from Aviation Weather
  
## Configure 
- Change background_tasks.py to collect from whichever API you choose
- Configure config.py as required
- Configure Database class inside dependencies
- Change endpoint if needed, it currently sends most current data in entirety
- Output format depends on arguments
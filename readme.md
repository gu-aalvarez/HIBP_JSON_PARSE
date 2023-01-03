# HIBP Json Pull and Parse

## Usage
1. Acquire the JSON URL from Have I Been Pwned
2. Use the `url_json_pull.ps1` script to pull the JSON file
   1. you can feed the URL as an argument - `.\url_json_pull.ps1 https://haveibeenpwned.com/DomainSearch/<URI>/json` or run `.\url_json_pull.ps1` by itself and it will ask for the URL
3. After `url_json_pull.ps1` is ran a .json file named `hibp.json` will be created, there is no need to prettify\format the file if you just want to parse it.
4. Run `python.exe HIBP_JSON_Parse.py` and it will output a timestamped csv file from the parsed JSON.
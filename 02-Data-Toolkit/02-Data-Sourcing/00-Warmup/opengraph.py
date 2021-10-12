# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""
import pprint
import requests
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(fetch_metadata("https://www.lewagon.com"))

def fetch_metadata(url):
    """
    """
    
    response = requests.get(f'https://opengraph.lewagon.com/?url={url}')
    if response.status_code != 200:
        return ''
    data = response.json()['data']
    
    return data
    
 
    #Return a dictionary of OpenGraph metadata found in HTML of given url
    # TODO: implement this function!

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.lewagon.com"))

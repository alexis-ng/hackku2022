import requests
import math
GOOGLE_API_KEY = 'AIzaSyBoclwNkaJnjOw1HmX80-D13zWw275PZY4' 

def extract_lat_long_via_address(address_or_zipcode):
    lat, lng = None, None
    api_key = GOOGLE_API_KEY
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return [lat, lng]

print(extract_lat_long_via_address(66061))


def haversine(applicant_loc, employer_loc):
    radius = 3958.8
    lat1 = math.radians(applicant_loc[0])
    lat2 = math.radians(employer_loc[0])
    long1 = math.radians(applicant_loc[1])
    long2 = math.radians(employer_loc[1])
    delta_lat = math.radians(applicant_loc[0] - employer_loc[0])
    delta_long = math.radians(applicant_loc[1] - employer_loc[1])
    a = (math.sin(delta_lat/2)**2)\
        + math.cos(lat1) * math.cos((lat2))\
             *  (math.sin(delta_long/2)**2)
    c = 2*(math.atan2(math.sqrt(a), math.sqrt(1-a)))
    d = radius * c 
    return d

print(haversine([38.9499492, -95.2658318], [38.9071042, -94.8728093]))

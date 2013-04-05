from rauth import OAuth2Service
import json
import codecs

foursquare = OAuth2Service(
    client_id='OWZIQVDO4TO3FLF1DGJNAYAS2MBKB5EXYLDFSXNHZIVKAZ1O',
    client_secret='PEOT3ZKAFRVKREOW2XVLJ1BJTSOHPNCS1D4JRBVASXR4YXEK',
    name='foursquare',
    authorize_url='https://foursquare.com/oauth2/authenticate',
    access_token_url='https://foursquare.com/oauth2/access_token',
    base_url='https://api.foursquare.com/v2/')

redirect_uri = 'https://foursquare.com/'

params = {'response_type': 'token',
          'redirect_uri': redirect_uri}

authorize_url = foursquare.get_authorize_url(**params)

print 'Visit this URL in your browser: ' + authorize_url

access_token = raw_input('Copy the access token from your browser\'s address bar: ')
session = foursquare.get_session(access_token)

checkin_endpoint = 'https://api.foursquare.com/v2/users/self/checkins'

query_params = {
    'oauth_token': access_token,
    'limit': '75',
    'sort': 'newestfirst',
    'v': '20130403'
}

fs_checkins = session.get(checkin_endpoint, params = query_params)
fs_checkin_data = json.loads(fs_checkins.content)

fs_checkins_file = codecs.open('fs_checkins.csv', 'w', 'utf8')

for item in fs_checkin_data['response']['checkins']['items']:
    venue = item['venue']
    venue_name = venue['name']
    venue_url = venue['canonicalUrl']
    print venue_name + '\n' + venue_url
    fs_checkins_file.write(','.join([venue_name, venue_url]) + '\n')

fs_checkins_file.close()



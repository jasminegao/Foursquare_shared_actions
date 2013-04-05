from rauth import OAuth2Service
import json
import pprint

#0WQQVBL1H4R2J05UMZAQ5EGUCA5NW4DSJMMZEMQA5CXQBJZ5

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

badges_endpoint = 'https://api.foursquare.com/v2/users/self/badges'

query_params = {
    'oauth_token': access_token,
    'v': '20130403'
}

fs_badges = session.get(badges_endpoint, params = query_params)
fs_badges_data = json.loads(fs_badges.content)

fs_badges_file = open('fs_badges.csv', 'w')

for _,item in fs_badges_data['response']['badges'].items():
    badge_name = item['name']
    badge_img_url = 'https://playfoursquare.s3.amazonaws.com/badge/200' + str(item['image']['name'])
    if badge_img_url != 'https://playfoursquare.s3.amazonaws.com/badge/200/default_off.png': #if badge is still locked do not write
        print badge_name + '\n' + badge_img_url
        fs_badges_file.write(','.join([badge_name, badge_img_url]) + '\n')

fs_badges_file.close()
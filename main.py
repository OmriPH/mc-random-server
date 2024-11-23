import os
import random
import time
import requests
from dotenv import load_dotenv

load_dotenv()

CLOUDFLARE_EMAIL = os.environ.get("CLOUDFLARE_EMAIL")
CLOUDFLARE_API_KEY = os.environ.get("CLOUDFLARE_API_KEY")
ZONE_ID = os.environ.get("ZONE_ID")
RECORD_ID = os.environ.get("RECORD_ID")
SUBDOMAIN = os.environ.get("SUBDOMAIN")

domains = open('domains.txt').read().splitlines()

def update():
    domain = random.choice(domains)

    resp = requests.put(
        'https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}'.format(
            ZONE_ID, RECORD_ID),
        json={
            'type': 'CNAME',
            'name': SUBDOMAIN,
            'content': domain,
            'proxied': False
        },
        headers={
            'X-Auth-Key': CLOUDFLARE_API_KEY,
            'X-Auth-Email': CLOUDFLARE_EMAIL
        })
    assert resp.status_code == 200

    print('updated dns record for {} to {}'.format(SUBDOMAIN,domain))


while True:
    update()
    time.sleep(300)

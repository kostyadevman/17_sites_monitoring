import sys
import os
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime, timedelta


def load_urls4check(path_to_file):
    with open(path_to_file, 'r') as file_with_urls:
        urls = file_with_urls.read().splitlines()
        file_with_urls.close()
    return urls


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
        return response.status_code == requests.codes.ok
    except Exception:
        return False


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois(domain_name)
    if isinstance(domain_info.expiration_date, list):
        exp_date = domain_info.expiration_date[0]
    else:
        exp_date = domain_info.expiration_date
    return exp_date


def get_domain_name_from_url(url):
    parsed_url = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_url)


def is_expired(expiration_date, expire_period):
    try:
        return datetime.now() + timedelta(expire_period) < expiration_date
    except Exception:
        return False


if __name__ == '__main__':
    expire_period = 30

    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        exit('Usage: python sites_monitoring.py <path to file>')
    file_with_urls = sys.argv[1]

    urls = load_urls4check(file_with_urls)

    for url in urls:
        domain_name = get_domain_name_from_url(url)
        print('Site {} respond with status HTTP 200: {}'.format(
            url,
            is_server_respond_with_200(url)
        ))

        expiration_date = get_domain_expiration_date(domain_name)

        print('Domain {} expiration time more than {} days: {}'.format(
            domain_name,
            expire_period,
            is_expired(expiration_date, expire_period)
         ))
        print('\n')

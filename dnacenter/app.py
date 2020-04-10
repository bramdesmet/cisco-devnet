import simplejson as json
import requests
from requests.auth import HTTPBasicAuth

from .hidden import DNAC_IP
from .hidden import DNAC_USERNAME
from .hidden import DNAC_PASSWORD


def get_auth_token(ip=DNAC_IP, username=DNAC_USERNAME, password=DNAC_PASSWORD):
    """
    Get Authentication Token
    :param ip: (string)
    :param username: (string)
    :param password: (string)
    :return: token (string)
    """

    url = 'https://{0}/api/system/v1/auth/token'.format(ip)
    auth = HTTPBasicAuth(username, password)
    verify = False

    response = requests.post(url=url, auth=auth, verify=False)
    response.raise_for_status()

    token = response.json()['Token']

    return token


def create_url(path, ip=DNAC_IP):
    """
    Create URL for API request
    :param path: (string)
    :param ip: (string)
    :return: url (string)
    """

    url = 'https://{0}/api/v1/{1}'.format(ip, path)
    return url


def request_api(path):
    url = create_url(path)
    token = get_auth_token()
    headers = {
        'X-auth-token': token
    }
    verify = False

    response = requests.get(url, headers=headers, verify=verify)
    return response.json()


def get_devices():
    devices = request_api('network-device')
    return devices


def main():
    print(json.dumps(get_devices(), indent=2))

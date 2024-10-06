import base64
import zlib

import requests
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout


def url_scheme(json_data: str) -> str:
  json_bytes = json_data.encode(encoding='utf-8')
  compressed = zlib.compress(json_bytes, level=9)
  b64bytes = base64.urlsafe_b64encode(compressed)
  param_body = b64bytes.decode('utf-8').replace('=', '~')
  scheme_header = 'pythonista3://?action=add-theme&theme-data='
  return f'{scheme_header}{param_body}'


def shorten_url(full_url: str) -> str:
  api_url = 'http://tinyurl.com/api-create.php'
  params = {'url': full_url}
  
  try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()
  except ConnectionError as e:
    print(f'Connection Error:{e}')
    raise
  except HTTPError as e:
    print(f'HTTP Error:{e}')
    raise
  except Timeout as e:
    print(f'Timeout Error:{e}')
    raise
  except RequestException as e:
    print(f'Error:{e}')
    raise
  return response.text

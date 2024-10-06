from pathlib import Path
import json

import requests
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout

from .root_locate import VS_LOCAL
from .to_dump import to_dump


class VSCodeThemeServer:
  file_name: str
  tmp_dir: Path
  data: dict
  info: dict
  dump: str
  info_keys: list[str] = [
    '___repository_url',
    '___author_name',
    '___license_kind',
    '___pushed_at',
    '___file_name',
    '___file_url',
  ]
  
  def __init__(self,
               theme_json_url: str,
               use_local: bool = False,
               tmp_dir: Path = VS_LOCAL):
    
    self.__json_url = theme_json_url
    self.file_name = self.__get_file_name(theme_json_url)
    self.tmp_dir = tmp_dir
    
    if use_local:
      self.data, self.info = self.__get_tmp_data_info()
    else:
      self.data = self.__get_data()
      self.info = self.__get_info()
    
    self.dump = to_dump(self.data, self.info)
  
  def get_value(
      self,
      top_name: str = '',
      colors: str | None = None,
      tokenColors: list[str] | None = None) -> str | bool | int | float | None:
    value = None
    
    if top_name:
      value = self.data.get(top_name)
    elif colors is not None and isinstance(colors, str):
      value = self.__for_colors(colors)
    elif tokenColors is not None and isinstance(tokenColors, list):
      value = self.__for_token_colors(tokenColors)
    
    if value is None:
      raise ValueError(
        f'value の値が`{value}` です:\n- {top_name=}\n- {colors=}\n- {tokenColors=}'
      )
    return value
  
  def __for_colors(self, key: str) -> str | bool | int | float | None:
    return self.data['colors'].get(key)
  
  def __for_token_colors(self,
                         keys: list[str]) -> str | bool | int | float | None:
    scope, settings = keys
    for tokenColor in self.data.get('tokenColors'):
      _scope = tokenColor.get('scope')
      # xxx: 配列格納に合わせる
      scopes = _scope if isinstance(_scope, list) else [_scope]
      if scope in scopes:
        return tokenColor.get('settings').get(settings)
  
  @staticmethod
  def __get_file_name(url: str) -> str:
    path = Path(url)  # xxx: 取り出し方が乱暴
    if path.suffix == '.json':
      return path.name
    else:
      raise ValueError(f'`.json` 形式のファイルではありません\n\turl:{url}')
  
  def __get_tmp_data_info(self) -> list[dict]:
    data_text = Path(self.tmp_dir, self.file_name).read_text(encoding='utf-8')
    loads = json.loads(data_text)
    
    info = self.__create_info(*[loads.get(key) for key in self.info_keys])
    
    return [
      loads,
      info,
    ]
  
  def __get_data(self) -> dict | None:
    params = {
      'raw': 'true',
    }
    
    try:
      response = requests.get(self.__json_url, params=params)
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
    # xxx: iceberg には、comment なし
    # wip: `.jsonc` (JSON with Comments) 対応
    return response.json()
  
  def __get_info(self) -> dict | None:
    tokens = self.__api_tokens()
    
    _url = tokens.get('html_url')
    _name = tokens.get('owner').get('login')
    _license = l.get('name') if (l :=
                                 tokens.get('license')) is not None else str(l)
    _pushed_at = tokens.get('pushed_at')
    
    # xxx: `None` は許容?
    pre_info = [
      _url,
      _name,
      _license,
      _pushed_at,
    ]
    
    info = self.__create_info(*pre_info)
    return info
  
  def __api_tokens(self) -> dict:
    _, _, owner_name, repo_name, *_ = Path(
      self.__json_url).parts  # xxx: 取り出し方が乱暴
    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}'
    
    try:
      response = requests.get(api_url)
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
    
    return response.json()
  
  def __create_info(self,
                    repository_url: str,
                    author_name: str,
                    license_kind: str,
                    pushed_at: str,
                    file_name: str | None = None,
                    file_url: str | None = None) -> dict:
    values = [
      repository_url,
      author_name,
      license_kind,
      pushed_at,
      self.file_name if file_name is None else file_name,
      self.__json_url if file_url is None else file_url,
    ]
    info = {key: value for key, value in zip(self.info_keys, values)}
    
    return info

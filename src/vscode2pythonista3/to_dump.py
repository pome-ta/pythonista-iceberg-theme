import json


def to_dump(json_data: dict, info_data: dict | None = None) -> str:
  dump_data = json_data if info_data is None else json_data | info_data
  kwargs = {
    'indent': 1,
    'sort_keys': True,
    'ensure_ascii': False,
  }
  return json.dumps(dump_data, **kwargs)

from pathlib import Path

from .root_locate import PY_LOCAL
from .server import VSCodeThemeServer
from .to_dump import to_dump
from .export import export


def get_user_theme_dir() -> Path | None:
  try:
    # xxx: 一応
    from objc_util import ObjCClass
  except ModuleNotFoundError as e:
    print(f'{e}:')
    return None
  _path_objc = ObjCClass('PA2UITheme').sharedTheme().userThemesPath()
  _path = Path(str(_path_objc))
  return _path


def build(convert_fnc,
          ts: VSCodeThemeServer,
          save_vscode: bool = True,
          vscode_dir: Path = None,
          save_pythonista: bool = True,
          pythonista_dir: Path = PY_LOCAL) -> str:
  converted = convert_fnc(ts)
  theme_dump = to_dump(converted)
  
  if save_vscode:
    export(ts.dump, ts.file_name,
           ts.tmp_dir if vscode_dir is None else vscode_dir)
  if save_pythonista:
    export(theme_dump, ts.file_name, pythonista_dir)
  
  if (user_theme_dir := get_user_theme_dir()) is not None:
    export(theme_dump, ts.file_name, user_theme_dir)
  else:
    print('値が`None`')
  
  return theme_dump

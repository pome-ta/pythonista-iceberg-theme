from pathlib import Path

# todo: Pythonista3 以外での`Path` 挙動クッション用
ROOT_PATH: Path = Path(__file__).parent
VS_LOCAL = Path(ROOT_PATH, '../opt/VSCodeThemeDumps')
PY_LOCAL = Path(ROOT_PATH, '../../theme')

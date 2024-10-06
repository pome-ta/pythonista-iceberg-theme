from pathlib import Path

from vscode2pythonista3 import VSCodeThemeServer, build
from transcription import create_section, to_override


def convert(ts: VSCodeThemeServer) -> dict:
  def is_dict_in_none_value(dct: dict | str | None, parent: str = '') -> bool:
    for ky, vl in dct.items():
      if isinstance(vl, dict):
        if is_dict_in_none_value(vl, f'{parent}.{ky}' if parent else ky):
          return True
      else:
        if vl is None:
          print(f'値に`None` が存在します')
          print(f'{parent=}:\n\tkey={ky}: value={vl}')
          return True
    return False
  
  main = dict()
  # GitHub Repository Data
  main |= ts.info
  d = dict()
  # Pythonista3 Color Theme
  d['background'] = ts.get_value(colors='editor.background')
  d['bar_background'] = ts.get_value(colors='tab.activeBackground')
  d['dark_keyboard'] = True
  d['default_text'] = ts.get_value(tokenColors=[
    'text',
    'foreground',
  ])
  d['editor_actions_icon_background'] = ts.get_value(
    colors='menu.selectionBackground')
  d['editor_actions_icon_tint'] = ts.get_value(
    colors='menu.selectionForeground')
  d['editor_actions_popover_background'] = ts.get_value(
    colors='menu.background')
  d['error_text'] = ts.get_value(colors='editorError.foreground')
  
  # d['font-family'] = 'Menlo-Regular'
  # d['font-siz'] = 15.0
  
  d['gutter_background'] = ts.get_value(colors='editorGutter.background')
  d['gutter_border'] = ts.get_value(colors='tab.border')
  d['interstitial'] = '#ff00ff'  # xxx: 仮
  d['library_background'] = ts.get_value(colors='sideBar.background')
  d['library_tint'] = ts.get_value(colors='sideBarSectionHeader.foreground')
  d['line_number'] = ts.get_value(colors='editorLineNumber.foreground')
  d['name'] = ts.get_value('name')
  d['separator_line'] = ts.get_value(colors='focusBorder')
  d['tab_background'] = ts.get_value(colors='tab.inactiveBackground')
  d['tab_title'] = ts.get_value(colors='tab.inactiveForeground')
  d['text_selection_tint'] = ts.get_value(
    colors='editorLineNumber.activeForeground')
  d['thumbnail_border'] = ts.get_value(colors='sideBar.border')
  d['tint'] = ts.get_value(colors='editorCursor.foreground')
  
  s = dict()  # scopes
  s['bold'] = {
    'font-style': 'bold',
  }
  s['bold-italic'] = {
    'font-style': 'bold-italic',
  }
  s['builtinfunction'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.function',
      'foreground',
    ]),
  }
  s['checkbox'] = {
    'checkbox': True,
  }
  s['checkbox-done'] = {
    'checkbox': True,
    'done': True,
  }
  s['class'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.class',
      'foreground',
    ]),
  }
  s['classdef'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.class',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['code'] = {
    'background-color':
      ts.get_value(tokenColors=[
        'markup.fenced_code.block',
        'foreground',
      ]),
    'corner-radius':
      2.0,
  }
  s['codeblock-start'] = {
    'color':
      ts.get_value(tokenColors=[
        'markup.inline.raw.string',
        'foreground',
      ]),
  }
  s['comment'] = {
    'color': ts.get_value(tokenColors=[
      'comment',
      'foreground',
    ]),
    'font-style': 'italic',
  }
  s['decorator'] = {
    'color': ts.get_value(tokenColors=[
      'meta.type.annotation',
      'foreground',
    ]),
  }
  s['default'] = {
    'color': ts.get_value(tokenColors=[
      'text',
      'foreground',
    ]),
  }
  s['docstring'] = {
    'color':
      ts.get_value(tokenColors=[
        'entity.other.attribute-name',
        'foreground',
      ]),
    'font-style':
      'italic',
  }
  s['escape'] = {
    'background-color': ts.get_value(tokenColors=[
      'support',
      'foreground',
    ]),
  }
  s['formatting'] = {
    'color':
      ts.get_value(tokenColors=[
        'markup.fenced_code.block',
        'foreground',
      ]),
  }
  s['function'] = {
    'color':
      ts.get_value(tokenColors=[
        'entity.name.function.method',
        'foreground',
      ]),
  }
  s['functiondef'] = {
    'color':
      ts.get_value(tokenColors=[
        'entity.name.function.method',
        'foreground',
      ]),
    'font-style':
      'bold',
  }
  s['heading-1'] = {
    'color': ts.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['heading-2'] = {
    'color': ts.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['heading-3'] = {
    'color': ts.get_value(tokenColors=[
      'markup.heading',
      'foreground',
    ]),
    'font-style': 'bold',
  }
  s['italic'] = {
    'font-style': 'italic',
  }
  s['keyword'] = {
    'color': ts.get_value(tokenColors=[
      'keyword',
      'foreground',
    ]),
  }
  s['link'] = {
    'text-decoration': 'underline',
    'color': ts.get_value(tokenColors=[
      'markup.underline.link',
      'foreground',
    ]),
  }
  s['marker'] = {
    'box-background-color':
      ts.get_value(colors='editorMarkerNavigation.background'),
    'box-border-color':
      ts.get_value(colors='inputOption.activeBorder'),
    'box-border-type':
      4,
  }
  s['module'] = {
    'color': ts.get_value(tokenColors=[
      'entity.name.import.go',
      'foreground',
    ]),
  }
  s['number'] = {
    'color': ts.get_value(tokenColors=[
      'constant',
      'foreground',
    ]),
  }
  s['project'] = {
    'font-style': 'bold',
  }
  s['string'] = {
    'color': ts.get_value(tokenColors=[
      'string',
      'foreground',
    ]),
  }
  s['tag'] = {
    'text-decoration': 'none',
  }
  s['task-done'] = {
    'color': ts.get_value(colors='notificationsInfoIcon.foreground'),
    'text-decoration': 'strikeout',
  }
  
  d['scopes'] = s
  
  if is_dict_in_none_value(d):
    raise ValueError('設定する値に`None` が存在するため変換できません')
  main |= d
  return main


def for_theme_sections(theme_url: str) -> str:
  theme_server = VSCodeThemeServer(theme_url)
  json_dump = build(convert, theme_server)
  file_name = theme_server.file_name
  theme_name = theme_server.data['name']
  section = create_section(json_dump, file_name, theme_name)
  return section


if __name__ == '__main__':
  dark_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg.color-theme.json'
  light_url = 'https://github.com/cocopon/vscode-iceberg-theme/blob/main/themes/iceberg-light.color-theme.json'
  
  urls = [
    dark_url,
    light_url,
  ]
  sections = [for_theme_sections(u) for u in urls]
  to_override(*sections)
  x = 1

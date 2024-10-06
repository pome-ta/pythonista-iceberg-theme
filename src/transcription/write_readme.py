from pathlib import Path

from jinja2 import Template

from .create_url import url_scheme, shorten_url

# todo: Pythonista3 以外での`Path` 挙動クッション用
ROOT_PATH: Path = Path(__file__).parent
tmp_dir = Path(ROOT_PATH, '../opt')

readme_template = 'readmeTemplate.md'
section_template = 'sectionTemplate.md'


def create_section(json_dump: str, file_name: str, theme_name: str) -> str:
  section_file = Path(tmp_dir, section_template)
  section_md = section_file.read_text(encoding='utf-8')
  template: Template = Template(source=section_md)
  
  compiled_scheme = url_scheme(json_dump)
  shortened_url = shorten_url(compiled_scheme)
  
  render_kwargs = {
    'name_header': theme_name,
    'link_name': file_name,
    'link_url': shortened_url,
    'scheme_raw': compiled_scheme,
  }
  rendered = template.render(render_kwargs)
  return rendered


def to_override(*args):
  new_line = '\n'
  sections = (new_line * 2).join(args)
  
  readme_file = Path(tmp_dir, readme_template)
  readme_md = readme_file.read_text(encoding='utf-8')
  template: Template = Template(source=readme_md)
  
  render_kwargs = {
    'section': sections,
  }
  rendered = template.render(render_kwargs)
  master_readme = Path(ROOT_PATH, '../../', 'README.md')
  master_readme.write_text(rendered, encoding='utf-8')

# wip: export しないvar も？

import webbrowser
import urllib.parse
from objc_util import ObjCClass

themes_path = str(ObjCClass('PA2UITheme').sharedTheme().userThemesPath())
url_path = '/..' * 9 + urllib.parse.quote(themes_path)

webbrowser.open(f'pythonista3://{url_path}')

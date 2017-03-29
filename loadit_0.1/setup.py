from distutils.core import setup
from glob import glob
import py2exe, re, os

def reglob(path, exp, invert=False):
    """glob.glob() style searching which uses regex
    :param exp: Regex expression for filename
    :param invert: Invert match to non matching files
    """
    m = re.compile(exp)
    if invert is False:
        res = [f for f in os.listdir(path) if m.search(f)]
    else:
        res = [f for f in os.listdir(path) if not m.search(f)]

    res = map(lambda x: "%s/%s" % ( path, x, ), res)
    return res

#tweak data_files to match your develop environment
#C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\redist\x86\Microsoft.VC120.CRT
# data_files = [("Microsoft.VC120.CRT", glob(r'C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\redist\x86\Microsoft.VC120.CRT\*.*'))]
#C:\Windows\System32\*.dll
data_files = [("Microsoft.VC120.CRT", glob(r'C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\redist\x86\Microsoft.VC120.CRT\*.*')), ("", reglob(r'C:\Windows\System32', r'(adv|ole|imm|com|gdi|ws2|user|shel|kern).*32\.dll$')), ("", ['loadit.cfg', 'lgc36.txt'])]
include_opt = {
	"optimize": 0,
	"includes": ['mechanize', 'bs4'],
	"excludes": ['_scproxy', 'builder.ParserRejectedMarkup', 'builder.builder_registry', 'cchardet', 'chardet', 'email.Utils', 'html.parser', 'html5lib', 'html5lib.constants', 'iconv_codec', 'lxml', 'wx', 'tcl'],
	"ascii": False,
}

"""
First build a console executable. When the exe works you can switch to windows version by replacing 'windows' with 'console'. 
Samples in lib\site-packages\py2exe\samples demonstrate several simple and advances features.
"""
setup(name="loadit",
    version="0.1",
    description="Load data from external data files into information management systems on dlmu.edu.cn",
    author="TSMC Labs",
    url="http://tsmc.dlmu.edu.cn/",
    author_email="rchen@dlmu.edu.cn",
    data_files=data_files,
    options = {'py2exe': include_opt},
    # windows=['loadit.py']       #to build a windows version
    console=['loadit.py']     #to build a console version
    )


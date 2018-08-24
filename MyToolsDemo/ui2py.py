# coding: utf-8
# convert *.ui to *_ui.py

import os
import sys
from pyside2uic import compileUi


def ui2py(uifile):
    pyfilename = '_'.join(uifile.rsplit('.', 1)) + '.py'
    with open(pyfilename, 'w') as pyfile:
        compileUi(uifile, pyfile)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        for f in files:
            ui2py(f)
            print(f, 'ui2py Done')

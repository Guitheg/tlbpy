#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

MAIN = os.path.abspath(os.path.dirname(__file__))
INIT = "__init__.py"

def upload():
    if len(sys.argv) != 1 + 2:
        print("Usage : <package_name> <V|m|p>")
    else:
        packname = sys.argv[1]
        package = os.path.join(MAIN, packname)
        file = os.path.join(package, INIT)
        data = ""
        with open(file) as f:
            for line in f.readlines():
                if line.startswith('__version__'):
                    V, m, p = line.split("=")[1].strip('"\n').split(".")
                    print("new version :",V,m,p)
                    t = sys.argv[2]
                    if t == "V":
                        V = int(V) + 1
                        m = 0
                        p = 0
                    if t == "m":
                        V = int(V)
                        m = int(m) + 1
                        p = 0
                    if t == "p":
                        V = int(V)
                        m = int(m)
                        p = int(p) + 1
                    line = '__version__="'+str(V)+"."+str(m)+"."+str(p)+'"\n'
                data+=line
        with open(file, 'w') as f:
            f.write(data)
        os.system("python setup.py sdist bdist_wheel")
        os.system("twine upload --skip-existing dist/*")

if __name__ == "__main__":
    upload()
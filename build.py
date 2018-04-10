import os

from os import path
from string import Template
from configparser import ConfigParser, ExtendedInterpolation


def get_name(p):
    p = path.abspath(p)
    absname, ext = path.splitext(p)
    dir, name = path.split(absname)
    return name


f = open('page-template.html', 'r')
templ = Template(f.read())
f.close()

meta = ConfigParser()
meta._interpolation = ExtendedInterpolation()
meta.read('meta.ini')

for root, subdirs, files in os.walk('html'):
    for f in files:
        model = dict()

        fo = open('html/' + f, 'r')
        model['license_text'] = fo.read()
        fo.close()

        model['license_name'] = meta[get_name(f)]['name']

        fo = open('page/' + get_name(f) + '.html', 'w')
        fo.write(templ.substitute(model))
        fo.close()

import os

from os import path
from string import Template
from configparser import ConfigParser, ExtendedInterpolation


def get_name(p):
    p = path.abspath(p)
    absname, ext = path.splitext(p)
    dir, name = path.split(absname)
    return name


# == Reading templates == #
f = open('templates/page-template.html', 'r')
tmpl_page = Template(f.read())
f.close()

f = open('templates/index-template.html', 'r')
tmpl_index = Template(f.read())
f.close()

f = open('templates/index-item-template.html', 'r')
tmpl_index_item = Template(f.read())
f.close()

f = open('templates/readme-template.md', 'r')
tmpl_readme = Template(f.read())
f.close()

f = open('templates/readme-index-item.md', 'r')
tmpl_readme_index_item = Template(f.read())
f.close()

f = open('templates/readme-index-item-nohtml.md', 'r')
tmpl_readme_index_item_nohtml = Template(f.read())
f.close()


# == Read templates == #

# == Reading meta == #
meta = ConfigParser()
meta._interpolation = ExtendedInterpolation()
meta.read('meta.ini')
# == Read meta == #

index = ''

# == Generating pages == #
for style_name in ['default', 'structure']:
    f = open('themes/' + style_name + '.css')
    style = f.read()
    f.close()

    for root, subdirs, files in os.walk('html'):
        for f in files:
            if not f.endswith('.html') or f == 'index.html':
                continue
            model = dict()

            fo = open('html/' + f, 'r')
            model['license_text'] = fo.read()
            fo.close()

            id = model['license_id'] = get_name(f)
            model['license_name'] = meta[id]['name']
            model['style'] = style
            model['style_name'] = style_name

            index += tmpl_index_item.substitute(model)

            fo = open('page/' + get_name(f) + ('' if style_name == 'default' else ('_' + style_name)) + '.html', 'w')
            fo.write(tmpl_page.substitute(model))
            fo.close()
# == Generated pages == #

# == Generating indexes == #
index = tmpl_index.substitute({'items': index})

f = open('page/index.html', 'w')
f.write(index)
f.close()

f = open('html/index.html', 'w')
f.write(index)
f.close()
# == Generated indexes == #

# == Generating readme == #
index = ''

for root, subdirs, files in os.walk('txt'):
    for f in files:
        if not f.endswith('.txt') or f == 'index.txt':
            continue

        model = dict()
        id = model['license_id'] = get_name(f)
        model['license_name'] = meta[id]['name']

        if path.exists('html/' + id + '.html'):
            index += tmpl_readme_index_item.substitute(model)
        else:
            index += tmpl_readme_index_item_nohtml.substitute(model)

index = index.split('\n')
index.sort()
index = '\n'.join(index)

f = open('README.md', 'w')
f.write(tmpl_readme.substitute({'index_items': index}))
f.close()

# == Generated readme == #

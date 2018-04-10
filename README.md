<link rel="stylesheet" href="markdown.css">

## A collection of licenses

This repository contains all kinds of original and modified licenses.

### Licenses

| Apache 2.0 | [TXT](/txt/apache_v2.txt) |  |  |
| MIT (Expat) | [TXT](/txt/expat.txt) | [HTML](/html/expat.html) | [PAGE](/page/expat.html) |
| GNU AGPL 3.0 | [TXT](/txt/gnu_agpl_v3.txt) |  |  |
| GNU GPL 3.0 | [TXT](/txt/gnu_gpl_v3.txt) |  |  |
| GNU LGPL 3.0 | [TXT](/txt/gnu_lgpl_v3.txt) |  |  |
| Mozilla Public License 2.0 | [TXT](/txt/mozilla_pl_v2.txt) |  |  |
| The University of Illinois/NCSA Open Source License | [TXT](/txt/ncsa.txt) | [HTML](/html/ncsa.html) | [PAGE](/page/ncsa.html) |
| The Unlicense | [TXT](/txt/unlicense.txt) | [HTML](/html/unlicense.html) | [PAGE](/page/unlicense.html) |
| MIT (X11) | [TXT](/txt/x11.txt) | [HTML](/html/x11.html) | [PAGE](/page/x11.html) |


### File Structure

| File | Use |
|-----:|:----|
| `.gitignore` | ignores the sass cache in `themes/` |
| `README.md` | this file |
| `build.py` | Automatically generates this files, all files in `page/` and index files from the templates in `templates/`. |  
| `markdown.css` | Stylesheet for this file. ([Air](http://markdowncss.github.io/air/)) (Not shown in GitHub) | 
| `meta.ini` | Contains metadata about the licenses (used by `build.py`) |

| Directory | Use |
|----------:|:----|
| `html/` | contains HTML files for the licenses (These aren't full pages they're just a \<small> element) |
| `page/` | contains HTML documents for the licenses (These are full pages they're a \<html> element) |
| `templates/` | contains templates ([PEP 292](https://www.python.org/dev/peps/pep-0292/)) (used by `build.py) |
| `themes/` | contains stylesheets that are automatically included in every *page* but it can also manually applied to *html*. |
| `txt/` | contains the licenses in textual representation |
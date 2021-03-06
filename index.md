<link rel="stylesheet" href="markdown.css">

## A collection of licenses

This repository contains all kinds of original and modified licenses and information about licenses and copyright.  
If you're unsure which license to choose look at [choosealicense.com](https://choosealicense.com/)  
[How to write a Copyright Notice](howto_copyright.html)

### Licenses

| Name | TXT | HTML | PAGE |
|-----:|:----|:-----|:-----|
| Apache 2.0 | [TXT](/txt/apache_v2.txt) | [HTML](/html/apache_v2.html) | [PAGE](/page/apache_v2.html) |
| BSD 2-Clause "Simplified" License | [TXT](/txt/bsd_2_simplified.txt) | [HTML](/html/bsd_2_simplified.html) | [PAGE](/page/bsd_2_simplified.html) |
| BSD 3-Clause "New" License | [TXT](/txt/bsd_3_new.txt) | [HTML](/html/bsd_3_new.html) | [PAGE](/page/bsd_3_new.html) |
| BSD 3-Clause Clear License | [TXT](/txt/bsd_3_clear.txt) | [HTML](/html/bsd_3_clear.html) | [PAGE](/page/bsd_3_clear.html) |
| GNU AGPL 3.0 | [TXT](/txt/gnu_agpl_v3.txt) |  |  |
| GNU GPL 3.0 | [TXT](/txt/gnu_gpl_v3.txt) |  |  |
| GNU LGPL 3.0 | [TXT](/txt/gnu_lgpl_v3.txt) |  |  |
| MIT (Expat) | [TXT](/txt/expat.txt) | [HTML](/html/expat.html) | [PAGE](/page/expat.html) |
| MIT (X11) | [TXT](/txt/x11.txt) | [HTML](/html/x11.html) | [PAGE](/page/x11.html) |
| Mozilla Public License 2.0 | [TXT](/txt/mozilla_pl_v2.txt) |  |  |
| NCSA Open Source License | [TXT](/txt/ncsa.txt) | [HTML](/html/ncsa.html) | [PAGE](/page/ncsa.html) |
| The Unlicense | [TXT](/txt/unlicense.txt) | [HTML](/html/unlicense.html) | [PAGE](/page/unlicense.html) |

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
| `templates/` | contains templates ([PEP 292](https://www.python.org/dev/peps/pep-0292/)) (used by `build.py`) |
| `themes/` | contains stylesheets that are automatically included in every *page* but it can also manually applied to *html*. |
| `txt/` | contains the licenses in textual representation |

<a href="https://github.com/Ma124/Licenses">Look at the source</a>

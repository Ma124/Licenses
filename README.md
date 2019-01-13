<link rel="stylesheet" href="markdown.css">

# Deprecated: Use [`https://ma124.js.org/l/<LICENSE>/<NAME>~<SITE>~<EMAIL>/<YEAR>`](https://ma124.js.org/misc/licenses_about.html)
# [Look at the website](https://ma124.github.io/Licenses)

This repository contains all kinds of original and modified licenses and information about licenses and copyright.

### File Structure

| File | Use |
|-----:|:----|
| `.gitignore` | ignores the sass cache in `themes/` |
| `README.md` | this file |
| `build.py` | Automatically generates the frontpage (`/index.html`), all files in `page/` and index files from the templates in `templates/`. |  
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

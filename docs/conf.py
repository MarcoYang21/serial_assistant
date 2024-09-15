# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Serial Assistant'
copyright = "2024, Marco'''s Studio"
author = 'Marco Yang'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'py-unhcr'
copyright = '2024'
author = 'Luis Alfredo Chaparro Gomez'
release = '0.1.2'

# General configuration
extensions = [
    'sphinx.ext.autodoc',     # Automatically include docstrings
    'sphinx.ext.napoleon',    # Support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',    # Add links to source code
    'sphinx.ext.githubpages', # Create .nojekyll file for GitHub Pages
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'  # Read the Docs theme

# Add any paths that contain custom static files (such as style sheets)
html_static_path = ['_static']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Language settings
language = 'en'
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'getting-started'
copyright = '2025, Giang Phan Truong'
author = 'Giang Phan Truong'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 
              'sphinx_copybutton', 
              'sphinx_new_tab_link', 
              'sphinx_rtd_dark_mode', 
              'sphinxemoji.sphinxemoji', 
              'sphinx_favicon',
              ]

templates_path = ['_templates']
exclude_patterns = []

sphinxemoji_style = 'twemoji'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

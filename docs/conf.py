# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = 'React Tutorial with Typescript'
copyright = '2025, David G.'
author = 'David G.'

version = '1.0.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = []
extensions = [
        'myst_parser',
        'sphinx_rtd_theme',
        "sphinx_design"
    ]

templates_path = ['_templates']
exclude_patterns = []
myst_enable_extensions = ["colon_fence"]
numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_theme_path = ["."]
html_static_path = ['_static']
html_show_sourcelink = False
html_css_files = [
    'css/custom-theme.css'
    # 'css/bootstrap.min.css'
]
html_js_files = [
    # 'css/bootstrap.min.js'
]
html_theme_options = {
    # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,


    'logo_only': False,
    #'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 6,
    'includehidden': True,
    'titles_only': False
}

html_context = {
    'display_github': False
}
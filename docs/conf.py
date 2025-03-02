"""Sphinx configuration."""

project = "djapi-blog"
author = "Kevin Bowen"
copyright = f"2025, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "djapi-blog"
extensions = [
    "sphinx.ext.duration",
]

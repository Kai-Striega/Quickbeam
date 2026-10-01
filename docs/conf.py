"""Sphinx configuration for the Quickbeam documentation."""

from importlib.metadata import PackageNotFoundError, version

project = "Quickbeam"
author = "the Quickbeam developers"
copyright = "2026, the Quickbeam developers"

try:
    release = version("quickbeam")
except PackageNotFoundError:  # building docs without the package installed
    release = "unknown"
version = release

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3
exclude_patterns = ["_build"]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

html_theme = "pydata_sphinx_theme"
html_title = "Quickbeam"
html_theme_options = {
    "github_url": "https://github.com/Kai-Striega/Quickbeam",
    "use_edit_page_button": True,
    "navigation_with_keys": False,
}
html_context = {
    "github_user": "Kai-Striega",
    "github_repo": "Quickbeam",
    "github_version": "main",
    "doc_path": "docs",
}

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Blood and the Circulatory System in the Human Body'
copyright = '2026, Tri Nguyen'
author = 'Tri Nguyen'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'atsphinx.color_text',
    'sphinx_revealjs',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'furo'
# html_theme = "sphinx_rtd_theme"
# html_theme = "sphinx_book_theme"

html_theme = "sphinx_revealjs"

html_static_path = ['_static']

# ============================================================
# sphinx-revealjs configuration (all options commented out)
# ============================================================

# ------------------------------------------------------------
# Basic revealjs builder options
# ------------------------------------------------------------

# Paths that contain extra static files for revealjs
# (similar to html_static_path, but revealjs-specific)
revealjs_static_path = ['_static']

# Additional JavaScript files to include
# (relative to revealjs_static_path or absolute URLs)
# revealjs_js_files = [
#     'custom.js',
# ]

# Additional CSS files to include
# (relative to revealjs_static_path or absolute URLs)
revealjs_css_files = [
    'custom.css',
]

# Whether to generate genindex.html
# Usually False for slides
# revealjs_use_index = False

# HTML theme used by sphinx-revealjs
# Built-in options: "revealjs-basic", "revealjs-simple"
# revealjs_html_theme = "revealjs-basic"


# ------------------------------------------------------------
# Reveal.js presentation style
# ------------------------------------------------------------

# Reveal.js slide theme
# Built-in Reveal.js themes:
# Black (Default): Sleek, professional dark theme.
# White: Clean, light backdrop for clarity.
# League: High-contrast dark theme with bold typography.
# Beige: Warm, light-toned classic look.
# Sky: Light blue aesthetic with rounded corners.
# Night: Dark theme with high contrast and sharp colors.
# Serif: Elegant light theme using serif fonts.
# Simple: Minimalist light theme with basic styling.
# Solarized: Based on the popular Solarized color scheme (often available in both light and dark).
# Moon: Dark theme featuring blue and grey tones.
# Blood: Dark theme with deep red accents.
# Dracula: A vibrant dark theme based on the Dracula spec
revealjs_style_theme = "Beige"

# ------------------------------------------------------------
# Section / slide behavior
# ------------------------------------------------------------

# Use section IDs instead of auto-numbered anchors
# Useful for stable internal links
# revealjs_use_section_ids = False


# ------------------------------------------------------------
# Reveal.js initialization (Reveal.initialize)
# ------------------------------------------------------------

# Extra JS files loaded AFTER reveal.js core
# Useful for custom logic
# revealjs_script_files = [
#     'extra-script.js',
# ]

# Reveal.js initialization config
# Can be:
#   - a Python dict (recommended)
#   - a raw JavaScript string
#
# Example options you can try:
# controls, progress, center, hash, transition,
# backgroundTransition, slideNumber, disableLayout,
# width, height, margin, minScale, maxScale

revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "slideNumber": True,
    "hash": True,
    "center": False,
    "transition": "slide",  # none / fade / slide / convex / concave / zoom
    "width": 1280,
    "height": 720,
    "margin": 0.04,
    "minScale": 1,
    "maxScale": 1,
}

# ------------------------------------------------------------
# Reveal.js plugins
# ------------------------------------------------------------

# Plugins must be declared as a list of dicts
# Each plugin dict usually contains:
#   - src   : JS file path
#   - name  : plugin variable name
#   - async : optional
#
# Common plugins:
#   - notes
#   - highlight
#   - zoom
#   - search
#
# revealjs_script_plugins = [
#     {
#         "src": "plugin/notes/notes.js",
#         "name": "RevealNotes",
#     },
#     {
#         "src": "plugin/highlight/highlight.js",
#         "name": "RevealHighlight",
#         "async": True,
#     },
# ]


# ------------------------------------------------------------
# Speaker notes
# ------------------------------------------------------------

# Extract speaker notes from HTML comments
# Example:
#   <!-- This is a speaker note -->
# revealjs_notes_from_comments = False

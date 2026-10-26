# Unified docs for the pymmcore-plus ecosystem.  See docs/contributing/docs.md.

# clone missing member repos into .repos/
repos *args:
    uv run --no-project tools/repos.py {{ args }}

# assemble the site and serve it with live reload
serve *args: repos
    uv run tools/compose.py serve {{ args }}

# assemble and build the site into site/
build *args: repos
    uv run tools/compose.py build {{ args }}

# fail on any warning
check: repos
    uv run tools/compose.py build --strict

# compare the old (live) site's URLs against the new build
check-urls *args:
    uv run tools/check_urls.py {{ args }}

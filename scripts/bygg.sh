#!/usr/bin/env bash
# Bygger nettstedet til site/: forsiden med språkvalg, site/no/ og site/en/.
set -euo pipefail
cd "$(dirname "$0")/.."
for L in no en; do
  mkdir -p "docs/$L/assets"
  cp assets/nm.css assets/feltliste.xlsx "docs/$L/assets/"
done
rm -rf site && mkdir -p site
mkdocs build --strict -f mkdocs.no.yml
mkdocs build --strict -f mkdocs.en.yml
cp index.html site/index.html
touch site/.nojekyll

#!/bin/bash
# Update the gh-pages branch and push to GitHub.

set -o nounset
set -o errexit
set -o pipefail

# Easy fix to enable calling this from any path in the repository.
BUILD_DIR="$(git rev-parse --show-toplevel)/doc/.build/html"

if [ ! -d "$BUILD_DIR" ]; then
    echo "HTML documentation build not found in $BUILD_DIR"
    echo "Are you in the project repository?"
    echo "Did you do an HTML build (make html)?"
    exit 1
fi

GH_PAGES="$(mktemp -d)"

git clone -b gh-pages git@github.com:martijnvermaat/calmap.git "$GH_PAGES"
export GIT_DIR="$GH_PAGES/.git"
export GIT_WORK_TREE="$BUILD_DIR"

touch "$BUILD_DIR/.nojekyll"
git add --all
git commit --allow-empty -m "Update docs"

git push

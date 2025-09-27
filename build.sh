# Check if commit message is provided
# if [ -z "$1" ]; then
#     echo "Error: Commit message is required"
#     echo "Usage: $0 \"your commit message\""
#     exit 1
# fi

#!/bin/bash
python scripts/scrape-goodreads-shelf.py

# git submodule update --init --recursive
# git submodule update --remote

# build site and output to 'public/'
hugo

# cd public/
# git add .
# git commit -m "$1"

# cd ../

# git add .
# git commit -m "$1"

# git push -u origin develop --recurse-submodules=on-demand
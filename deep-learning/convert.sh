#!/bin/bash

# check for nb name
if [ $# -eq 0 ]; then
  echo "Error: No nb provided"
  echo "Usage: $0 notebook_name.ipynb"
  exit 1
fi

jupyter nbconvert --to html "$1"

echo "Groovy dude: $1 converted."

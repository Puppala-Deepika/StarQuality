#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    curl -X PATCH  -d   "$line" 'https://datamining-40114.firebaseio.com/products.json'
  
done < "$1"

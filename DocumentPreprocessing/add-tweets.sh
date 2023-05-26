#!/bin/bash
set -B                  # enable brace expansion
for i in {0..0}; do
  curl -XPOST "http://admin:Zi12ZnK2r2n@127.0.0.1:5984/twitter/_bulk_docs" --header "Content-Type: application/json" --data @./located-tweets$i.json
done
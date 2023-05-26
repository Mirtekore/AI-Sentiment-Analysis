#!/bin/bash
set -B                  # enable brace expansion
scp add-tweets.sh ubuntu@172.26.135.240:~/data/twitterdata
for i in {0..0}; do
  scp located-tweets$i.json ubuntu@172.26.135.240:~/data/twitterdata
done
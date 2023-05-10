#!/usr/bin/env bash

# Runs into max connection streams on mastodon social
export MASTODON_ACCESS_TOKEN="psbBwt1Fup13_91jQXtLxrWZ6U57XOwZmX5LK-ZF-sU"
export URL='https://mastodon.social/api/v1'

curl --header "Authorization: Bearer ${MASTODON_ACCESS_TOKEN=}" \
     -XGET \
     -vvv \
     "${URL}/streaming/hashtag?tag=AI" 

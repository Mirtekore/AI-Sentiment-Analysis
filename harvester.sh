#!/usr/bin/env bash

# Runs into max connection streams on mastodon social
# Works fine for aus social
export MASTODON_ACCESS_TOKEN=""EdOcJee5mHnl5eX1DHqQzFZaJ_FzrfIJm8uERDEuZVw""
export URL='https://aus.social/api/v1'

curl --header "Authorization: Bearer ${MASTODON_ACCESS_TOKEN=}" \
     -XGET \
     -vvv \
     "${URL}/streaming/hashtag?tag=AI" 

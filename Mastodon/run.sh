#!/bin/bash

ansible-playbook --ask-become-pass -i hosts -u ubuntu --ask-vault-pass mastodon.yaml -vvv
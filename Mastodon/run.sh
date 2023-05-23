#!/bin/bash

# ansible-playbook -i hosts -u ubuntu --ask-vault-pass mastodon.yaml -vvv
ansible-playbook -i hosts -u ubuntu mastodon.yaml -vvv
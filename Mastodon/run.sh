#!/bin/bash

ansible-playbook -i hosts -u ubuntu --ask-vault-pass mastodon.yaml -vvv
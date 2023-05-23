#!/bin/bash
ansible-galaxy collection install openstack.cloud:1.10.0
. ./openrc.sh; ansible-playbook -vv mrc.yaml | tee output.txt
#!/usr/bin/env bash

set -e

if [[ "$(uname)" != "Darwin" ]]; then
  echo "This script can run only on OS-X"
fi

ACTION=${1:-'up'}

vagrant box update
vagrant box prune
vagrant destroy -f
if [[ "$ACTION" == "destroy" ]]; then
  exit
fi
vagrant up

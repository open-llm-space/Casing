#!/bin/bash

PORT="8080"

while getopts "p:" flag; do
  case "${flag}" in
    p) PORT="${OPTARG}" ;;
    *) exit 1 ;;
  esac
done

ttyd --port $($port) --max-clients 1 --once --exit-no-conn --writable claude --add-dir ./setup/instruct --settings ./.claude/settings.json
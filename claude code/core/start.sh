#!/bin/bash
set -euo pipefail

echo 'initializing claude config...'
sed -i '$d' ./.claude.json
printf ',\n"projects":{\n"/mnt/share":{\n"hasTrustDialogAccepted":true\n}\n},\n"hasCompletedOnboarding":true}' >> ./.claude.json
echo 'claude config initiated'

echo 'referencing workspace'
cd /mnt/share
echo 'workspace is ready for action!'

echo 'starting claude'
ttyd --port 8080 --max-clients 1 --once --exit-no-conn --writable ~/.local/bin/claude --add-dir ~/instruct --settings ~/.claude/settings.json
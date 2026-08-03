#!/bin/bash
set -e

echo 'installing graphify...'
~/.local/bin/graphify install
~/.local/bin/graphify claude install
rm -f ~/CLAUDE.md
echo 'graphify installed'

echo 'initializing workspace'
cd /mnt/share
rm -rf /mnt/share/graphify-out
set +e
~/.local/bin/graphify extract . --code-only
~/.local/bin/graphify update
set -e

echo 'initializing watch service...'
python3 -u ~/watch.py 2>&1 &
echo 'watch service is ready'

cd ~
./start.sh
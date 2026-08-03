from pathlib import Path
from datetime import datetime
from os import environ
from subprocess import run
from time import sleep

def log(message):
  print(f'[{datetime.now()}] W: {message}')

def reg(path: Path):
  entries = path.rglob('*')
  hash = {}
  for entry in entries:
    try:
      hash[str(entry)] = entry.stat().st_mtime
    except:
      pass
  return hash


interval = int(environ.get('CASING_WATCH_INTERVAL', '30'))
change_threshold = float(environ.get('CASING_WATCH_CHANGE_THRESHOLD', '50')) / 100
root = Path('/mnt/share')
source = reg(root)

while True:
  sleep(interval)
  diff = 0
  target = reg(root)
  
  for path, ts in source.items():
    if not path in target or ts != target[path]:
      diff += 1

  for path in target.keys():
    if not path in source:
      diff += 1


  diff_volume = diff / (len(source) + len(target)) / 2
  log(f'total changes amount: {diff}, changes overall volume: {round(diff_volume, 2)}, max changes threshold: {change_threshold}')

  if diff_volume > change_threshold:
    source = target
    log('updating local graph...')
    output = run('~/.local/bin/graphify update', shell=True, capture_output=True, text=True)
    log('update completed')
    log(output)
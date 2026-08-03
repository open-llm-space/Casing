from urllib.request import urlopen, Request
import json
import re
import sys

workdir = '/home/claudeusr'

def parse(md):
  pattern = r"```json\s*(.*?)\s*```"
  match = re.search(pattern, md, re.DOTALL)
  if match:
    try:
      return json.loads(match.group(1))
    except:
      pass
  return None

try:
  hook = json.load(sys.stdin)
  prompt = hook.get('prompt', '')
  start = prompt.strip()[0]

  if hook.get('toolCall', hook.get('isSkill', False)) or start == '/' or start == '!':
    sys.exit(0)


  with open(f'{workdir}/.claude/settings.validations.json', 'r', encoding='utf-8') as file:
    config = json.loads(file.read())

  with open(f'{workdir}/instruct/CLAUDE.md', 'r', encoding='utf-8') as file:
    ctx = file.read()

  with open(f'{workdir}/instruct/.claude/hooks/force-prompt-validation/instruct.md', 'r', encoding='utf-8') as file:
    instructions = file.read()

  service = config.get('env', {}).get('ANTHROPIC_BASE_URL')
  url = f'{service}/api/generate'
  method = 'POST'
  model = config.get('model')

  payload = {
    'model': model,
    'prompt': f'Context:\n{ctx}\n\n\n{instructions}\n\n{prompt}',
    'stream': False,
    'think': False
  }

  req = Request(
    url, 
    data=json.dumps(payload).encode('utf-8'), 
    headers={'Content-Type': 'application/json'},
    method=method
  )

  with urlopen(req) as response:
    result = json.loads(response.read().decode('utf-8'))['response']
    verdict = parse(result)
    if verdict and verdict.get('allow'):
      sys.exit(0)
    else:
      print(f'{method} {url} (via `{model}` model)', file=sys.stderr)
      reason = verdict['block'] if verdict else result
      print(f'\n{reason}', file=sys.stderr)
      sys.exit(2)
except Exception as error:
  print(f'Hook failure: {error}', file=sys.stderr)
  sys.exit(1)
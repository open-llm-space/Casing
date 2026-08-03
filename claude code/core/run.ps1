param (
  [string]$port = "8080"
)

Invoke-Expression "ttyd --port $($port) --max-clients 1 --once --exit-no-conn --writable claude --add-dir ./setup/instruct --settings ./.claude/settings.json";
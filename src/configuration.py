import json
from types import SimpleNamespace

file = open("config.json")
content = file.read()
config = json.loads(content, object_hook=lambda d: SimpleNamespace(**d))

## Twitter MCP Client

1. Go to RapidAPI.com, get your api key and enable the api  https://rapidapi.com/alexanderxbx/api/twitter-api45 
2. Update the claude_desktop_config.json with the following details , 
```
"mcp-x": {
      "command": "uv", 
      "args": [
        "--directory",
        "PATH TO REPOSITORY",
        "run",
        "main.py"
      ],
      "env":{
        "RAPID_API_KEY": "XXXXXXXXXXXXXXXX"
      }
    }
```


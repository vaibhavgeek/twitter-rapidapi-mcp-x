## Twitter MCP Client

[![smithery badge](https://smithery.ai/badge/@vaibhavgeek/twitter-rapidapi-mcp-x)](https://smithery.ai/server/@vaibhavgeek/twitter-rapidapi-mcp-x)

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

### Installing via Smithery

To install twitter-rapidapi-mcp-x for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@vaibhavgeek/twitter-rapidapi-mcp-x):

```bash
npx -y @smithery/cli install @vaibhavgeek/twitter-rapidapi-mcp-x --client claude
```


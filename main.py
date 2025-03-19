import httpx
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP
import os


# Initialize FastMCP server
mcp = FastMCP("mcp-x")
RAPID_API_KEY = os.getenv('RAPID_API_KEY')

async def get_twitter_profile(screenname: str, rest_id: str = None) -> Dict[str, Any]:
    """
    Function to get Twitter profile information using the RapidAPI Twitter API.
    
    Args:
        screenname (str): Twitter username without the @ symbol
        rest_id (str, optional): Twitter user's rest_id if known
    
    Returns:
        Dict[str, Any]: Profile information
    """
    url = f"https://twitter-api45.p.rapidapi.com/timeline.php"
    
    params = {"screenname": screenname}
    if rest_id:
        params["rest_id"] = rest_id
        
    headers = {
        "x-rapidapi-host": "twitter-api45.p.rapidapi.com",
        "x-rapidapi-key": RAPID_API_KEY
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": f"Failed to fetch profile: {response.text}"
            }

@mcp.tool()
async def get_tweets_from_profiles(profiles: List[str]) -> Dict[str, Any]:
    """
    Get tweets from multiple Twitter profiles.
    
    Args:
        profiles (List[str]): List of Twitter usernames without the @ symbol
    
    Returns:
        Dict[str, Any]: Dictionary containing profile information for each username
    """
    results = {}
    
    for profile in profiles:
        profile_data = await get_twitter_profile(profile)
        results[profile] = profile_data
    
    return results

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
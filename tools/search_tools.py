import json
import os

import requests
from crewai.tools import tool


class SearchTools:
    @staticmethod
    @tool("Search the internet for information")
    def search_internet(query: str) -> str:
        """Search the internet for information.
        
        Args:
            query: The search query to look up
            
        Returns:
            str: Search results for the query
        """
        return f"Search results for: {query}"
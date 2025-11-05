"""
Web Search Agent using OpenAI Agents SDK

This module implements an AI agent that:
1. Takes a user query
2. Generates 2 optimized search queries
3. Provides reasoning for each query
4. Performs web searches using the generated queries
"""

from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv(override=True)


class WebSearchQueryGenerator:
    """
    An AI agent that generates multiple search queries from a user input
    and performs web searches using the OpenAI Agents SDK.
    """

    def __init__(self):
        """Initialize the WebSearchQueryGenerator with OpenAI client."""
        self.client = OpenAI()

    def generate_search_queries(self, user_query: str) -> dict:
        """
        Generate 2 optimized search queries from the user input with reasoning.

        Args:
            user_query: The original query from the user

        Returns:
            dict: Contains 2 search queries with their reasoning
        """

        system_prompt = """You are a search query optimization expert. Your task is to take a user's query
and generate 2 different but related search queries that will help find comprehensive information.

For each query you generate, provide:
1. The optimized search query
2. A clear reason why this query variation would be useful

Consider these strategies:
- Query 1: Broaden or rephrase the original query to capture more general information
- Query 2: Add specific keywords or constraints to find more detailed/technical information

Respond in JSON format:
{
    "query_1": {
        "query": "the first search query",
        "reason": "explanation of why this query is useful"
    },
    "query_2": {
        "query": "the second search query",
        "reason": "explanation of why this query is useful"
    }
}"""

        user_prompt = f"Original query: {user_query}\n\nGenerate 2 optimized search queries with reasoning."

        # Use OpenAI API to generate the search queries
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}
        )

        # Parse the response
        result = json.loads(response.choices[0].message.content)
        return result

    def perform_web_search(self, query: str) -> str:
        """
        Perform a web search using the generated query.

        Note: This uses OpenAI's function calling to simulate web search.
        For actual web search, you would integrate with a real search API.

        Args:
            query: The search query to execute

        Returns:
            str: Search results or placeholder
        """
        # Define the web search tool
        web_search_tool = {
            "type": "function",
            "function": {
                "name": "web_search",
                "description": "Performs a web search and returns relevant results",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query to execute"
                        }
                    },
                    "required": ["query"]
                }
            }
        }

        # Simulate web search using OpenAI
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that performs web searches."},
                {"role": "user", "content": f"Search for: {query}"}
            ],
            tools=[web_search_tool]
        )

        return f"Web search executed for: {query}"

    def run(self, user_query: str, execute_searches: bool = False) -> dict:
        """
        Main method to run the web search agent.

        Args:
            user_query: The original query from the user
            execute_searches: Whether to actually execute the searches (default: False)

        Returns:
            dict: Complete results including queries, reasoning, and search results
        """
        print(f"\n{'='*60}")
        print(f"Original Query: {user_query}")
        print(f"{'='*60}\n")

        # Generate the search queries
        queries = self.generate_search_queries(user_query)

        # Display the generated queries and reasoning
        print("Generated Search Queries:\n")

        for i, (key, value) in enumerate(queries.items(), 1):
            print(f"Query {i}:")
            print(f"  Search Query: {value['query']}")
            print(f"  Reason: {value['reason']}")
            print()

        # Optionally execute the searches
        results = {
            "original_query": user_query,
            "generated_queries": queries
        }

        if execute_searches:
            print("Executing searches...\n")
            search_results = {}

            for key, value in queries.items():
                search_query = value['query']
                result = self.perform_web_search(search_query)
                search_results[key] = result
                print(f"✓ {result}")

            results["search_results"] = search_results
            print()

        print(f"{'='*60}\n")
        return results


def main():
    """
    Example usage of the WebSearchQueryGenerator agent.
    """
    # Initialize the agent
    agent = WebSearchQueryGenerator()

    # Example queries to test
    test_queries = [
        "How to implement machine learning in Python",
        "Best practices for REST API design",
        "Climate change effects on agriculture"
    ]

    # Run the agent for each test query
    for query in test_queries:
        result = agent.run(query, execute_searches=True)

        # You can also access the results programmatically
        # print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

"""
Advanced Web Search Agent using OpenAI Agents SDK

This module demonstrates the use of the OpenAI Agents SDK to create an intelligent
agent that generates multiple search queries and performs web searches.

Requirements:
    - openai-agents
    - openai
    - python-dotenv
"""

try:
    from agents import Agent, WebSearchTool, trace, Runner
    AGENTS_SDK_AVAILABLE = True
except ImportError:
    print("Warning: openai-agents SDK not fully available. Using fallback implementation.")
    AGENTS_SDK_AVAILABLE = False

from openai import OpenAI
from dotenv import load_dotenv
import json
from typing import Dict, List

# Load environment variables
load_dotenv(override=True)


class IntelligentWebSearchAgent:
    """
    An intelligent AI agent that uses the OpenAI Agents SDK to:
    1. Analyze user queries
    2. Generate multiple optimized search queries
    3. Provide detailed reasoning for each query
    4. Execute web searches if requested
    """

    def __init__(self):
        """Initialize the agent with OpenAI client and tools."""
        self.client = OpenAI()
        self.agent = None

        if AGENTS_SDK_AVAILABLE:
            self._initialize_agent_sdk()
        else:
            print("Using standard OpenAI API implementation")

    def _initialize_agent_sdk(self):
        """Initialize the OpenAI Agents SDK components."""
        try:
            # Initialize the web search tool
            web_search_tool = WebSearchTool()

            # Create the agent with web search capabilities
            self.agent = Agent(
                name="WebSearchQueryAgent",
                instructions="""You are an expert at generating optimized search queries.
                When given a user query, you should:
                1. Generate 2 different but complementary search queries
                2. Provide clear reasoning for why each query would be useful
                3. Consider different aspects: broad vs specific, general vs technical
                """,
                tools=[web_search_tool],
                model="gpt-4o-mini"
            )
            print("✓ OpenAI Agents SDK initialized successfully")
        except Exception as e:
            print(f"Could not initialize Agents SDK: {e}")
            self.agent = None

    def generate_queries_with_reasoning(self, user_query: str) -> Dict:
        """
        Generate 2 optimized search queries with detailed reasoning.

        Args:
            user_query: The original user query

        Returns:
            Dict containing the generated queries and their reasoning
        """

        system_prompt = """You are a search query optimization expert.

Your task: Given a user query, generate exactly 2 different search queries that will help find comprehensive information.

Strategy for Query 1 - BROAD APPROACH:
- Rephrase to capture general/overview information
- Use synonyms or related terms
- Aim for comprehensive, foundational results
- Include context that broadens the scope

Strategy for Query 2 - SPECIFIC/TECHNICAL APPROACH:
- Add specific keywords, technical terms, or constraints
- Target detailed, in-depth information
- Include year/version/platform specifics if relevant
- Focus on practical implementation or advanced aspects

For each query provide:
1. The optimized search query (clear and concise)
2. A specific reason explaining why this query variation will yield useful results

Output format (JSON):
{
    "query_1": {
        "query": "the first search query",
        "reason": "detailed explanation of why this specific query wording will help find [specific type of information]"
    },
    "query_2": {
        "query": "the second search query",
        "reason": "detailed explanation of why this query variation targets [different aspect or detail level]"
    }
}"""

        user_prompt = f"""Original user query: "{user_query}"

Please generate 2 optimized search queries with detailed reasoning."""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result

    def execute_search_with_agent(self, query: str) -> str:
        """
        Execute a web search using the OpenAI Agents SDK.

        Args:
            query: The search query to execute

        Returns:
            str: Search results from the agent
        """
        if not AGENTS_SDK_AVAILABLE or self.agent is None:
            return f"[Simulated search for: {query}]"

        try:
            # Use the Runner to execute the agent with the search query
            runner = Runner(self.agent)
            result = runner.run(f"Search for: {query}")
            return result
        except Exception as e:
            return f"Search execution failed: {str(e)}"

    def run(self, user_query: str, execute_searches: bool = False) -> Dict:
        """
        Main execution method for the web search agent.

        Args:
            user_query: The original query from the user
            execute_searches: Whether to execute actual searches (requires Agents SDK)

        Returns:
            Dict: Complete results including queries, reasoning, and optional search results
        """

        print(f"\n{'='*70}")
        print(f"🔍 Web Search Agent - Query Analysis")
        print(f"{'='*70}")
        print(f"\nOriginal Query: \"{user_query}\"")
        print(f"\n{'='*70}\n")

        # Generate optimized queries
        queries = self.generate_queries_with_reasoning(user_query)

        # Display results
        print("📋 Generated Search Queries:\n")

        for i, (key, value) in enumerate(queries.items(), 1):
            print(f"Query {i} - {'BROAD APPROACH' if i == 1 else 'SPECIFIC/TECHNICAL APPROACH'}:")
            print(f"  🔎 Search Query: \"{value['query']}\"")
            print(f"  💡 Reason: {value['reason']}")
            print()

        # Prepare results
        results = {
            "original_query": user_query,
            "generated_queries": queries,
            "search_executed": execute_searches
        }

        # Execute searches if requested
        if execute_searches:
            print(f"{'='*70}")
            print("🌐 Executing Web Searches...")
            print(f"{'='*70}\n")

            search_results = {}
            for i, (key, value) in enumerate(queries.items(), 1):
                search_query = value['query']
                print(f"Searching with Query {i}...")
                result = self.execute_search_with_agent(search_query)
                search_results[key] = result
                print(f"✓ Completed: {search_query}\n")

            results["search_results"] = search_results

        print(f"{'='*70}\n")

        return results

    def interactive_mode(self):
        """
        Run the agent in interactive mode, allowing users to input queries.
        """
        print("\n" + "="*70)
        print("🤖 Interactive Web Search Query Generator")
        print("="*70)
        print("\nThis agent will generate 2 optimized search queries for your input.")
        print("Type 'quit' or 'exit' to stop.\n")

        while True:
            try:
                user_input = input("Enter your query: ").strip()

                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Goodbye!\n")
                    break

                if not user_input:
                    print("Please enter a valid query.\n")
                    continue

                # Run the agent
                execute = input("Execute web searches? (y/n): ").strip().lower() == 'y'
                self.run(user_input, execute_searches=execute)

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")


def demo_examples():
    """
    Demonstrate the agent with example queries.
    """
    agent = IntelligentWebSearchAgent()

    # Example queries showcasing different types of searches
    example_queries = [
        "How to implement machine learning in Python",
        "Best practices for REST API design",
        "What are the latest trends in quantum computing",
        "How to optimize SQL database performance",
        "Climate change impact on ocean ecosystems"
    ]

    print("\n" + "="*70)
    print("🚀 Web Search Agent Demo - Example Queries")
    print("="*70 + "\n")

    for i, query in enumerate(example_queries, 1):
        print(f"\n{'#'*70}")
        print(f"# Example {i} of {len(example_queries)}")
        print(f"{'#'*70}\n")

        result = agent.run(query, execute_searches=False)

        # Optional: Save results to a file
        # with open(f"search_results_{i}.json", "w") as f:
        #     json.dump(result, f, indent=2)

        if i < len(example_queries):
            input("Press Enter to continue to next example...")

    print("\n✅ Demo completed!\n")


def main():
    """
    Main entry point for the web search agent.
    """
    import sys

    if len(sys.argv) > 1:
        # Use command line argument as query
        query = " ".join(sys.argv[1:])
        agent = IntelligentWebSearchAgent()
        agent.run(query, execute_searches=True)
    else:
        # Show menu
        print("\nWeb Search Agent Options:")
        print("1. Run demo with example queries")
        print("2. Interactive mode")
        print("3. Quick test with default query")

        choice = input("\nSelect option (1-3): ").strip()

        if choice == "1":
            demo_examples()
        elif choice == "2":
            agent = IntelligentWebSearchAgent()
            agent.interactive_mode()
        else:
            # Quick test
            agent = IntelligentWebSearchAgent()
            agent.run("How to build a chatbot with Python", execute_searches=False)


if __name__ == "__main__":
    main()

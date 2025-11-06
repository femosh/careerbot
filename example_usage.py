"""
Example Usage of Web Search Agents

This file demonstrates how to use the web search query generation agents.
"""

from websearch_agent import WebSearchQueryGenerator
from websearch_agent_advanced import IntelligentWebSearchAgent
import json


def basic_example():
    """
    Example using the basic WebSearchQueryGenerator
    """
    print("\n" + "="*70)
    print("BASIC WEB SEARCH AGENT EXAMPLE")
    print("="*70 + "\n")

    # Initialize the agent
    agent = WebSearchQueryGenerator()

    # Example query
    query = "How to deploy a machine learning model to production"

    # Run the agent
    result = agent.run(query, execute_searches=False)

    # Access the generated queries programmatically
    print("\nProgrammatic Access to Results:")
    print(json.dumps(result, indent=2))


def advanced_example():
    """
    Example using the advanced IntelligentWebSearchAgent
    """
    print("\n" + "="*70)
    print("ADVANCED WEB SEARCH AGENT EXAMPLE")
    print("="*70 + "\n")

    # Initialize the advanced agent
    agent = IntelligentWebSearchAgent()

    # Example query
    query = "Best practices for microservices architecture"

    # Run the agent
    result = agent.run(query, execute_searches=False)

    # Process the results
    print("\n📊 Result Summary:")
    print(f"Original Query: {result['original_query']}")
    print(f"Number of Generated Queries: {len(result['generated_queries'])}")

    for key, value in result['generated_queries'].items():
        print(f"\n{key}:")
        print(f"  Query: {value['query']}")
        print(f"  Reason: {value['reason'][:100]}...")


def compare_queries_example():
    """
    Example showing how different queries generate different search strategies
    """
    print("\n" + "="*70)
    print("COMPARING DIFFERENT QUERY TYPES")
    print("="*70 + "\n")

    agent = IntelligentWebSearchAgent()

    test_queries = [
        "Python web frameworks",
        "How to secure a REST API",
        "Docker vs Kubernetes comparison"
    ]

    for query in test_queries:
        print(f"\n{'─'*70}")
        print(f"Testing: {query}")
        print(f"{'─'*70}")

        result = agent.run(query, execute_searches=False)

        # Show the queries generated
        for i, (key, value) in enumerate(result['generated_queries'].items(), 1):
            print(f"\n  Generated Query {i}: {value['query']}")


def custom_query_example():
    """
    Example allowing user to input their own query
    """
    print("\n" + "="*70)
    print("CUSTOM QUERY EXAMPLE")
    print("="*70 + "\n")

    # Get user input
    user_query = input("Enter your search query: ").strip()

    if not user_query:
        print("No query provided. Using default query.")
        user_query = "artificial intelligence applications in healthcare"

    # Initialize agent
    agent = IntelligentWebSearchAgent()

    # Run with user's query
    result = agent.run(user_query, execute_searches=False)

    # Save to file
    output_file = "query_results.json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\n✅ Results saved to: {output_file}")


def main():
    """
    Main function to run all examples
    """
    print("\n" + "="*70)
    print("🚀 WEB SEARCH AGENT EXAMPLES")
    print("="*70)

    examples = {
        "1": ("Basic Agent Example", basic_example),
        "2": ("Advanced Agent Example", advanced_example),
        "3": ("Compare Different Queries", compare_queries_example),
        "4": ("Custom Query", custom_query_example),
        "5": ("Run All Examples", None)
    }

    print("\nAvailable Examples:")
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")

    choice = input("\nSelect an example (1-5) or press Enter for all: ").strip()

    if choice == "5" or not choice:
        # Run all examples
        basic_example()
        input("\nPress Enter to continue...")
        advanced_example()
        input("\nPress Enter to continue...")
        compare_queries_example()
        input("\nPress Enter to continue...")
        custom_query_example()
    elif choice in examples and examples[choice][1]:
        examples[choice][1]()
    else:
        print("Invalid choice. Running basic example.")
        basic_example()

    print("\n✅ Examples completed!\n")


if __name__ == "__main__":
    main()

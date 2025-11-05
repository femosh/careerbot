# Web Search Query Generation Agent

## Overview

This project implements an AI agent that generates multiple optimized search queries from a single user input using the OpenAI API and OpenAI Agents SDK. The agent analyzes the user's query and creates 2 different but complementary search queries, each with detailed reasoning.

## Features

✨ **Smart Query Generation**: Automatically generates 2 optimized search queries from any input
🧠 **Reasoning Explanation**: Provides detailed explanations for why each query variation is useful
🔍 **Dual Strategy Approach**:
- Query 1: Broad/general approach for comprehensive information
- Query 2: Specific/technical approach for detailed information
🛠️ **Multiple Implementations**:
- Basic version using OpenAI API
- Advanced version using OpenAI Agents SDK

## Files

```
websearch_agent.py              # Basic implementation
websearch_agent_advanced.py     # Advanced implementation with Agents SDK
example_usage.py                # Example usage and demonstrations
WEBSEARCH_AGENT_README.md       # This file
```

## Requirements

```bash
pip install openai openai-agents python-dotenv
```

Make sure you have a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```python
from websearch_agent import WebSearchQueryGenerator

# Initialize the agent
agent = WebSearchQueryGenerator()

# Generate queries
result = agent.run("How to implement machine learning in Python")
```

### Advanced Usage

```python
from websearch_agent_advanced import IntelligentWebSearchAgent

# Initialize the advanced agent
agent = IntelligentWebSearchAgent()

# Generate queries with detailed reasoning
result = agent.run("Best practices for REST API design", execute_searches=False)

# Access results
print(result['generated_queries'])
```

### Command Line Usage

Run the advanced agent directly from command line:

```bash
# Interactive mode
python websearch_agent_advanced.py

# Direct query
python websearch_agent_advanced.py "your search query here"

# Run examples
python example_usage.py
```

## How It Works

### Query Generation Strategy

The agent uses two complementary strategies:

**Query 1 - Broad Approach:**
- Rephrases to capture general/overview information
- Uses synonyms or related terms
- Aims for comprehensive, foundational results
- Includes context that broadens the scope

**Query 2 - Specific/Technical Approach:**
- Adds specific keywords, technical terms, or constraints
- Targets detailed, in-depth information
- Includes year/version/platform specifics if relevant
- Focuses on practical implementation or advanced aspects

### Example Output

**Input Query:** "How to implement machine learning in Python"

**Generated Queries:**

1. **Broad Approach:**
   - Query: "Python machine learning tutorial for beginners overview"
   - Reason: This query targets introductory and comprehensive guides that provide foundational knowledge about implementing ML in Python, making it ideal for understanding the basics and available frameworks.

2. **Specific/Technical Approach:**
   - Query: "Python machine learning implementation scikit-learn tensorflow production 2024"
   - Reason: This query focuses on specific frameworks (scikit-learn, tensorflow) and production implementation, targeting more advanced, practical resources with up-to-date information for actual deployment scenarios.

## API Reference

### WebSearchQueryGenerator

Basic implementation using standard OpenAI API.

**Methods:**
- `generate_search_queries(user_query: str) -> dict`: Generate optimized queries
- `perform_web_search(query: str) -> str`: Execute web search
- `run(user_query: str, execute_searches: bool = False) -> dict`: Main execution method

### IntelligentWebSearchAgent

Advanced implementation with OpenAI Agents SDK support.

**Methods:**
- `generate_queries_with_reasoning(user_query: str) -> Dict`: Generate queries with detailed reasoning
- `execute_search_with_agent(query: str) -> str`: Execute search using Agents SDK
- `run(user_query: str, execute_searches: bool = False) -> Dict`: Main execution method
- `interactive_mode()`: Run in interactive mode

## Response Format

Both implementations return a dictionary with the following structure:

```json
{
  "original_query": "user's input query",
  "generated_queries": {
    "query_1": {
      "query": "optimized search query 1",
      "reason": "explanation for query 1"
    },
    "query_2": {
      "query": "optimized search query 2",
      "reason": "explanation for query 2"
    }
  },
  "search_executed": false,
  "search_results": {}  // Only if execute_searches=True
}
```

## Examples

See `example_usage.py` for comprehensive examples including:
- Basic usage
- Advanced usage
- Comparing different query types
- Custom query input
- Programmatic access to results

Run examples:
```bash
python example_usage.py
```

## Benefits of Multiple Queries

1. **Comprehensive Coverage**: Different query formulations capture different aspects of the topic
2. **Redundancy**: If one query doesn't yield good results, the other might
3. **Breadth vs Depth**: Balances between overview and detailed information
4. **Perspective Variety**: Different phrasings may surface different types of sources

## Use Cases

- 📚 Research: Find both overview and detailed information on topics
- 🔬 Technical Documentation: Get both beginner and advanced resources
- 📰 News Search: Find both general coverage and specific details
- 🎓 Learning: Access both introductory and in-depth materials
- 💼 Business Intelligence: Gather both market overviews and specific data

## Customization

You can customize the query generation by modifying the system prompt in either implementation file. The current strategies can be adjusted to fit specific use cases:

- Academic research
- Product searches
- News and current events
- Technical documentation
- Code examples

## Limitations

- Requires OpenAI API key
- API usage costs apply
- Web search execution requires additional configuration or Agents SDK
- Quality depends on the OpenAI model's understanding

## Future Enhancements

- [ ] Integration with actual web search APIs (Google, Bing, DuckDuckGo)
- [ ] Support for more than 2 queries
- [ ] Query optimization based on search results
- [ ] Caching of generated queries
- [ ] Multi-language support
- [ ] Domain-specific query strategies

## License

MIT License

## Contributing

Feel free to submit issues and enhancement requests!

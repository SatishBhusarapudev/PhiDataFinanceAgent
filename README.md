# PhidataFinanceAgent

The `PhidataFinanceAgent` project is designed to leverage AI agents for retrieving and processing financial data, as well as performing web-based searches. The project uses the `phi` library to define and manage agents with specific roles and tools.

## Project Structure

The project consists of the following files:

- **`.env`**: Contains API keys for Groq and OpenAI.
- **`agentteams.py`**: Defines a team of agents, including a web agent and a finance agent, to collaboratively process tasks.
- **`financeAgent.py`**: Implements a finance-focused agent with tools for retrieving stock data and company symbols.
- **`simple_grog_agent.py`**: Demonstrates a simple agent setup for summarizing and comparing financial data.
- **`main.py`**: Placeholder file for potential future functionality.

## Agents Overview

### Web Agent
Defined in [`agentteams.py`](agentteams.py), the Web Agent is responsible for performing web searches using the DuckDuckGo tool.

- **Model**: `Groq(id="llama-3.3-70b-versatile")`
- **Tools**: `DuckDuckGo`
- **Instructions**: Always include sources.
- **Features**:
  - Displays results in Markdown format.
  - Shows tool calls for debugging.

### Finance Agent
Defined in both [`agentteams.py`](agentteams.py) and [`financeAgent.py`](financeAgent.py), the Finance Agent is specialized in retrieving and summarizing financial data.

- **Model**: `Groq(id="llama-3.3-70b-versatile")`
- **Tools**:
  - `YFinanceTools` for stock prices, analyst recommendations, and company information.
  - `get_company_symbol` function for resolving company names to stock symbols (defined in `financeAgent.py`).
- **Instructions**:
  - Use tables to display data.
  - Include sources in responses.
- **Features**:
  - Displays results in Markdown format.
  - Shows tool calls for debugging.

### Agent Team
Defined in [`agentteams.py`](agentteams.py), the Agent Team combines the Web Agent and Finance Agent to collaboratively handle tasks.

- **Model**: `Groq(id="llama-3.3-70b-versatile")`
- **Team Members**: Web Agent, Finance Agent
- **Instructions**:
  - Always include sources.
  - Use tables to display data.
- **Features**:
  - Displays results in Markdown format.
  - Shows tool calls for debugging.

## Example Usage

### Finance Agent
The Finance Agent can summarize and compare analyst recommendations and fundamentals for specific stocks. Example from [`financeAgent.py`](financeAgent.py):

```python
agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and Phidata clear. Show in tables.", stream=True
)
```

### Agent Team
The Agent Team can collaboratively summarize financial data and news. Example from [`agentteams.py`](agentteams.py):

```python
agent_team.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA", stream=True
)
```

## Environment Variables

The `.env` file contains the following keys:

- `GROQ_API_KEY`: API key for Groq.
- `OPENAI_API_KEY`: API key for OpenAI.

## Dependencies

- `phi` library for agent and tool management.
- `dotenv` for loading environment variables.

## How to Run

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies.
3. Set up the `.env` file with your API keys.
4. Run the desired Python script, e.g., `agentteams.py` or `financeAgent.py`.

```bash
python agentteams.py
```

## License

This project is licensed under the MIT License.
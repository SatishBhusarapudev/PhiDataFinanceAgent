from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools 

load_dotenv()

agent =Agent( model=Groq(id="llama-3.3-70b-versatile"),
              tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
              show_tool_calls=True,
              markdown=True,
              instructions=["Please use tables to display data "]
             )

#agent.print_response("What is the most beautiful place in the world?")
agent.print_response("Summarize and compare analyst recommendations for TSLA and NVDA");

from deepagents import create_deep_agent

from llm import deepseek_chat_model
from search.tavily_client import internet_search

research_instructions = """
You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

internet_search_agent = create_deep_agent(
    model=deepseek_chat_model,
    tools=[internet_search],
    system_prompt=research_instructions
)

from agent.internet_search_agent import internet_search_agent

if __name__ == '__main__':
    result = internet_search_agent.invoke({
        "messages": [
            {"role": "user", "content": "What is deepagents?"}
        ]
    })

    # Print the agent's response
    print(result["messages"][-1].content)

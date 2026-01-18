from agent.internet_search_agent import internet_search_agent

if __name__ == '__main__':
    inputs = {
        "messages": [
            {"role": "user", "content": "What is deepagents?"}
        ]
    }

    for chunk in internet_search_agent.stream(inputs, stream_mode="values"):
        if "messages" in chunk:
            msg = chunk["messages"][-1]
            if msg.content:
                print(msg.type + ": " + msg.content, end="\n\n", flush=True)

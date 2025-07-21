from langchain.llms import OpenAI
from langchain.agents import initialize_agent

llm = OpenAI(temperature=0)

# Define tool
sentiment_tool = Tool(
    name="SentimentClassifier",
    func=classify_sentiment,
    description="Use this tool to detect sentiment in user input. Input should be a short sentence."
)

# Initialize agent
agent = initialize_agent(
    tools=[sentiment_tool],
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=True
)

# Run agent
agent.run("Classify the sentiment of this review: This product is amazing and exceeded expectations!")

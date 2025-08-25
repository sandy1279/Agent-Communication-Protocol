from collections.abc import AsyncGenerator
from acp_sdk.models import Message, MessagePart
from acp_sdk.server import RunYield, RunYieldResume, Server
from crewai import Crew, Task, Agent, LLM
from smolagents import DuckDuckGoSearchTool

server = Server()

llm = LLM(
    model="ollama_chat/tinyllama:1.1b-chat",
    base_url="http://localhost:11434",
    max_tokens=5000
)



@server.agent()
async def research_verifier(input: list[Message]) -> AsyncGenerator[RunYield, RunYieldResume]:
    """Agent that fact-checks and enhances a research summary using web search."""

    agent = Agent(
        role="Research Verifier",
        goal="Fact-check and enhance research summaries using reliable sources",
        backstory="You are a fact-checker and verifier who validates research with supporting evidence from the web.",
        llm=llm,
        tools=[DuckDuckGoSearchTool()]  # ✅ integrated search tool
    )

    task = Task(
        description=f"Fact-check and improve this summary: {input[0].parts[0].content}",
        expected_output="A corrected and enhanced summary with references or validation notes.",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task])
    task_output = await crew.kickoff_async()

    yield Message(parts=[MessagePart(content=str(task_output))])

if __name__ == "__main__":
    server.run(port=8001)

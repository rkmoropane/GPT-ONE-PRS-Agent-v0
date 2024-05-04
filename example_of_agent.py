# Standard library imports
import os

# Related third party imports
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI # a great way to connect to multiple large languagle models' tools


# Get all your secret environment variables
class Config:
    MODEL=os.environ.get("OPENAI_API_KEY", "gpt-3.5-turbo-0125")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    SERPER_API_KEY = os.environ.get("SERPER_API_KEY")

# assign the SerperDevTool to a defined variable search_tool
google_search_tools = SerperDevTool()

# let's get all environment vars
config = Config()
# define our agents with roles and goals
researcher = Agent(
    role="Senior Research Assistant",
    goal="Look up the latest Advancement in AI Agents",
    backstory="""You work at a leading tech think tank.
            Your expertise lies in identifying emerging trends.
            You have a knack for dissecting complex data and presenting actionable insights.
        """, # system prompt or system instruction,
    verbose=False, # this is whether you want to your response to be verbose (long detailed or short detailed)  
    allow_delegation=False, # we don't want the task to be delegated to another agent.
    tools=[google_search_tools],
    llm=ChatOpenAI(model_name=config.MODEL, temperature=0.3) # low the temperature, the more consistent it is, but less creative it is - more accurate to the search results it gets keep it low.
)

writer = Agent(
    role="Senior Short-Article Writer",
    goal="Summarize the latest Advancement in AI Agents in a concise article.",
    backstory="""You are a renowned content strategist, known for your insightful and engaging article.
            You transform complex concepts into compelling narratives.
        """, # system prompt or system instruction,
    verbose=True, # this is whether you want to your response to be verbose (long detailed or short detailed)  
    allow_delegation=True, # we want the task to be delegated to another agent.
    llm=ChatOpenAI(model_name=config.MODEL, temperature=0.7) # let's get more creative.
)

# Let's give our agent a task, because without it, it cannot do anything.
task1 = Task(
    description="""Conduct a comprehensive analysis of the latest advancements in AI Agents in April.
    Identify key trends, breakthrough technologies, and potential industry impacts.""",
    expected_output="Full analysis report in bullet points",
    agent=researcher
)

task2 = Task(
    description="""Using the insights provided, write a short article that 
    highlights the most significant AI agent advancements.
    Your post should be informative yet accessible, catering to a tech-savvy audience.
    Make it sound cool, avoid complex words so it doesn't sound like AI.""",
    expected_output="Full blog post of at least 4 paragraphs",
    agent=writer
)

crew = Crew(
    agents=[researcher, writer],
    tasks = [task1, task2],
    verbose=2, # You can set it to 1 or 2 to different logging levels
)

results = crew.kickoff()
print(type(researcher), type(writer), type(task1), type(crew))
print("###########")
print(results)
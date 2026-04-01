# this is for puting tools here and we can use main.py for main logic

#Tools are things that the LLM/agent can use that we can either write ourself or we can brint it
# from things like the langchain community Hub

#we are using three toools all are free no need for api key

#-----------------------------------------------------------------------------------

# WikipediaQueryRun ->A tool class that lets your AI agent search Wikipedia.
# 👉 Purpose:
# Sends a query to Wikipedia
# Fetches summary/info
# Returns it as text for the LLM

# DuckDuckGoSearchRun ->A web search tool using DuckDuckGo search engine.
# 👉 Purpose:
# Searches internet content
# Returns search snippets/

# WikipediaAPIWrapper->A utility wrapper for Wikipedia API.


# Think of it as:
# 👉 Backend connection to Wikipedia.

# 👉 Purpose:
# Handles API calls
# Formats Wikipedia results
# Cleans returned data

# When did we actually make an API call? I don’t see any API call code.”

# 👉 That’s because LangChain hides it internally.
# ✅ Where API call actually happens

# When you do:
# wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
# wiki.run("Python programming")

# 👉 The API call happens inside:
# WikipediaAPIWrapper → internally calls Wikipedia API.

# Tool->A generic LangChain class to create custom tools for AI agents.
# 👉 Purpose:
# Lets you define:
# Tool name
# Function it runs
# Description (important for agent reasoning)
#-----------------------------------------------------------------------------



from langchain_community.tools import WikipediaQueryRun,DuckDuckGoSearchRun 
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

# 👉 AI can ONLY use the tools you give it.
#first tool->search tool
search=DuckDuckGoSearchRun() #search is an obj of DDSR and now it can run use att and method
search_tool=Tool(
    name="search",
    func=search.run,
    description="Search the wen for imformation"
)#search_tool is an obj of Tool and now it can run use att and method


#sec tool->wikipedia tool

api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=100)
# top_k_results= how manu results you want back
# dco_content_chars_max=max character you want back
wiki_tool=WikipediaQueryRun(api_wrapper=api_wrapper)

#making own custom tool
# creatin a fucntion to be a custom tool 

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"\n--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"

save_tool=Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Save structured reseach data to a text file.",
)

#you have to tel the ai , in query to save it , if not it will think no need to use to use the save tool, it must think it is required to
# use this tool and dont tell langchin to call the function

#After knowing what does this tool do ai tell the langchiant to run this tool when needed .. 

#------------------------------------------------------------------------------------------------------------------------------
# ✅ What actually happens
# 1️⃣ AI generates structured output

# Example:
# Tool: Search
# Input: "black and white animals"

# This comes from the LLM response format (function calling / tool calling).

# 2️⃣ LangChain reads that output
# LangChain checks:
# 👉 “AI wants to use Search tool.”

# So it triggers:
# search_tool.run("black and white animals")

# 3️⃣ Tool executes
# Your function runs.
# Returns data.

#------------------------------------------------------------------------------------------------------------
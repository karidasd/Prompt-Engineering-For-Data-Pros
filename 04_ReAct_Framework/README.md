# 04: ReAct Framework (Reasoning + Acting) 🤖

## 🇬🇧 Theory (Θεωρία)

What happens when an LLM needs to interact with the outside world? An LLM alone is just a text generator. It cannot execute code, query a database, or search the web by default.

The **ReAct (Reason + Act)** framework bridges this gap. It's the core logic behind modern AI Agents (like LangChain or AutoGPT). In ReAct, the model works in a loop:
1. **Thought:** The model reasons about what it needs to do.
2. **Action:** The model calls a specific Tool (e.g., `SearchWeb`, `RunPython`, `QuerySQL`).
3. **Observation:** The model receives the result of the tool.
*(Repeat until the goal is achieved)*

---

## 📋 The ReAct System Prompt

If you are building an AI Agent in Python, this is the core prompt you feed it:

```text
You are a Data Analyst Agent. You have access to the following tools:
- [Run_SQL]: Executes a SQL query on the 'sales' database and returns the result.
- [Python_Plot]: Takes data and generates a matplotlib chart.

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Run_SQL, Python_Plot]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!
Question: What were the total sales in Q3 2023?
Thought: 
```

---

## 🔍 Why it matters (Γιατί είναι σημαντικό)
As a modern Data Engineer, you will increasingly build "Agentic Workflows". Instead of writing hard-coded ETL pipelines, you will build Agents that can dynamically query databases, clean data, and alert you—all driven by the ReAct framework!

# 05: Code Generation and Debugging 👨‍💻

## 🇬🇧 Theory (Θεωρία)

Writing code with LLMs is the most common use case, but most developers do it wrong. They paste an error message and say "fix this", which leads to hallucinated, out-of-context fixes.

To get production-ready code, you must provide:
1. The **Environment Context** (e.g., Python version, OS).
2. The **Framework Constraints** (e.g., PySpark vs Pandas).
3. The **Full Stack Trace** (for debugging).

---

## 📋 Template 1: Generating Production Code

```text
Act as a Senior Data Engineer.
Task: Write a Python script to download a CSV from an AWS S3 bucket, rename the columns to snake_case, and upload it to a PostgreSQL database.

Environment:
- Python 3.10
- AWS SDK (boto3)
- SQLAlchemy for DB connection

Constraints:
- Do not use pandas. Use pure python generators or the `csv` module for memory efficiency.
- Include Google-style docstrings.
- Include proper logging (using the logging module, not print statements).
- Include a try-except block to catch Boto3 credentials errors.

Output only the Python code inside a markdown block.
```

---

## 📋 Template 2: The Ultimate Debugger

```text
I am encountering an error in my Airflow DAG. 

Here is my code:
[PASTE CODE HERE]

Here is the full error stack trace:
[PASTE STACK TRACE HERE]

Analyze the error step-by-step. 
1. Identify the root cause.
2. Explain WHY it happened.
3. Provide the corrected code.
```

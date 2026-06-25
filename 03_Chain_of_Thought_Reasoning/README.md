# 03: Chain of Thought Reasoning 🔗

## 🇬🇧 Theory (Θεωρία)

When humans solve a complex math problem or write a complex SQL query, they don't instantly jump to the final answer. They break it down into steps. 

Large Language Models work the same way. If you ask an LLM to generate a massive, 100-line SQL query with window functions and multiple CTEs in one go, it might hallucinate or make a logic error.

**Chain of Thought (CoT)** is a technique where you explicitly ask the model to "think step-by-step" before providing the final answer. By forcing the model to generate its intermediate reasoning, it has more "tokens" to think, leading to significantly higher accuracy in complex tasks.

---

## 📋 The CoT Prompt Template for SQL

```text
Task: Write a PostgreSQL query to find the top 3 highest-earning employees in each department, but only for departments that have more than 10 employees. 

Before writing the query, let's think step-by-step:
1. First, identify the tables and columns needed.
2. Second, think about how to filter departments with more than 10 employees.
3. Third, think about which Window Function is needed to rank employees by salary within their department.
4. Finally, construct the CTEs and the final SELECT statement.

Write down your reasoning for each step, and then provide the final SQL query.
```

---

## 💡 The "Magic" Phrase
If you are lazy and don't want to define the steps manually, simply append this magic phrase to the end of your prompt:

> **"Let's think step by step."**

Researchers found that just adding this phrase increases the model's accuracy on logic and math problems by over 40%!

# 11: LLM-as-a-Judge & Metrics ⚖️

## 🇬🇧 Theory (Θεωρία)

How do you know if your Prompt is "good"? In traditional ML, we have Accuracy, F1-Score, and RMSE. In Prompt Engineering, evaluating a text response is difficult.

The modern MLOps approach is **LLM-as-a-Judge**. You use a powerful model (like GPT-4) to grade the outputs of a cheaper/faster model (like GPT-3.5 or Llama 3) based on a strict rubric.

---

## 📋 The Grader Template

```text
You are an impartial Judge evaluating the quality of a generated SQL query.

You will be given the User's Question, the Database Schema, and the Generated SQL.

Rate the Generated SQL on a scale of 1 to 5 based on the following rubric:
1 - The SQL is completely wrong or uses non-existent tables.
2 - The SQL runs but answers the wrong question.
3 - The SQL is correct but highly inefficient.
4 - The SQL is correct and efficient, but lacks readability/formatting.
5 - Perfect SQL query.

User Question: {question}
Schema: {schema}
Generated SQL: {generated_sql}

Provide your rating in this exact JSON format:
{"score": <int>, "reasoning": "<string>"}
```

---

## 🔍 Automation
In production, you run this prompt automatically over 1,000 test cases using CI/CD pipelines. If the average score drops below 4.5, the new prompt is rejected!

# 07: Self-Reflection & Correction 🪞

## 🇬🇧 Theory (Θεωρία)

Even the best LLMs make mistakes, especially when writing complex code (like PySpark transformations or dynamic SQL). If you just copy-paste the first output, you are risking production bugs.

**Self-Reflection** is a technique where you feed the LLM's own output back into it and explicitly ask it to "Critique" its own work before giving you the final result. LLMs are surprisingly good at catching their own logical errors when explicitly asked to look for them!

---

## 📋 The Reviewer Template

Use this prompt *after* the LLM has generated some code for you:

```text
Please act as an extremely strict Senior Staff Engineer conducting a Code Review on the code you just wrote above.

Take a deep breath and review the code step-by-step for the following issues:
1. Are there any edge cases (like null values, empty lists) that will crash the code?
2. Is the time complexity optimal? (e.g., did you use nested loops instead of a hash map?)
3. Are there any potential security vulnerabilities (like SQL injection)?

Write down your critique. 
If you found any issues, rewrite the code to be perfectly robust and production-ready.
```

---

## 🔍 The "Auto-Fix" Pipeline (Για Data Engineers)
In advanced Data Engineering pipelines, we build this into a loop:
1. Agent A writes the SQL.
2. Agent B (The Reviewer) runs the Self-Reflection prompt.
3. If Agent B finds an error, Agent A rewrites it.
This drastically reduces hallucination rates in automated data pipelines!

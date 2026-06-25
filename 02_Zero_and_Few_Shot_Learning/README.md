# 02: Zero and Few-Shot Learning 🎯

## 🇬🇧 Theory (Θεωρία)

When we give a prompt to an AI without providing any examples of the expected output, we call it **Zero-Shot Prompting**. LLMs are incredibly smart and can often deduce what you want.

However, when you need data formatted in a very specific, strict way (e.g., JSON schemas, custom log formats, or specific ETL mappings), zero-shot might fail. This is where **Few-Shot Prompting** comes in.

By providing 1 to 3 examples (shots) within your prompt, you "train" the model in real-time (in-context learning) to match your exact pattern.

---

## 📋 The Few-Shot Prompt Template

```text
Task: Extract entities from the following log messages and format them as JSON.

Example 1:
Input: "2024-03-15 10:22:15 ERROR Database connection failed in module auth.py"
Output: {"date": "2024-03-15", "time": "10:22:15", "level": "ERROR", "message": "Database connection failed", "module": "auth.py"}

Example 2:
Input: "2024-03-15 10:25:00 WARN High memory usage detected on server node-01"
Output: {"date": "2024-03-15", "time": "10:25:00", "level": "WARN", "message": "High memory usage detected", "module": "server node-01"}

Now, process the following input and output ONLY the JSON:
Input: [INSERT YOUR REAL DATA HERE]
Output:
```

---

## 🔍 Why it matters for Data Pros (Γιατί είναι σημαντικό)

In Data Engineering, you often need to parse unstructured data (like raw text, emails, or logs) into structured tables. 
Instead of writing complex and fragile **Regular Expressions (Regex)**, you can pass the raw data through an LLM using a Few-Shot prompt. 

The model will learn the pattern from your examples and output perfectly structured JSON, which you can immediately load into a database or DataFrame!

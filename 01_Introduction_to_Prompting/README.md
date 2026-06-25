# 01: Introduction to Prompting 🧠

## 🇬🇧 Theory (Θεωρία)
**Prompt Engineering** is the art of communicating with Large Language Models (LLMs) to get the exact output you want. It's not just "asking questions"; it's about providing context, constraints, and specific instructions.

As a Data Professional, you must understand three key concepts:
1. **System Prompt (Role-playing):** Telling the model *who* it is (e.g., "Act as a Senior Data Engineer").
2. **Context:** Giving the model the background information it needs to solve the problem.
3. **Temperature:** A parameter (0.0 to 1.0) that controls creativity. For coding and data tasks, you usually want a low temperature (0.0 - 0.2) for deterministic, factual outputs.

---

## 💻 The Ultimate Basic Framework (Το Βασικό Πλαίσιο)

A professional prompt always follows the **CREATE** framework:
- **C**ontext: What is the background?
- **R**ole: Who is the AI?
- **E**xpectation: What exactly do you want?
- **A**ction: What should the AI do step-by-step?
- **T**one: How should it sound? (e.g., professional, concise)
- **E**xtras: Any strict constraints? (e.g., "Do not use pandas, use polars")

---

## 📋 Prompt Template (Αντιγραφή - Επικόλληση)

```text
Act as a [INSERT ROLE, e.g., Senior Data Engineer].

Context: I am working on a project where [INSERT CONTEXT, e.g., I need to extract data from a JSON API and save it to PostgreSQL].

Action: Please [INSERT ACTION, e.g., write a Python script using the 'requests' and 'psycopg2' libraries to accomplish this].

Tone: Professional, concise, and heavily commented code.

Constraints: 
- Do not use any external ORMs like SQLAlchemy.
- Handle connection errors gracefully using try-except blocks.
```

---

## 🔍 Example in Action (Παράδειγμα)

**User Prompt:**
> Act as a Senior Data Engineer. Context: I have a massive CSV file (50GB) and my machine has only 16GB of RAM. Action: Write a Python script to read this file, filter out rows where the 'status' column is 'failed', and save the result to a new CSV. Constraints: Do not use pandas. Use a memory-efficient approach like chunking or the 'csv' module directly.

**AI Output:**
The AI will output a highly optimized memory-efficient script using `pd.read_csv(chunksize=...)` or the standard `csv` library, exactly as constrained, saving you hours of StackOverflow searching!

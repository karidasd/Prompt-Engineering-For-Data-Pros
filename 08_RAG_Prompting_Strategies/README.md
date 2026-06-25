# 08: RAG Prompting Strategies 📚

## 🇬🇧 Theory (Θεωρία)

LLMs only know what they were trained on. If you ask an LLM about your company's internal HR policy or a proprietary Database Schema, it will hallucinate.

**RAG (Retrieval-Augmented Generation)** is the industry standard solution. In RAG, you first "search" a vector database for relevant documents, and then you inject those documents into the Prompt. 

However, injecting random text into a prompt confuses the model. You must structure the prompt using XML tags or clear delimiters so the model knows what is "Your Instruction" and what is "The Context Document".

---

## 📋 The RAG Master Template

```text
Act as a precise corporate Data Assistant.
Your task is to answer the user's question using ONLY the information provided in the <context> block below.

<context>
[INSERT SEARCH RESULTS / INTERNAL DOCUMENT TEXT HERE]
</context>

Constraints:
1. Do not use outside knowledge. If the answer is not in the <context>, reply strictly with "I do not have enough information to answer this."
2. Cite the specific part of the context you used to formulate your answer.

User Question: [INSERT USER QUESTION HERE]
```

---

## 🔍 Why the XML tags (`<context>`)?
LLMs (especially Claude and GPT-4) are specifically fine-tuned to recognize XML-style tags. Enclosing your raw data inside `<context>...</context>` prevents Prompt Injection attacks and keeps the model highly focused on the provided data.

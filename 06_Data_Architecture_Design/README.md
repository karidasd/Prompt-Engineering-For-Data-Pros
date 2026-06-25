# 06: Data Architecture & System Design 🏛️

## 🇬🇧 Theory (Θεωρία)

LLMs are not just code generators; they are exceptional System Architects. Since models like GPT-4 and Claude have read the entire documentation of AWS, GCP, and Azure, you can use them as your personal Principal Engineer.

When using an LLM for System Design, you must define the **Scale**, the **Budget**, and the **Team Skillset**.

---

## 📋 The Architecture Consultant Template

```text
Act as a Principal Cloud Architect.
I need to design a Data Architecture for a new startup.

Business Context:
- We receive 10,000 JSON events per second from IoT devices.
- We need real-time dashboards (sub-second latency) for our clients.
- We need to store raw data cheaply for historical ML training.

Constraints:
- Cloud Provider: AWS
- Budget: Very tight (startup). Prefer serverless over provisioned instances.
- Team: We have 2 Data Engineers who know Python and SQL well, but no Java/Scala knowledge.

Deliverables:
1. Propose the optimal AWS services for Ingestion, Storage, Processing, and Serving.
2. Explain why you chose these services considering our constraints.
3. Provide a rough data flow diagram using Mermaid.js syntax.
```

---

## 🌟 The Magic of Mermaid.js
Notice the last line in the prompt? You can ask LLMs to output **Mermaid.js** code. If you paste that code into a Markdown file on GitHub (or a Mermaid live viewer), it will automatically render a beautiful, visual Architecture Diagram! No more dragging and dropping boxes in Visio!

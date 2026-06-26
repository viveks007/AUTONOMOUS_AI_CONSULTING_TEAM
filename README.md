# Autonomous AI Consulting Team

Multi-Agent AI Consulting System built using:

- LangGraph
- Groq
- LangSmith
- Python
- Multi-Agent Architecture

Features:
- Supervisor Pattern
- Planning Agent
- Conditional Routing
- Parallel Execution
- Reducers
- Tool Calling
- Memory
- Checkpointing
- Human In The Loop
- LangSmith Monitoring


version 1 structure:

                 User
                   |
                   v
          Supervisor Agent
                   |
    --------------------------------
    |              |               |
    v              v               v
Business      Market         Data Science
Analyst       Researcher      Expert

    \             |            /
     \            |           /
      -----------------------
                  |
                  v
         Solution Architect

                  |
                  v
          Financial Analyst

                  |
                  v
              Reviewer

                  |
                  v
              User

version 2 structure:

                          User
                            │
                            ▼
                     LangGraph Workflow
                            │
                     Parallel Execution
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
 Business Agent      Market Researcher     Data Scientist
        │                   │                   │
        └──────────────┬────┴──────────────┬────┘
                       ▼
              Solution Architect
                       ▼
              Financial Analyst
                       ▼
                  Reviewer
                       ▼
                      END


version 3:

                 Agent
                    │
                    ▼
              invoke_llm()
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
      Groq                 Gemini
        │                     │
     Success?                 │
        │                     │
     Yes ▼                    │
     Return                   │
        │                     │
        └──────No─────────────┘
                    ▼
               Gemini Response
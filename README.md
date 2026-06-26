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


version 4:

                User
                  │
                  ▼
           LangGraph Graph
                  │
                  ▼
         SQLite Checkpointer
                  │
                  ▼
      checkpoint.db (disk)


version 5:

                  LangGraph Agent
                        │
              Tool Calling (@tool)
                        │
        ┌───────────────┴────────────────┐
        │                                │
 Native Tools                      MCP Tools
        │                                │
 Calculator                     Brave Search MCP
 CSV Analyzer                   Weather MCP
 File Reader
 DateTime
 Wikipedia

 version 6:

 AUTONOMOUS_AI_CONSULTING_TEAM
│
├── agents/
├── graph/
├── tools/
│
└── mcp/
    │
    ├── __init__.py
    ├── server.py          ← MCP Server
    ├── client.py          ← MCP Client
    ├── config.py
    └── tool_wrapper.py

Part 1 MCP Server

Part 2 Inspector


Part 3 MCP Client

Part 4 Tool Discovery

Part 5 Tool Execution

Part 6 LangChain Wrapper

Part 7 LangGraph Integration

Part 8 Official GitHub MCP

Part 9 Official Filesystem MCP

Part 10 Official Brave Search MCP


version 6: router introduce
                        User
                          │
                          ▼
                  Intent Router
                          │
                          ▼
                    Supervisor
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   Tool Agent      Business Agent     Data Scientist
        │                 │                 │
        └─────────────────┴─────────────────┘
                          │
                          ▼
                     Supervisor
                          │
         decides next agent OR END
                          │
        ┌──────────────┬──────────────┐
        ▼              ▼              ▼
 Market Research   Architecture   Financial
        │              │              │
        └──────────────┴──────────────┘
                          │
                          ▼
                     Supervisor
                          │
                     Reviewer?
                          │
                          ▼
                         END
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


version 1:
AUTONOMOUS_AI_CONSULTING_TEAM/

│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── agents/
│   │
│   ├── supervisor.py
│   ├── business_analyst.py
│   ├── market_researcher.py
│   ├── data_scientist.py
│   ├── solution_architect.py
│   ├── financial_analyst.py
│   ├── reviewer.py
│   └── report_generator.py
│
├── prompts/
│   │
│   ├── supervisor_prompt.py
│   ├── business_prompt.py
│   ├── market_prompt.py
│   ├── ds_prompt.py
│   ├── architect_prompt.py
│   ├── finance_prompt.py
│   ├── reviewer_prompt.py
│   └── report_prompt.py
│
├── graph/
│   │
│   ├── state.py
│   ├── workflow.py
│   ├── router.py
│   └── reducers.py
│
├── llm/
│   │
│   ├── groq_client.py
│   └── model_config.py
│
├── tools/
│   │
│   ├── web_search.py
│   ├── roi_calculator.py
│   ├── competitor_analysis.py
│   └── market_trends.py
│
├── memory/
│   │
│   ├── short_term_memory.py
│   ├── checkpoint_manager.py
│   └── thread_memory.py
│
├── reports/
│   │
│   ├── report_builder.py
│   └── pdf_export.py
│
├── evaluation/
│   │
│   ├── execution_metrics.py
│   ├── token_tracking.py
│   └── workflow_evaluation.py
│
├── data/
│   │
│   ├── sample_queries/
│   ├── generated_reports/
│   └── checkpoints/
│
└── tests/
    │
    ├── test_agents.py
    ├── test_graph.py
    └── test_tools.py


version 2:
AUTONOMOUS_AI_CONSULTING_TEAM/
│
├── agents/
├── checkpoint/
│   ├── checkpointer.py
│   └── sqlite_checkpoint.py
│
├── config/
│   └── settings.py
│
├── graph/
├── langsmith/
│   ├── callbacks.py
│   └── tracing.py
│
├── llm/
├── memory/
│   ├── conversation_memory.py
│   ├── memory_manager.py
│   └── short_term_memory.py
│
├── prompts/
├── tools/
│   ├── __init__.py
│   ├── base_tool.py
│   ├── calculator_tool.py
│   ├── file_reader_tool.py
│   ├── pdf_tool.py
│   ├── python_tool.py
│   ├── sql_tool.py
│   ├── tool_registry.py
│   ├── web_search_tool.py
│   └── wikipedia_tool.py
│
├── utils/
│   ├── helpers.py
│   └── logger.py
│
├── app.py
├── requirements.txt
└── .env
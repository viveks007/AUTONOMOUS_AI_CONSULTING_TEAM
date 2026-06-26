from langgraph.checkpoint.sqlite import SqliteSaver

conn = SqliteSaver.from_conn_string("data/checkpoint.db")

checkpointer = conn.__enter__()
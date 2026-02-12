# agent_trace/callback.py
from langchain_core.callbacks import BaseCallbackHandler
from .core import AgentTree
from rich import print as rprint  # <--- Import Rich's printer

class TraceCallback(BaseCallbackHandler):
    def __init__(self, session_name="Agent Execution"):
        self.session_name = session_name

    def on_chain_end(self, outputs, run_id, parent_run_id=None, **kwargs):
        """
        parent_run_id is None only for the top-level execution.
        This prevents the 'multiple trees' and 'orphaned' logs.
        """
        if parent_run_id is None:
            rprint(f"[bold blue]Final Trace: {self.session_name}[/bold blue]")
            trace = AgentTree(outputs)
            trace.show()
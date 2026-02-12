# agent_trace/core.py
from rich.tree import Tree
from rich.console import Console
from rich.panel import Panel
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

class AgentTree:
    def __init__(self, result):
        # FIX: Handle both dicts and raw lists
        if isinstance(result, dict):
            self.messages = result.get("messages", [])
        elif isinstance(result, list):
            self.messages = result
        else:
            self.messages = []
            
        self.console = Console()

    def _build_tree(self) -> Tree:
        root = Tree("[bold cyan]Agent Execution Trace[/bold cyan]")
        tool_call_map = {}
        
        for msg in self.messages:
            if isinstance(msg, HumanMessage):
                root.add(f"[bold green]User Input:[/bold green] {msg.content}")
            
            elif isinstance(msg, AIMessage):
                node_label = f"[bold yellow]AI Thought/Decision[/bold yellow]"
                if msg.content:
                    node_label += f"\n[italic]{msg.content[:100]}...[/italic]"
                
                ai_node = root.add(node_label)
                
                if hasattr(msg, 'tool_calls') and msg.tool_calls:
                    for tc in msg.tool_calls:
                        tool_node = ai_node.add(f"[magenta]Tool Call:[/magenta] {tc['name']}")
                        tool_node.add(f"[dim]Args: {tc['args']}[/dim]")
                        tool_call_map[tc['id']] = tool_node
            
            elif isinstance(msg, ToolMessage):
                parent_node = tool_call_map.get(msg.tool_call_id)
                if parent_node:
                    status = "[green]Success[/green]"
                    parent_node.add(f"[bold]Observation ({status}):[/bold]\n{msg.content}")
                else:
                    # Only show orphaned results if we actually have content
                    if msg.content:
                        root.add(f"[dim red]Partial Tool Result:[/dim red] {msg.content}")

        return root

    def show(self):
        if not self.messages:
            return
        tree = self._build_tree()
        self.console.print(Panel(tree, expand=False, border_style="blue"))
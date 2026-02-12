
# 🌳 agent-tree

**The missing visualizer for AI Agents. Turn messy terminal logs into beautiful, interactive trees.**

`agent-tree` is a zero-config, terminal-first observability tool. It captures the complex "reasoning loop" of AI agents and renders them as clean, hierarchical trees in your console. No API keys, no web dashboards, no fluff.

## Why agent-tree?
## 📸 Why use agent-tree?

| Without agent-tree (Messy JSON) | With agent-tree (Clean Visualization) |
| :---: | :---: |
| <img src="https://raw.githubusercontent.com/umarfarooq478/agent-tree/refs/heads/master/assets/json.png" width="400" /> | <img src="https://raw.githubusercontent.com/umarfarooq478/agent-tree/refs/heads/master/assets/agent-tree.png" width="400" /> |

## 🚀 Quick Start

### 1. Automatic (LangChain/LangGraph)
Just pass the `TraceCallback` into your agent's config. It automatically catches the end of the run and draws the tree.

```python
from agent_tree import TraceCallback

# Your agent logic...
agent.invoke(
    {"messages": [("user", "Is 50 shares of Apple under $15,000?")]},
    config={"callbacks": [TraceCallback(session_name="Budget Check")]}
)

```

### 2. Manual (Post-Execution)

If you already have a result object, you can visualize it instantly.

```python
from agent_tree import AgentTrace

at = AgentTrace(result_object)
at.show()

```

## ✨ Key Features

* **Instant Visuals:** Built on top of the `Rich` library for high-performance terminal UI.
* **Root-Only Tracing:** Smart logic prevents "log spam" by only showing the final, complete execution tree.
* **Framework Agnostic:** Works perfectly with LangChain but can be adapted for any JSON-like agent output.

## 🛠 Installation

```bash
pip install agent-tree

```

## Github Repository
You can find the full source code and contribute on [GitHub](https://github.com/umarfarooq478/agent-tree).
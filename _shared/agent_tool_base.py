# MySquad Agent Mesh — Base Tool Contract
from __future__ import annotations
from typing import Any, Dict

class AgentTool:
    name: str = "base_tool"
    version: str = "1.0.0"

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        raise NotImplementedError

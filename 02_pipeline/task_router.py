# MySquad Agent Mesh — Intelligent Task Router
from __future__ import annotations

ROSTER = {
    "ops": "HermesLocal",
    "git_byok": "HermesLocal",
    "code": "Cursor",
    "3d_scene": "Claude",
    "build": "Grok"
}

def route_task(task_type: str) -> str:
    return ROSTER.get(task_type, "HermesLocal")

if __name__ == "__main__":
    for task in ["git_byok", "code", "3d_scene", "ops"]:
        print(f"Task '{task}' -> Assigned to: {route_task(task)}")

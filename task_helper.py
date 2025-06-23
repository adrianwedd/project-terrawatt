from typing import List, Dict

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


def parse_tasks(path: str) -> List[Dict[str, str]]:
    """Parse tasks from CODEX_TASKS.md into dictionaries."""
    tasks = []
    with open(path) as fh:
        block = []
        in_code = False
        for line in fh:
            stripped = line.rstrip()
            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if in_code or stripped.startswith("## Schema"):
                continue
            if stripped == "" and block:
                tasks.append(_load_block(block))
                block = []
            else:
                block.append(stripped)
        if block:
            tasks.append(_load_block(block))
    # discard placeholder tasks
    return [t for t in tasks if t and "XXX" not in t.get("id", "")]


def _load_block(lines: List[str]) -> Dict[str, str]:
    entry = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            entry[key.strip()] = value.strip()
    return entry


def prioritize_tasks(tasks: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Return tasks sorted by priority and id."""
    return sorted(
        tasks,
        key=lambda t: (PRIORITY_ORDER.get(t.get('priority', 'P3'), 3), t.get('id', '')),
    )


if __name__ == '__main__':
    import sys

    task_file = sys.argv[1] if len(sys.argv) > 1 else 'CODEX_TASKS.md'
    for t in prioritize_tasks(parse_tasks(task_file)):
        print(f"{t.get('id')} - {t.get('title')} ({t.get('priority')})")


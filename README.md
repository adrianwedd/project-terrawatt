# Terrawatt Research Playground

This repository contains experiments for building a sustainability research platform using LangGraph and LangChain. The backlog of incremental tasks lives in [`CODEX_TASKS.md`](CODEX_TASKS.md) and is parsed by `task_helper.py` to help prioritize daily work.

Key design references include the architectural blueprint and several research plans stored in this repo. See [`docs/setup.md`](docs/setup.md) for environment notes and usage instructions.

## License

This project is released under the [MIT License](LICENSE).

## Starter Graph

A minimal LangGraph demo lives in `orchestrator/starter_graph.py`. It shows how
state is saved with `SqliteSaver` and how a run can resume after interruption.
Run it with:

```bash
python -m orchestrator.starter_graph
```

The first execution processes the ingest node then stops. Running the command
again resumes from the saved state and completes the analysis step.

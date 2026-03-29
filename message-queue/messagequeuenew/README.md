# Task Processing System

A Python-based task processing system that mirrors the producer-consumer architecture of the original RabbitMQ notification example.

## Overview

This project accepts tasks from a producer, stores them in a FIFO queue, and processes them with a consumer. Each task includes a type, payload, status, and retry behavior.

## Architecture

```
+----------+     +-------------+     +-------------+
| Producer | --> | Task Queue  | --> | Consumer    |
+----------+     +-------------+     +-------------+
      |                |                 |
      |                |                 +-- executes task handlers
      |                |                 +-- marks task completed or failed
      |                +-- stores tasks   +-- requeues failed tasks
      +-- submits tasks
```

## Supported Task Types

- `resize_image`
- `calculate_sum`
- `convert_file`

## Folder Structure

- `config/` - environment-based configuration values
- `queue/` - queue implementation and task storage
- `producer/` - task validation and submission logic
- `consumer/` - task execution and retry handling
- `tasks/` - task models, handlers, and factory functions
- `tests/` - unit tests for queue and task execution
- `main.py` - application entrypoint

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Execute the sample task processing workflow:

```bash
python main.py
```

## Test

Run unit tests with:

```bash
pytest
```

## Design Decisions

- Python was chosen for its developer productivity and mature support for task orchestration.
- The system uses a thread-safe in-memory queue to keep the implementation simple and portable.
- Clear separation of concerns is enforced with distinct producer, consumer, queue, and task modules.
- Configuration values are loaded from environment variables via `config/settings.py`.
- Structured logging is implemented using Python's standard `logging` library.
- The retry mechanism increments a task attempt counter and requeues tasks when failures occur.

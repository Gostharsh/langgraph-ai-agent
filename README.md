# LangGraph AI Agent

A multi-step AI agent built with LangGraph, Pydantic, RAG, planning, execution, reflection, and replanning.

## Features

- Question Rewriting
- Router Agent
- Direct Tool Execution
- Planning Agent
- RAG Search
- Reflection Agent
- Replanning Loop
- Final Answer Generation

## Architecture

User Question
    ↓
Rewrite
    ↓
Router
 ┌───────────┴───────────┐
 │                       │
Direct                 Planner
 │                       │
 └──────→ Executor ←─────┘
              ↓
         Reflector
         ↙      ↘
    Replan     Answer
       ↓
    Executor

## Run

```bash
python main.py

Tech Stack
- LangGraph
- LangChain
- Pydantic
- ChromaDB
- Ollama/OpenAI
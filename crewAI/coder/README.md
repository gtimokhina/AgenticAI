# Coder Crew

Welcome to the Coder Crew project, powered by [crewAI](https://crewai.com). This template is designed to set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/coder/config/agents.yaml` to define your agents
- Modify `src/coder/config/tasks.yaml` to define your tasks
- Modify `src/coder/crew.py` to add your own logic, tools and specific args
- Modify `src/coder/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart this crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the coder Crew, assembling the agents and assigning them tasks as defined in the configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The coder Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.



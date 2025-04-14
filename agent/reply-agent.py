import asyncio
import os
import shutil
import subprocess
import time
from typing import Any

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings

from constants import SYSTEM_PROMPT_BASE, SYSTEM_PROMPT_JOURNEY_INSTRUCTIONS


async def run(mcp_server: MCPServer):
    agent = Agent(
        name="Assistant",
        instructions=SYSTEM_PROMPT_BASE + SYSTEM_PROMPT_JOURNEY_INSTRUCTIONS,
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="required", parallel_tool_calls=True),
    )

    while True:
        # Wait for the user to input a message
        message = input("Enter a message (or 'exit' to quit): ")
        if message.lower() == "exit":
            break

        # Run the agent with the user input
        print(f"\n\nRunning: {message}")
        result = await Runner.run(starting_agent=agent, input=message)
        print(result.final_output)


async def main():
    async with MCPServerSse(
            name="SSE Python Server",
            params={
                "url": "http://0.0.0.0:8000/sse"
            },
            cache_tools_list=True
    ) as server:
        trace_id = gen_trace_id()
        with trace(workflow_name="SSE Example", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
            await run(server)


def start_sse_server():
    # We'll run the SSE server in a subprocess. Usually this would be a remote server, but for this
    # demo, we'll run it locally at http://localhost:8000/sse
    process: subprocess.Popen[Any] | None = None
    try:
        this_dir = os.path.dirname(os.path.abspath(__file__))
        server_file = os.path.join(this_dir, "server.py")

        print("Starting SSE server at http://localhost:8000/sse ...")

        # Run `uv run server.py` to start the SSE server
        process = subprocess.Popen(["uv", "run", server_file])
        # Give it 3 seconds to start
        time.sleep(3)

        print("SSE server started. Running example...\n\n")
    except Exception as e:
        print(f"Error starting SSE server: {e}")
        exit(1)


if __name__ == "__main__":
    # Let's make sure the user has uv installed
    if not shutil.which("uv"):
        raise RuntimeError(
            "uv is not installed. Please install it: https://docs.astral.sh/uv/getting-started/installation/"
        )

    asyncio.run(main())

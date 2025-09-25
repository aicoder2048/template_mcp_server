from fastmcp import FastMCP
from contextlib import asynccontextmanager
from typing import Dict, Any
from .tools.hello_tool import hello
from .prompts.hello_prompt import call_hello_multiple
from .config.settings import settings

@asynccontextmanager
async def lifespan(server: FastMCP):
    """Server lifecycle management."""
    print(f"🚀 Starting {settings.server_name} server...")
    yield
    print(f"👋 Shutting down {settings.server_name} server...")

def create_server() -> FastMCP:
    """Create and configure the MCP server."""
    mcp = FastMCP(
        name=settings.server_name,
        version=settings.version,
        lifespan=lifespan
    )

    @mcp.tool()
    async def hello_tool(name: str) -> Dict[str, Any]:
        """
        Say hello to someone.

        Args:
            name: The name of the person to greet

        Returns:
            A greeting response with status and message
        """
        return await hello(name)

    @mcp.prompt()
    async def call_hello_multiple_prompt(name: str, times: int = 3) -> str:
        """
        Generate a prompt to call hello multiple times.

        Args:
            name: The name to use in the hello calls
            times: Number of times to call hello (default: 3)

        Returns:
            A formatted prompt string
        """
        return await call_hello_multiple(name, times)

    return mcp

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("fibonacci")

def fibonacci(n: int) -> int:
    if n <= 1:
        return max(0, n)
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@mcp.tool()
async def get_fibonacci(n: int) -> str:
    """Berechnet die n-te Fibonacci-Zahl.

    Args:
        n (int): Die Position in der Fibonacci-Sequenz.
    """
    fibonacci_result = str(fibonacci(n))
    return fibonacci_result


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

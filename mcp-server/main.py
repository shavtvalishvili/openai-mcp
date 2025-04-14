import server


def main():
    print("Hello from mcp-server!")


if __name__ == "__main__":
    # Initialize and run the server
    server.mcp.run(transport='sse')

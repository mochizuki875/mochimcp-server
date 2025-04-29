import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mochimcp-server")

# addというツールを定義
@mcp.tool(name="add", description="Add two numbers")
async def add(a: int, b: int) -> int:
    return a + b

# subtractというツールを定義
@mcp.tool(name="subtract", description="Subtract two numbers")
async def subtract(a: int, b: int) -> int:
    return a - b

# create_fileというツールを定義
# ホームディレクトリ配下にファイルを作成する
@mcp.tool(name="create_file", description="Create a file with given content")
async def create_file(filename: str, content: str) -> str:
    home_directory = os.path.expanduser('~')
    file_path = os.path.join(home_directory, filename)

    with open(file_path, 'x', encoding='utf-8') as file:
        file.write(content)

    return f"Successfully wrote to {file_path}"

if __name__ == "__main__":
    # 通信にstdioを使用する
    mcp.run(transport="stdio")
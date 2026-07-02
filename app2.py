from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
def divide(a,b):
    return a / b

@tool
def add(a: int, b: int) ->int: 
    """Add two numbers"""
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return a/b
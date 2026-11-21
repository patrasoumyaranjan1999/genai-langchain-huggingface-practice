"""Day 3 - dummy functions for practice."""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def reverse_text(text: str) -> str:
    """Return the text reversed."""
    return text[::-1]


def word_count(text: str) -> int:
    """Return the number of words in the text."""
    return len(text.split())


def fake_llm_response(prompt: str) -> str:
    """Pretend to call an LLM and return a canned response."""
    return f"[dummy LLM] You asked: '{prompt}'. This is a placeholder answer."


if __name__ == "__main__":
    print(greet("World"))
    print(add(2, 3))
    print(reverse_text("LangChain"))
    print(word_count("Hugging Face makes NLP easy"))
    print(fake_llm_response("What is GenAI?"))

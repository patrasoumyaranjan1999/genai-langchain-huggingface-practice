def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Day 2."


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(greet("Learner"))
    print("2 + 3 =", add(2, 3))

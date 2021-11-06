TEXT = """What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
TEMPLATE = "five centuries"
P = 3


def hash(text: str, from_i, count) -> int:
    ret = 0
    for i in range(count):
        print(i, from_i + i, count - i - 1)
        ret += (text[from_i + i]) * P ** (count - i - 1)


def main():
    hash(TEXT, 0, 5)


if __name__ == '__main__':
    main()
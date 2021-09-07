import random


def generate_tag(tag):
    if tag is not None:
        while True:
            yield tag
    tags = ("html", "head", "body", "p", "a", "div", "h1", "h2", "h3")
    while True:
        yield random.choice(tags)


def html_tag(tag=None):
    tag = generate_tag(tag)

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            lines = [f"<{next(tag)}>" + line + f"</{next(tag)}>" for line in args]
            original_function(*lines)

        return wrapper

    return decorator


@html_tag()
def print_lines(*args):
    for line in args:
        print(line)


if __name__ == '__main__':
    words = [
        "salam",
        "aleykum",
        "ruble",
        "budet"
    ]
    print_lines(*words)

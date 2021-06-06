import random


def main():
    with open("snl.txt", "r") as file:
        text = file.read().strip().split("\n")[::-1]
        try:
            while True:
                i = random.randint(0, len(text) / 2 - 1)
                print(
                    f"{i} -> {text[2*i+1]} -> http://www.youtube.com/watch?v={text[2*i]}"
                )
        except KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    main()
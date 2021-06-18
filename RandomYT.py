import random
import sys
import webbrowser


def main():
    with open("snl.txt", "r") as file:
        text = file.read().strip().split("\n")[::-1]
        try:
            while True:
                i = random.randint(0, len(text) / 2 - 1)
                url = f"http://www.youtube.com/watch?v={text[2*i]}"
                print(f"{i} -> {url} -> {text[2*i+1]}")
                webbrowser.open(url)
                input()
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    main()

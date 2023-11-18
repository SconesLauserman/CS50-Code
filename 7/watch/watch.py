import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if result := re.search(r'.+src="https?://(www\.)?youtube.com/embed/([^"]+)".+', s):
        return f"https://youtu.be/{result.group(2)}"


if __name__ == "__main__":
    main()

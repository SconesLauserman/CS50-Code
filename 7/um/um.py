import re


def main():
    print(count(input("Text: ")))


def count(s):
    final = 0
    final += len(re.findall(r"\sum[,?\.?\!?\??\s]", s[2:], re.IGNORECASE))
    if s[:2].lower() == "um": final += 1
    return final


if __name__ == "__main__":
    main()

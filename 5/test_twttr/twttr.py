def main():
    input_shorten = shorten(input("Input: "))
    print(f"Output: {input_shorten}")


def shorten(sentence):
    replacements = list("aeiouAEIOU")
    output = sentence
    for char in replacements:
        output = output.replace(char, "")
    return output


if __name__ == "__main__":
    main()

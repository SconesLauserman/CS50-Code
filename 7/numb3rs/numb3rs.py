def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        split_ip = ip.split(".")
        if len(split_ip) != 4:
            return False
        for num in split_ip:
            if float(num) >= 0 and float(num) <= 255:
                pass
            else:
                return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()

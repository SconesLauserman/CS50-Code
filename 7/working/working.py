import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.fullmatch(
        r"([1-2]?[0-9](:[0-6][0-9])?) (AM|PM) to ([1-2]?[0-9](:[0-7][0-7])?) (PM|AM)", s
    ):
        AM = re.sub("[a-zA-Z\s]", "", s.split("AM")[0][-6:])
        PM = re.sub("[a-zA-Z\s]", "", s.split("PM")[0][-6:])
        AM_whole = AM.split(":")[0]
        AM_minor = "00"
        if len(AM.split(":")) >= 2:
            AM_minor = AM.split(":")[1]
        PM_whole = PM.split(":")[0]
        PM_minor = "00"
        if len(PM.split(":")) >= 2:
            PM_minor = PM.split(":")[1]
        if int(AM_whole) < 10:
            AM_whole = "0" + AM_whole
        if int(PM_whole) < 10:
            PM_whole = "0" + PM_whole
        if AM_whole == "12":
            AM_whole = "00"
        if PM_whole == "12":
            PM_whole = "00"
        if (
            int(PM_minor) > 59
            or int(AM_minor) > 59
            or int(AM_whole) > 11
            or int(PM_whole) > 11
        ):
            raise ValueError

        if re.sub(r"[0-9\sto:]", "", s).startswith("AM"):
            return f"{AM_whole.strip()}:{AM_minor} to {int(PM_whole) + 12}:{PM_minor}"
        else:
            return f"{int(PM_whole) + 12}:{PM_minor} to {AM_whole.strip()}:{AM_minor}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()

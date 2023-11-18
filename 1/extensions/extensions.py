# ======================================================================================================================== #
# Step 1: Within function "main", print the users file extension media type, using the function "file_media_type".         #
# Step 2: Implement function "file_media_type".                                                                            #
# Step 3: Write function "file_media_type":                                                                                #
#   Step 1(file_media_type): Make a dicranary of all the file extensions and the value as the media type.                  #
#   Step 2(file_media_type): Make the following conditions:                                                                #
#       Condition 1(file_media_type): If the file extension exist in the dictanary, then return the file_extension.        #
#       Condition 2(file_media_type): Else then return "application/octet-stream" which is a common default.               #
# ======================================================================================================================== #


def main():
    # Step 1(main): Print the users file extension media type, using the function "file_media_type".
    print(file_media_type(input("File name: ").lower().strip().split(".")))


# Step 2: Implement the function "file_media_type"
def file_media_type(file="file.jpeg"):
    # Step 1(file_media_type): Make a dictanary of all the file extensions and the value as the media type.
    file_extension = {
        "jpeg": "image/jpeg",
        "jpg": "image/jpeg",
        "gif": "image/gif",
        "png": "image/png",
        "txt": f"text/{file[0]}",
        "zip": "application/zip",
        "pdf": "application/pdf",
    }
    # Step 2(file_media_type): Write the following condition:

    # Condition 1(file_media_type): If the file exist in the dicranary, then return the file_extension.
    if file[len(file) - 1] in file_extension:
        return file_extension[file[len(file) - 1]]
    # Condition 2(file_media_type): Else then return "application/octet-stream" which is a common default.
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()

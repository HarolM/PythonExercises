#implement a program that prompts user for name of a file and then outputs that file's media type case insensitive in any of the following suffixes. 
# .gif .jpg .jpeg .png .pdf .txt .zip

filename = input("File Name: ").lower().split(".")

try:
    if filename[1] in ["gif", "jpg", "jpeg", "png"]:
        print(f"image/{filename[1]}")

    elif filename[1] in ["pdf", "zip"]:
        print(f"application/{filename[1]}")

    elif filename[1] in [".txt"]:
        print("text/plain")

    else:
        print("application/octet-stream")
except IndexError:
    print("application/octet-stream")
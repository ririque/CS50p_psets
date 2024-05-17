def main():
    question = input("File name: ").lower().strip()
    extensions(question)


def extensions(n):
    if n.endswith((".jpeg",  ".jpg")):
        print("image/jpeg")
    elif n.endswith(".png"):
        print("image/png")
    elif n.endswith(".gif"):
        print("image/gif")
    elif n.endswith(".pdf"):
        print("application/pdf")
    elif n.endswith(".zip"):
        print("application/zip")
    elif n.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")


main()

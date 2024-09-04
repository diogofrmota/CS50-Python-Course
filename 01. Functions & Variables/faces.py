def convert(text):
    return text.replace(":)", "🙂").replace(":C", "🙁")


def main():
    print(convert(input("Escreve um smile: ")))


main()
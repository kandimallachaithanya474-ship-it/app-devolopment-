from googletrans import Translator

translator = Translator()

while True:
    print("\n1. Translate  2. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text: ")
        src = input("From language (en, hi, te): ")
        dest = input("To language (en, hi, te): ")

        result = translator.translate(text, src=src, dest=dest)

        print("Translated Text:", result.text)

    elif choice == "2":
        break

    else:
        print("Invalid choice")
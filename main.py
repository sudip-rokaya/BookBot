def main():
    file_path = "books/frankenstein.txt"
    print(f"Trying to open: {file_path}")  # Debug statement to verify the file path
    try:
        with open(file_path, "r") as f:
            file_contents = f.read()
        return print_report(file_contents)
    except FileNotFoundError:
        print(f"Error: Thed file at '{file_path}' was not found.")
        return 0

def count_words(text):
    return len(text.split())
def count_characters(text):
    count = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            count[char] = 1 + count.get(char, 0)
    return count
def print_report(text):
    print(f"{count_words(text)} was found in the document")
    count = count_characters(text)
    sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    for char, value in sorted_count:
        print(f"The {char} character was found {value} times")
        print('\n')
    print(count)

if __name__ == "__main__":
    print(main())

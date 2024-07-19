def main():

    with open("books/frankenstein.txt") as f:

        file_contents = f.read()
        word_list = file_contents.split()
        print(word_list.count())

    return None

if __name__ == '__main__':
    main()



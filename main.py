def main():
    book_path = "books/frankenstein.txt"
    
    file_contents = read_book(book_path)
    word_list = get_world_list(file_contents) 
    char_list = count_characters(file_contents)
    sorted_list = sorted(char_list.items(), key=lambda item: item[1], reverse=True)

    print(char_list) 
        
    print(f"--- Begin report of{book_path} ---")
    print(f"{len(word_list)} words found in the document")
    for k,v in sorted_list:
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
    
    return None

def count_characters(file_content):
    char_dict = {'a': 0, 'b': 0, 'c' : 0, 'd' : 0 , 'e': 0, 'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,
                  'm':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,
                 }
    for c in file_content:
        if c.lower() in char_dict:
            char_dict[c.lower()] +=1
    return char_dict

def get_world_list(file_contents):
    return file_contents.split()

def read_book(book_path):
    with open(book_path) as f:
        return f.read()
    

if __name__ == '__main__':
    main()



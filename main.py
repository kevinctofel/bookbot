def main():
  file_path = "books/frankenstein.txt"
  text = read_book(file_path)
  total_words = count_words(text)
  letter_dict = count_letters(text)
  print_report(total_words, letter_dict)
  
def read_book(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents
  
def count_words(text):
  words = text.split()
  # print(words)
  return len(words)

def count_letters(text):
  letters = {}
  # key is a letter in string format
  # value is an integer
  for letter in text.lower():
    letters[letter] = letters.get(letter, 0) + 1
  return letters

def print_report(words, letters):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'\n{words} words found in the document\n')

    for letter in alpha:
      print(f"The '{letter}' character was found {letters.get(letter)} times")

    print('\n--- End report ---')


main()
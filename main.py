def main():
  file_path = "books/frankenstein.txt"
  text = read_book(file_path)
  print (count_words(text))
  print (count_letters(text))
  
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
  print(letters)

main()
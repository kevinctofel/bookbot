def main():
  file_path = "books/frankenstein.txt"
  text = read_book(file_path)
  print (count_words(text))
  
def read_book(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents
  
def count_words(text):
  words = text.split()
  # print(words)
  return len(words)

main()
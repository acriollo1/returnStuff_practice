def word():
  word = str(input("Choose a word:"))
  return word

def reverse_word(x):
  new = x[::-1]
  word = new.upper()
  return word
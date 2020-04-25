import sys

#determines if the first character is alphabetic
def alpha(char):
  if char.isalpha():
    return True
  return False

#determines if the username is valid
def validUsername(str):
    first = str[0]
    if alpha(first) and len(str) <= 255:
      return "Valid Username"
    else:
      return "Invalid Username"


if __name__ == "__main__":
  print(validUsername("Kimberly123"))



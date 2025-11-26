char = 'a'
string = "hello apple"
if char.lower() in string.lower():
   print(f"'{char}' found in the string (case-insensitive).")
else:
   print(f"'{char}' not found in the string.")
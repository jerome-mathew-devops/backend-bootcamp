marks = 80 
result = ""
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)


#Match Statements
def checkVowel(n):
   match n:
      case 'a': return "Vowel alphabet"
      case 'e': return "Vowel alphabet"
      case 'i': return "Vowel alphabet"
      case 'o': return "Vowel alphabet"
      case 'u': return "Vowel alphabet"
      case _: return "Simple alphabet"
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('o'))

#For Loop
words = ["one", "two", "three"]
for x in words:
  print(x)

#While Loop
i = 1
while i < 6:
  print(i)
  i += 1

#The break statement
x = 0

while x < 10:
    print("x:", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1

print("End")

#The Continue Statement
for letter in "Python":
    # continue when letter is 'h'
    if letter == "h":
        continue
    print("Current Letter :", letter)

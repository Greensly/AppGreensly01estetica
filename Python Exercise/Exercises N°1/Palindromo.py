def palindromo(Word):
    large = len(Word)
    wordInv = ""
    for i in range(large):
        wordInv += Word[large-1-i]
    for j in range(large):
        if wordInv[j] == Word[j]:
            n = j+1
    if n == large:
        print("La palabra es Palindrome")
    else:
        print("La palabra no es Palindrome")

WordDetec = str(input("Ingrese palabra para chequear si es un palindrome"))

palindromo(WordDetec)
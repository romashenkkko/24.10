s=str(input("Dati sirul de caractere-"))
print("a)numărul de apariţii ale caracterului ’A’ în şirul x=",s.count(chr(65)))
a=''
if 'A' in s:
    for i in range(0,len(s)):
        if s[i]==chr(65):
            a=s.replace(chr(65),chr(42))
        print("b)şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’=",a)
else:
    print("b)şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’=",s)
b=''
if 'B' in s:
    for i in range(0,len(s)):
        if s[i]==chr(66):
            b=s.replace(chr(66),'')
        print("c)şirul obţinut prin radierea din şirul X a tuturor apariţiilor caracterului ’B’=",b)
else:
    print("c)şirul obţinut prin radierea din şirul X a tuturor apariţiilor caracterului ’B’=",s)
print("d)numărul de apariţii ale silabei 'MA' în şirul X=",s.count('MA'))
print("g)scrierea inversă a şirului X=",s[::-1])
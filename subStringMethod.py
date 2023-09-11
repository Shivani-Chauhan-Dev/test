# s = "durgasoftware durgasoftware"
# print(s.count("soft"))
# print(s.count("s" , 6 , 18))

# s = "learning python is very difficult"
# s1 = s.replace("defficult","easy")
# print(s1)

# str = "one one was a race horse, two two was one too"
# x = str.replace("one", "three")
# print(x)

# str = "one one was a race horse, two two was one too"
# x = str.replace("one", "three", 3)
# print(x)


# replace all instances of 'r' (old) with 'e' (new)
# string = "grrks FOR grrks"
# print(string.replace("r","e"))
# print(string.replace("r" ,"e" , 3))

# split()function

# string = "one,two,three"
# s = string.split(",")
# print(s)


# text = 'geeks for geeks'
# s = text.split(" ")
# print(s)

# word = 'geeks, for, geeks'
# s1 = word.split(",")
# print(s1)

# word = 'geeks:for:geeks'
# s1 = word.split(":")
# print(s1)

# word = 'CatBatSatFatOr'
# s1 = word.split("t")
# print(s1)
# for x in s1:
#     print(x)
# print(type(x))

# word = "geeks for geeks pawan"
# print(word.split(" " , 2))
# print(word.split(" ", 0))
# print(word.split(" ", 4))


s = "durga software"
s1 =  s.split(" ")
# print(s1)
# print(s1[::-1])
l = len(s1)
for x in s1:
    print(s1[x - l - 1])
    


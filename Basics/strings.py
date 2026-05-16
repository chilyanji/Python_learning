str1 = "this is a string"
len1 = len(str1)
print(len1)


# indexing #

str2 =  'Ayush Singh'
ch = str2[4]
print(ch)



# Slicing #

str3 = 'Saurabh Kumar'
print((str3[-13:-6]))
print((str3[8:]))

# remove space from front & last
print(str3.strip)

# Spacing 
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))

# Function #


print(str3.endswith("bh"))
print(str3.capitalize())
print(str3.replace("Saurabh Kumar", "Ayush Singh"))
print(str3.find("l"))
print(str3.count("h"))
txt = "We are the so-called \"Vikings\" from the north." 

# \'	Single Quote
txt = 'It\'s alright.'
print(txt) #return (It's alright.)

# \\	Backslash	
txt = "This will insert one \\ (backslash)."
print(txt) #return (This will insert one \ (backslash).)

# \n	New Line	
txt = "Hello\nWorld!"
print(txt) #return (Hello
#                   World!)

# \r	Carriage Return	
txt = "Hello\rWorld!"
print(txt)  #return same as\n

# \t	Tab	
txt = "Hello\tWorld!"
print(txt) #return (Hello   World!)

# \b	Backspace	
txt = "Hello \bWorld!"
print(txt) #return (HelloWorld!)

# \ooo	Octal value	
txt = "\110\145\154\154\157"
print(txt) #return (Hello)

# \xhh	Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #return (Hello)
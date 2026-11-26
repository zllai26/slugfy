import slugfy

x = slugfy.dash("Hello ,,.,.,., World")
y = slugfy.underscore("Hello  World")
z = slugfy.dashlimit("Hello ,,.,.,., World", 100)
a = slugfy.underscorelimit("a", 1)

print(x)
print(y)
print(z)
print(a)
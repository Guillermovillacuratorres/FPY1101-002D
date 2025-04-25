texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ut rhoncus ex, in rutrum orci. Integer tempor eros sapien, volutpat placerat erat egestas eget. Sed."
nombre = "juan"
print(texto.upper())
print(texto.lower())
print(nombre.capitalize())
print(len(texto))
print(texto[162])
print(len("123456"))

print(texto.find("DOLORx"))

txt = "  Hola o o o o o   "
print(txt.strip())
print(txt.replace("LA","@").replace("a","#"))

print(txt[2:4].replace("o","$"))

print(texto.split())
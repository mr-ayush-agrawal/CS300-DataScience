names = ["Ayush Agrawal", "Rishi Sri..", "Harsh Singh", "GG Mishra"]
ini = []
for name in names:
    x = lambda y: y.split(" ")[0]
    ini.append(x(name))
print(ini)
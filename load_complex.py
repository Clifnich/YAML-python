import yaml

with open('aliass.yml', 'r') as ymlfile:
    myml = yaml.load(ymlfile)

for section in myml:
    print(section)

print(myml['development'])
#print(section['defaults']['adapter'])

#for subsection in section[0]:
#    print(subsection)
#print(myml['This is a key\nthat has multiple lines'])

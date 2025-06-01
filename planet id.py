def planet(id):
    planet = {1:'mercury',2:'earth',3:'jupiter',4:'venus',5:'saturn',6:'mars',7:'uranus',8:'neptune'}
    return planet[id]

id = int(input("Enter planet id"))
p = planet(id)
print(p)


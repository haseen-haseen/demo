def generatorExample():
    for i in range(5000):
        yield i


gen=generatorExample()   
for i in gen:
    print(i)     
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
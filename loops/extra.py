index = 17;
while True:
    index = index+1
    pirates = 5
    monkey = 1
    coconuts = index

    totalSpecies = pirates + monkey

    for i in range(pirates):
        _coconunsEachPerson = (coconuts / 5)
        coconuts = coconuts - _coconunsEachPerson - 1
        print ('Er zijn ',coconuts,'over')

    print('Ze zijn wakker JarrrHarr')

    _coconunsEachPerson = (coconuts / 5)
    coconuts = coconuts - _coconunsEachPerson - 1
    # print(int(coconuts))
    if int(coconuts) == 1:
        print(index)
        break    

print(coconuts)
print('alle hands aan deck! yarr. Dat beest is dik geworden. 😜')


# f = open('pow.txt','rt')
# for i in range(10):
    # a = f.readline()
    # # a = a.lstrip()
    # a = a.rstrip()
    # if i==9:
    #     print(a)
    #     break
    # print(a,end='')

# f.close()

with open('./pow.txt','rt') as f:
    for i in range(10):
        a = f.readline()
        # a = a.lstrip()
        a = a.rstrip()
        if i==9:
            print(a)
            break
        print(a,end='')

import re

def main():
    p = ''
    a = open('pow.txt','rt')
    a.readline()
    while True:
        b = a.readline()
        p+=b
        if b == '':
            break

    a1 = re.compile(r'M.{5}')
    a2 = a1.findall(p)
    print(a2)
    print(p)
if __name__ == '__main__':
    main()
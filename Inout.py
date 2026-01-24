with open('data.txt','w') as f:
    f.write('Hello\n')
    f.write('Xin chào')
with open('data.txt','r') as reader:
    print(reader.read())
    reader.seek(0)
    print(reader.readline(),end='')
    print(reader.readline())

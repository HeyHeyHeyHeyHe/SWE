
def trungbinh(a):
    x=0
    k=len(a)
    for i in a:
        x+=i
    return x/k



a=list(map(int,input("Nhập dãy số:").split()))
print(trungbinh(a))
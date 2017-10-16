def main():
    for i in range(3):
        a[i]=input()
    if a[0]>a[1]:
        if a[0]>a[2]:
            print(a[0])
        else:
            print(a[2])
    else:
        if a[1]<a[2]:
            print(a[2])
        else:
            print(a[1])
    print('end')
main()
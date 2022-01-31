n=int(input())
arr1=[int(x) for x in input().split()]
n2=int(input())
arr2=[int(x) for x in input().split()]
for item1 in arr1:
    #print("item",item1)
    for item2 in arr2:
        #print("item2",item2)
        if(item1==item2):
            print(item1)
            arr2.remove(item2)
            break

#same prgrm lisyt comprehnesion se v kia h

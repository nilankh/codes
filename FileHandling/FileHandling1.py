

#to read data
f = open('MyData.txt', 'r')


##print(f.read())
##print(f.readline())
##print(f.readline())


f1 = open('abc.txt', 'w')
##f1 = open('abc.txt', 'a')
##f1.write('Nilank')
##f1.write('Nikhil')

##for data in f:
##    f1.write(data)
##    print(data)

##w = open('up.JPG', 'rb')
###rb = read binary
##for i in w:
##    print(i)

w = open('up.JPG', 'rb')
#rb = read binary
w1 = open('Mypic.JPG','wb')
#wb - write binary
for i in w:
    w1.write(i)














    

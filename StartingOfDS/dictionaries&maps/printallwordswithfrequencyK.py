'''
#one way
s="this is a word string having many many word"
#print(s)
k=2
words=s.split()
#print(words)
d={}
for w in words:
    #print(w)
    if w in d:
        #print('inside d',d)
        d[w]=d[w]+1
    else:
        d[w]=1
        #print('else',d)
#print()
print('final d',d)'''




'''
#another way
s="this is a word string having many many word"
k=2
words=s.split()
d={}
for w in words:
    #print(w)
    d[w]=d.get(w,0)+1
    #print(d[w])
   
print(d)
for w in d:
    if d[w]==k:
        print(w)
'''



   

s="this is a word string having many many word"
k=1
words=s.split()
def printKFreqWords(s,k):
    words=s.split()
    d={}
    for w in words:
        
        d[w]=d.get(w,0)+1
        #(d[w])
    for w in d:
        if d[w]==k:
            print(w)
printKFreqWords(s,k)

'''
>>> words = s.split()
>>> words
['this', 'is', 'a', 'word', 'string', 'having', 'many', 'many', 'word']
>>> d={}
>>> d[this] = d.get('this',0)+1
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d[this] = d.get('this',0)+1
NameError: name 'this' is not defined
>>> d['this'] = d.get('this',0)+1
>>> d
{'this': 1}
>>> d['is'] = d.get('is',0) + 1
>>> d
{'this': 1, 'is': 1}
>>> d['a'] = d.get('a',0) + 1
>>> d
{'this': 1, 'is': 1, 'a': 1}
>>> d['word'] = d.get('word',0) + 1
>>> d
{'this': 1, 'is': 1, 'a': 1, 'word': 1}
>>> d['string
  
SyntaxError: EOL while scanning string literal
>>> d['string'] = d.get('string',0)+1
>>> d
{'this': 1, 'is': 1, 'a': 1, 'word': 1, 'string': 1}
>>> d['having'] = d.get('having',0) + 1
>>> d
{'this': 1, 'is': 1, 'a': 1, 'word': 1, 'string': 1, 'having': 1}
>>> d['many'] = d.get('many',0) + 1
>>> d
{'this': 1, 'is': 1, 'a': 1, 'word': 1, 'string': 1, 'having': 1, 'many': 1}
>>> d['many'] = d.get('many',0) + 1
>>> d
{'this': 1, 'is': 1, 'a': 1, 'word': 1, 'string': 1, 'having': 1, 'many': 2}
>>> d['word'] = d.get('word',0) + 1
>>> d
{'this': 1, 'is': 1, 'a': 1, 'word': 2, 'string': 1, 'having': 1, 'many': 2}'''









        
        

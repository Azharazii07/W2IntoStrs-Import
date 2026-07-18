# Caeser Cipher in crytography 
s = 'abcdefghijklmnopqrstuvwxyz' 
print("\'"+s[0]+"\' ",s.index(s[-1]),sep="") 
i , k = 0 , 1 
lim = 26 
print(i%lim , s[i%lim]) # a-z 0-25 and 26-51 and so on...... 
r = "azhar" 
t = '' 
t = t+s[ ( s.index( r[i] ) + k )%lim] 
t = t+s[ ( s.index( r[i+1] ) + k )%lim] 
t = t+s[ ( s.index( r[i+2] ) + k )%lim] 
t = t+s[ ( s.index( r[i+3] ) + k )%lim] 
t = t+s[ ( s.index( r[i+4] ) + k )%lim] 
print(t)

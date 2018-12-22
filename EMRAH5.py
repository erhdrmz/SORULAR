def denklem1(x):
    return x*(x+1)/2
def denklem2(x):
    return x*((3*x)-1)/2
def denklem3(x):
    return x*((2*x)-1)
a = b = c = 1
denklem_a = denklem1(a)
denklem_b = denklem2(b)
denklem_c = denklem3(c)
print("Sonuçlar")
while True:
  if denklem_a == denklem_b and denklem_b == denklem_c:
    print("A({}) = B({}), C({}) = {}".format(a,b,c,denklem_a))
  if denklem_a <= denklem_b and denklem_a <= denklem_c:
    a += 1
    denklem_a = denklem1(a)
  elif denklem_b <= denklem_a and denklem_b <= denklem_c:
    b += 1
    denklem_b = denklem2(b)
  elif denklem_c <= denklem_a and denklem_c <= denklem_b:
    c += 1
    denklem_c = denklem3(c)
  else:
    print("SONUÇ YOK !")
    assert(False);

example=set()
print(dir(example))
print(help(example.add))
print(dir())
example.add(False)
example.add(42)
example.add(0)
example.add(3.141)
example.add(0)
example.add("Thorium")
example.add(False)
print(example)
print(2 not in example)
print(0 in example)
primes=[2,3,4,5,6,7,8]
primes.append(2)
primes.insert(0,20)
print(primes)
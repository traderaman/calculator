
print("Hey dude! I love calculating;)")
print\
('1.Add; 2.Substract; 3.Multiply or 4.Divide?')
cal = (input("What do you want me to do: "))
if cal == '1':
    a = float((input('Okay, insert first number: ')))
    b = float((input('Done, insert second number: ')))
    c = (a+b)
    print(f'Adding {a} with {b} results {c}')
    print('Phew! That was so simple.')
elif cal == '2':
    d = float((input('Okay, insert first number: ')))
    e = float((input('Done, insert second number: ')))
    f = (d-e)
    print(f'Substracting {e} from {d} results {f}')
    print('Ask something more tougher,atleast!')
elif cal == '3':
    g = float((input('Okay, insert first number: ')))
    h = float((input('Done, insert second number: ')))
    i= (g*h)
    print(f'Multiplying {g} with {h} results {i}')
    print('Well! multiplication is my cup of tea;)')
elif cal == '4':
    j = float((input('Okay, insert first number: ')))
    k = float((input('Done, insert second number: ')))
    l= float(j/k)
    m = "{:.2f}".format(l)
    print(f'Dividing {j} by {k} results {m}')
    print('Try dividing by zero, LOL.')
else:
    print('Better you start with Homeschooling again xD')

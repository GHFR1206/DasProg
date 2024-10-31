a = 2
b = 32
print('a =', a, '=', format(a, '08b'))
print('b =', b, '=', format(b, '08b'), '\n')

#AND &
print('and [&]')
print(f'a & b = {a & b}')
print(format(a, '08b'), '&', format(b, '08b'), '=', format(a & b, '08b'),
'\n')
#OR |
print('or [|]')
print(f'a | b = {a | b}')
print(format(a, '08b'), '|', format(b, '08b'), '=', format(a | b, '08b'),
'\n')
#XOR ^
print('xor [^]')
print(f'a ^ b = {a ^ b}')
print(format(a, '08b'), '^', format(b, '08b'), '=', format(a ^ b, '08b'),
'\n')
#NOT ~
print('not [~]')
print(f'~a ~b = {~a, ~b}')
print('~' + format(a, '08b'), '~' + format(b, '08b'), '=', format(~a,
'08b'), format(~b, '08b'), '\n')
#SHIFT RIGHT >>
print('shift right [>>]')
print(f'a >> b = {a >> b}')
print(format(a, '08b'), '>>', format(b, '08b'), '=', format(a >> b,
'08b'), '\n')
#SHIFT LEFT<<
print('shift left [<<]')
print(f'a << b = {a << b}')
print(format(b, '08b'), '<<', format(a, '08b'), '=', format(b << a,
'08b'), '\n')
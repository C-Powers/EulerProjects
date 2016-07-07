#simple generator function!!!!!!


def simple_gen_fun():
    yield 1
    yield 2
    yield 3

for value in simple_gen_fun():
  print value


our_gen = simple_gen_fun()

print next(our_gen)

print next(our_gen)

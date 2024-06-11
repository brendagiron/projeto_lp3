from validate_docbr import CPF

cpf = CPF()


print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate('168.079.481-74'))
print(cpf.validate('95842125080'))

cpfs = [
    '168.079.481-74',
    '95842125080',
    '755664'
]

print(cpf.validate_list(cpfs))


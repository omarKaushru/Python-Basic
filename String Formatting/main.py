
# Python String Formatting Basics
# Old way of formatting strings  -- C style

print('I am %s' % 'Umar')
print('I am %s and I am %d years old' % ('Hasan', 65))
print('I am %s and I live in %s!' % ('Shamsun Nahar', 'Haven'))

name = 'Umar'
age = 28
profession = 'Engineer'
earning = 28374.23323

print('Hi I am %s and I am %d years old. I am an %s and I earn %.2f$' % (name, age, profession, earning))

# A slightly better way of formatting strings

print('I am {} and I am very {}.'.format('Omar', 'bad'))
# changing the output order
print('I am {0} and I am very {1}.'.format(name, 'bad'))
print('I am {1} and I am very {0}.'.format(name, 'bad'))

# A much better of way of formatting strings

food = 'Beep'
language = 'Python'
print(f'I am {name} and I eat {food}. I don\'t believe in {language} haters.\nAnd {2**3} == {8}.')

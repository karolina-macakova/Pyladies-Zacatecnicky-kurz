# Tento program počítá obvod a obsah čtverce o zadane strane a kruhu o stejnem polomeru

strana = float(input('Zadej stranu čtverce v centimetrech: '))
print('Obvod čtverce se stranou', strana, 'cm je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'cm je', strana * strana, 'cm2')

polomer = strana
pi = 3.1415926
print('Obvod kruhu o polomeru', polomer, 'cm je', 2 * polomer * pi, 'cm')
print('Obsah kruhu o polomeru', polomer, 'cm je', pi * polomer * polomer, 'cm2')
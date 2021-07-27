#Operador Ternário
#condition_true if condition else false_condition


name = 'WanDEV'
check_true = 'Name Checked Sucessfuly!'
check_false = 'Name Checked Error!'
alert = 'Name Checked Sucessfuly!' if bool(name) else 'Name Checked Error!'
print(alert)

is_magic = 'Yes!' if name[0] == 'W' else 'No.'
print(is_magic)
# Preencher textos de formas automatizadas
from string import Template

# format
name1 = 'Wanderson Fontes'
print(f'\nSoftware Developer\nName: {name1}'+'\n'+('-'*50))

# Template
templ = Template("\nSoftware Developer\nName: ${name}")
# Transform sentence into a template
templUpdate = templ.substitute(name='Wanderson Fontes')
print(templUpdate+'\n'+('-'*50))

# Test
templ1 = Template("Hi, how are you?\nMy name is ${name}!\nI'm ${work}")
templUpdate1 = templ1.substitute(name='Wanderson', work='Developer')
print(templUpdate1+'\n'+('-'*50))

templ2 = Template("I have a ${pet} called ${namePet}")
templUpdate2 = templ2.substitute(pet='Dog', namePet='Lyon')
print(templUpdate2+'\n'+('-'*50))

# Use dictionary
# The benefit of using the dictionary is that it makes the code cleaner.
# In addition to helping with possible future adjustments, as they are made in just one place in the code.

data = {
    'name': 'Wanderson',
    'work': 'Developer',
    'level': 'Full'
}

templ3 = Template("Who am I?\nMy name is ${name}.\nI work with ${work}.\nMy level is ${level}!")
templUpdate3 = templ3.substitute(data)
print(templUpdate3+'\n'+('-'*50))





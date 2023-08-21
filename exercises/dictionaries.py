# dictionary = a changeable, unordered collection of unique key: value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC', 
            'India':'New Dehli',
            'China':'Beijing', 
            'Russia': 'Moscow'}

print(capitals.keys())
print(capitals.values())
print(capitals.items())

print(capitals['India'])
print(capitals.get('USA'))
  
capitals.update({'Germany': 'Berlin'})
capitals.update({'Brazil': 'Brazilia'})

for key,value in capitals.items():
    print(value)
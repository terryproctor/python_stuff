glossary = {
    'tuple' : 'A tuple is a finite ordered list (sequence) of elements. An n-tuple is a sequence (or ordered list) of n elements, where n is a non-negative integer. There is only one 0-tuple, referred to as the empty tuple. An n-tuple is defined inductively using the construction of an ordered pair.',
    'dictionary' : 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.',
    'elif' : 'Short for else if. It allows us to check for multiple expressions.',
    'list' : 'List is a collection which is ordered and changeable. Allows duplicate members.',
    'set': 'A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.',
    'operator' : 'Operators are used to perform operations on variables and values.', 
    'comments' :'Comments can be used to explain Python code.',
    'variables': 'Variables are containers for storing data values.',
    'casting': 'There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.',
}
#print(glossary['tuple'])
#print(f"\nThe meaning of Tuple:\n\t{glossary.get('tuple')}\n")
#print(f"The meaning of Dictionary:\n\t{glossary.get('dictionary')}\n")
#print(f"The meaning of elif:\n\t{glossary.get('elif')}\n")
#print(f"The meaning of list:\n\t{glossary.get('list')}\n")

print(glossary.keys)

for key, value in glossary.items():
    print(f"\nThe meaning of {key}:\n\t{value}\n")


print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = raw_input("Enter a word:")
if len(original) > 0:
    print (original)
else:
    print ("empty")


pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    
else:
    print 'empty'

new_word = new_word[1:len(new_word)]
print new_word

"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True


    not is evaluated first;
    and is evaluated next;
    or is evaluated last.


"""

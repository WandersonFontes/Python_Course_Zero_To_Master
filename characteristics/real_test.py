# Any object returns True

# Values ​​that return the value False
# False or None
# Zero in numerical values: 0, 0.0, 0j
# Empty strings and collections: '', [], {}
# Set and empty intervals: set(), range(0)
test1 = []
test2 = {}
test3 = ''
test4 = set()
test5 = range(0)

# print(' test1: ',bool(test1),'\n','test2: ',bool(test2))
# print(' test3: ',bool(test3),'\n','test4: ',bool(test4),'\n', 'test5: ',bool(test5),'\n')

# If all of objects return True how to make an object return False
# Representing an object that returns False by default


class FalseObject:

    def __bool__(self):
        return False

    def __len__(self):
        return 0

#print(bool(FalseObject))
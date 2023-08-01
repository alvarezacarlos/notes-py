#***** variables
'''
    reserved memory location, this means that when you create a variable you reserve some space in the memory.
    based on the datatype of the variable, python interpreter allocates memory and decides what can be stored in the reserved memory.
'''

'''deleting a variable'''
c = 3
del c

'''Multiple Assignment'''
a = b = c = 100
print (a)
print (b)
print (c)


a,b,c = 1,2,"Zara Ali"
print (a)
print (b)
print (c)


'''Variable Names
    A variable name must start with a letter or the underscore characters
    A variable name cannot start with a number or any special character like $, (, * % etc.
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Python variable names are case-sensitive which means Name and NAME are two different variables in Python.
    Python reserved keywords cannot be used naming the variable.
'''

'''local variables
python local variables are defined inside a function. we can not access variable outside the function.
def say_name():
    name = 'Peter'
    print(name)
print(name)  # this will show an error


Below is how we can use local variables as the function returns it: 
def say_name():
    name = 'Carlos'
    print(name)
    return name

print(say_name())
'''


'''global variables
Any variable created outside a function can be accessed within any function and so they have global scope.
'''

#***** datatypes
'''datatypes are used to define what is the type of the data we are going to store in that memory served space (variable/constant)
        Numeric:
            int
            long (long integers, they can also be represented in octal and hexadecimal)
            float (floating point real values)
            complex (complex numbers)
        String:
            str
        Sequence:
            list
            tuple
            range
        Binary:
            bytes
            bytearray
            memoryview
        Mapping:
            dict
        Boolean:
            bool
        Set:
            set
            frozenset
        None
            NoneType
        Date types

numeric:
    python numeric data types store numeric values. Number objects are created when you assign a value to them.
    number: 
        number objects are created when you assign a value to them.
        var1 = 1
        var2 = 10
        var = 10.0233

        Here are some examples of numbers:
        int: 10, 100, -786, 80, -490, -0x260, 0x69
        long: 51924361L, -0x19323L, 0122L, 0xDEFABCECBDAECBFBAEl, 535633629843L, -052318172735L, -4721885298529L
        float: 0, 15.2, -21.9, 32.3+e18, -90, -3.25E+101, 70.2-E12
        complex: 3.14j, 45.j, 9.322e-36j, .876j, -.6545+0J, 3e+26J, 4.53e-7j

        Python allows you to use a lowercase l with long, but it is recommended that you use only an uppercase L to avoid confusion with the number 1. Python displays long integers with an uppercase L.

        A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj, where x and y are the real numbers and j is the imaginary unit.

        Number data types store numeric values. They are immutable data types, means that changing the value of a number data type results in a newly allocated object.
    
    Mathematical Functions:
        abs(x)
            The absolute value of x: the (positive) distance between x and zero.
        ceil(x)
            The ceiling of x: the smallest integer not less than x
        cmp(x, y)
            -1 if x < y, 0 if x == y, or 1 if x > y
        exp(x)
            The exponential of x: ex
        fabs(x)
            The absolute value of x.
        floor(x)
            The floor of x: the largest integer not greater than x
        log(x)
            The natural logarithm of x, for x> 0
        log10(x)
            The base-10 logarithm of x for x> 0.
        max(x1, x2,...)
            The largest of its arguments: the value closest to positive infinity
        min(x1, x2,...)
            The smallest of its arguments: the value closest to negative infinity
        modf(x)
            The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.
        pow(x, y)
            The value of x**y.
        round(x [,n])
            x rounded to n digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.
        sqrt(x)
            The square root of x for x > 0

    Random Number Functions:
        Random numbers are used for games, simulations, testing, security, and privacy applications. Python includes following functions that are commonly used.
        choice(seq)
            A random item from a list, tuple, or string.
        randrange ([start,] stop [,step])
            A randomly selected element from range(start, stop, step)
        random()
            A random float r, such that 0 is less than or equal to r and r is less than 1
        seed([x])
            Sets the integer starting value used in generating random numbers. Call this function before calling any other random module function. Returns None.
        shuffle(lst)
            Randomizes the items of a list in place. Returns None.
        uniform(x, y)
            A random float r, such that x is less than or equal to r and r is less than y

    Trigonometric Functions:
        acos(x)
            Return the arc cosine of x, in radians.
        asin(x)
            Return the arc sine of x, in radians.
        atan(x)
            Return the arc tangent of x, in radians.
        atan2(y, x)
            Return atan(y / x), in radians.
        cos(x)
            Return the cosine of x radians.
        hypot(x, y)
            Return the Euclidean norm, sqrt(x*x + y*y).
        sin(x)
            Return the sine of x radians.
        tan(x)
            Return the tangent of x radians.
        degrees(x)
            Converts angle x from radians to degrees.
        radians(x)
            Converts angle x from degrees to radians.

    Constants & Description
        pi
            The mathematical constant pi.
        e
            The mathematical constant e.


string: 
    contiguous set of characters represented in the quotation marks.
    Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.
    The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator in Python

    str = 'Hello World!'
    print (str)          # Prints complete string
    print (str[0])       # Prints first character of the string
    print (str[2:5])     # Prints characters starting from 3rd to 5th
    print (str[2:])      # Prints string starting from 3rd character
    print (str * 2)      # Prints string two times
    print (str + "TEST") # Prints concatenated string


    Updating Strings:
        Mutabilidad in Python

    Escape Characters:
        Backslash   Hexadecimal     Description
        notation    character   
        \a  0x07    Bell or alert
        \b  0x08    Backspace
        \cx         Control-x
        \C-x        Control-x
        \e          0x1b            Escape
        \f          0x0c            Formfeed
        \M-\C-x                     Meta-Control-x
        \n          0x0a            Newline
        \nnn                        Octal notation, where n is in the range 0.7
        \r          0x0d            Carriage return
        \s          0x20            Space
        \t          0x09            Tab
        \v          0x0b            Vertical tab
        \x          Character x
        \xnn                        Hexadecimal notation, where n is in the range 0.9, a.f, or A.F

    String Special Operators:    
        +           
            Concatenation - Adds values on either side of the operator                          
            a + b will give HelloPython
        *           
            Repetition - Creates new strings, concatenating multiple copies of the same string  
            a*2 will give -HelloHello
        []          
            Slice - Gives the character from the given index                                    
            a[1] will give e
        [ : ]       
            Range Slice - Gives the characters from the given range                             
            a[1:4] will give ell
        in          
            Membership - Returns true if a character exists in the given string                 
            H in a will give 1
        not in      
            Membership - Returns true if a character does not exist in the given string         
            M not in a will give 1
        r/R         
            Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.                                                     
            print r'\n' prints \n and print R'\n'prints \n
        %   
            Format - Performs String formatting 

    String Formatting Operator:
        print("My name is %s and weight is %d kg!" % ('Zara', 21))

        Here is the list of complete set of symbols which can be used along with %

        %c  character
        %s  string conversion via str() prior to formatting
        %i  signed decimal integer
        %d  signed decimal integer
        %u  unsigned decimal integer
        %o  octal integer
        %x  hexadecimal integer (lowercase letters)
        %X  hexadecimal integer (UPPERcase letters)
        %e  exponential notation (with lowercase 'e')
        %E  exponential notation (with UPPERcase 'E')
        %f  floating point real number
        %g  the shorter of %f and %e
        %G  the shorter of %f and %E

    Other supported symbols and functionality:
        *	    argument specifies width or precision
        -	    left justification
        +	    display the sign
        <sp>	leave a blank space before a positive number
        #	    add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
        0	    pad from left with zeros (instead of spaces)
        %	    '%%' leaves you with a single literal '%'
        (var)	mapping variable (dictionary arguments)
        m.n.	m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)

    Unicode String:
        Normal strings in Python are stored internally as 8-bit ASCII, while Unicode strings are stored as 16-bit Unicode. This allows for a more varied set of characters, including special characters from most languages in the world. 
        
        print u'Hello, world!'

    Built-in String Methods:
        capitalize()
            Capitalizes first letter of string
        center(width, fillchar)
            Returns a space-padded string with the original string centered to a total of width columns.
        count(str, beg= 0,end=len(string))
            Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
        decode(encoding='UTF-8',errors='strict')
            Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.
        encode(encoding='UTF-8',errors='strict')
            Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.
        endswith(suffix, beg=0, end=len(string))
            Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
        expandtabs(tabsize=8)
            Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.
        find(str, beg=0 end=len(string))
            Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
        index(str, beg=0, end=len(string))
            Same as find(), but raises an exception if str not found.
        isalnum()
            Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
        isalpha()
            Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
        isdigit()
            Returns true if string contains only digits and false otherwise.
        islower()
            Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
        isnumeric()
            Returns true if a unicode string contains only numeric characters and false otherwise.
        isspace()
            Returns true if string contains only whitespace characters and false otherwise.
        istitle()
            Returns true if string is properly "titlecased" and false otherwise.
        isupper()
            Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.
        join(seq)
            Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
        len(string)
            Returns the length of the string
        ljust(width[, fillchar])
            Returns a space-padded string with the original string left-justified to a total of width columns.
        lower()
            Converts all uppercase letters in string to lowercase.
        lstrip()
            Removes all leading whitespace in string.
        maketrans()
            Returns a translation table to be used in translate function.
        max(str)
            Returns the max alphabetical character from the string str.
        min(str)
            Returns the min alphabetical character from the string str.
        replace(old, new [, max])
            Replaces all occurrences of old in string with new or at most max occurrences if max given.
        rfind(str, beg=0,end=len(string))
            Same as find(), but search backwards in string.
        rindex( str, beg=0, end=len(string))
            Same as index(), but search backwards in string.
        rjust(width,[, fillchar])
            Returns a space-padded string with the original string right-justified to a total of width columns.
        rstrip()
            Removes all trailing whitespace of string.
        split(str="", num=string.count(str))
            Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
        splitlines( num=string.count('\n'))
            Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.
        startswith(str, beg=0,end=len(string))
            Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.
        strip([chars])
            Performs both lstrip() and rstrip() on string.
        swapcase()
            Inverts case for all letters in string.
        title()
            Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
        translate(table, deletechars="")
            Translates string according to translation table str(256 chars), removing those in the del string.
        upper()
            Converts lowercase letters in string to uppercase.
        zfill (width)
            Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).
        isdecimal()
            Returns true if a unicode string contains only decimal characters and false otherwise.

sequence: 
    list:
        To some extent, Python lists are similar to arrays in C. One difference between them is that all the items belonging to a Python list can be of different data type where as C array can store elements related to a particular data type.
        The values stored in a Python list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.

        list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
        tinylist = [123, 'john']
        print (list)            # Prints complete list
        print (list[0])         # Prints first element of the list
        print (list[1:3])       # Prints elements starting from 2nd till 3rd 
        print (list[2:])        # Prints elements starting from 3rd element
        print (tinylist * 2)    # Prints list two times
        print (list + tinylist) # Prints concatenated lists
    
        Basic List Operations:
            len([1, 2, 3])	                3	                            Length
            [1, 2, 3] + [4, 5, 6]	        [1, 2, 3, 4, 5, 6]	            Concatenation
            ['Hi!'] * 4	                    ['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
            3 in [1, 2, 3]	                TRUE	                        Membership
            for x in [1, 2, 3]: print x,	1 2 3	                        Iteration

        Indexing, Slicing, and Matrixes:
            L[2]	SPAM!	            Offsets start at zero
            L[-2]	Spam	            Negative: count from the right
            L[1:]	['Spam', 'SPAM!']	Slicing fetches sections

        Built-in List Functions & Methods:
            sorted(names) == sorted(colors)
                Compares elements of both lists.
                colors  = ['red', 'yellow', 'black']
                names = ['Carlos', 'Jhon', 'Peter']
                result = True if sorted(names) == sorted(colors) else False
                print(result)
            len(list)
                Gives the total length of the list.
            max(list)
                Returns item from the list with max value.
            min(list)
                Returns item from the list with min value.
            list(seq)
                Converts a tuple into list.
                my_tuple = ('Mark', 'Jhon', 'Pered')
                my_tuple_2 = list(my_tuple)
                my_tuple_2[0] = 'Carlos'
                print (my_tuple_2)

        Python includes following list methods:
            list.append(obj)
                Appends object obj to list
                aList = [123, 'xyz', 'zara', 'abc']
                print(aList)
                aList.append(2009)
                print(aList)
            list.count(obj)
                Returns count of how many times obj occurs in list
            list.extend(seq)
                Appends the contents of seq to list
                aList = [123, 'xyz', 'zara', 'abc', 123]
                print(aList)
                bList = [2009, 'manni']
                aList.extend(bList)
                print(aList)
            list.index(obj)
                Returns the lowest index in list that obj appears
            list.insert(index, obj)
                Inserts object obj into list at offset index
                aList = [123, 'xyz', 'zara', 'abc']
                print(aList)
                aList.insert( 3, 2009)
                print(aList)
            list.pop(obj=list[-1])
                Removes and returns last object or obj from list
                aList = [123, 'xyz', 'zara', 'abc']
                print(aList)
                x = aList.pop()
                print(aList)
                y = aList.pop(2)
                print(aList)
                print(x)
                print(y)
            list.remove(obj)
                Removes object obj from list
                aList = [123, 'xyz', 'zara', 'abc', 'xyz']
                aList.remove('xyz')
                print(aList)
                aList.remove('abc')
                print(aList)
            list.reverse()
                Reverses objects of list in place
            list.sort([func])
                Sorts objects of list, use compare func if given


    tuple:
        A Python tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.
        The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. 
        
        tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
        tinytuple = (123, 'john')
        print (tuple)               # Prints the complete tuple
        print (tuple[0])            # Prints first element of the tuple
        print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
        print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
        print (tinytuple * 2)       # Prints the contents of the tuple twice
        print (tuple + tinytuple)   # Prints concatenated tuples

        Basic Tuples Operations
            len((1, 2, 3))	                3	                            Length
            (1, 2, 3) + (4, 5, 6)	        (1, 2, 3, 4, 5, 6)	            Concatenation
            ('Hi!',) * 4	                ('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
            3 in (1, 2, 3)	                True	                        Membership
            for x in (1, 2, 3): print x,	1 2 3	                        Iteration

        Indexing, Slicing, and Matrixes
            L[2]	'SPAM!'	            Offsets start at zero
            L[-2]	'Spam'	            Negative: count from the right
            L[1:]	['Spam', 'SPAM!']	Slicing fetches sections

        No Enclosing Delimiters
            Any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short examples
            print 'abc', -4.24e93, 18+6.6j, 'xyz';
            x, y = 1, 2;
            print "Value of x , y : ", x,y;

        Built-in Tuple Functions
        Compares elements of both tuples.
            t1 = ('carlos', 'mark')
            t2 = ('jhon', 'juan')
            x = True if t1 == t2 else False
            print(x)
        len(tuple)
            Gives the total length of the tuple.
        max(tuple)
            Returns item from the tuple with max value.
        min(tuple)
            Returns item from the tuple with min value.
        tuple(seq)
            Converts a list into tuple.


    range:
        Python range() is an in-built function in Python which returns a sequence of numbers starting from 0 and increments to 1 until it reaches a specified number.
        We use range() function with for and while loop to generate a sequence of numbers. Following is the syntax of the function:
        range(start, stop, step)
        Here is the description of the parameters used:
        start: Integer number to specify starting position, (Its optional, Default: 0)
        stop: Integer number to specify starting position (It's mandatory)
        step: Integer number to specify increment, (Its optional, Default: 1)

        for i in range(5):
            print(i)

        for i in range(1, 5):
        print(i)

        for i in range(1, 5, 2):
        print(i)

        list = ['Jhon', 'Peter', 'Mark']
        for i in range(1, len(list), 1):
                print(list[i])   

        
mapping
    dict:
        Python dictionaries are kind of hash table type.
        They work like associative arrays or hashes found in Perl and consist of key-value pairs.
        A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.
        Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). 

        dict = {}
        dict['one'] = "This is one"
        dict[2]     = "This is two"

        tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
        print (dict['one'])       # Prints value for 'one' key
        print (dict[2])           # Prints value for 2 key
        print (tinydict)          # Prints complete dictionary
        print (tinydict.keys())   # Prints all the keys
        print (tinydict.values()) # Prints all the values

        dict[2]     = "This is two but with a new value"
        print(dict[2])

        Python dictionaries have no concept of order among elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.

        Accessing Values in Dictionary:
            dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
            print "dict['Name']: ", dict['Name']
            print "dict['Age']: ", dict['Age']

        Updating Dictionary:
            dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
            dict['Age'] = 8; # update existing entry
            dict['School'] = "DPS School"; # Add new entry
            print "dict['Age']: ", dict['Age']
            print "dict['School']: ", dict['School']
        
        Delete Discionary Elements:
            dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
            print(dict)
            del dict['Name']; # remove entry with key 'Name'
            print(dict)
            dict.clear();     # remove all entries in dict
            print(dict)
            del dict ;        # delete entire dictionary

        Properties of Dictionary Keys:
            (a) More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins.
            (b) Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed.

        Built-in Dictionary Functions & Methods:            
            Compares elements of both dict.
                dict1 = {'Name': 'Zara', 'Age': 7}
                dict2 = {'Name': 'Mahnaz', 'Age': 27}
                dict3 = {'Name': 'Abid', 'Age': 27}
                dict4 = {'Name': 'Zara', 'Age': 7}
                result = True if dict1 == dict2 else False
                print(result)
                result = True if dict1 == dict4 else False
                print(result)
            len(dict)
                Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
            str(dict)
                Produces a printable string representation of a dictionary
            type(variable)
                Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.
        
        Dictionary Methods:
            dict.clear()
                Removes all elements of dictionary dict
            dict.copy()
                Returns a shallow copy of dictionary dict
                dict1 = {'Name': 'Zara', 'Age': 7}
                dict2 = dict1.copy()
                print(dict1)
                print(dict2)

                dict1['Name'] = 'Jhon'
                print(dict1)
                print(dict2)
            dict.fromkeys()
                Create a new dictionary with keys from seq and values set to value.
                dict1 = {'Name': 'Zara', 'Age': 7}
                dict3 = dict.fromkeys(dict1.keys(), 10)
                print(dict3)

                seq = ('name', 'age', 'sex')
                dict1 = dict.fromkeys(seq, 10)
                print(dict1)
            dict.get(key, default=None)
                For key key, returns value or default if key not in dictionary
                seq = ('name', 'age', 'sex')
                dict1 = dict.fromkeys(seq, 10)
                print(dict1)

                print(dict1.get('name'))
                print(dict1['name'])
            has_key(key) not longer used. We use in opertator in python 3
                Returns true if key in dictionary dict, false otherwise
                seq = ('name', 'age', 'sex')
                dict1 = dict.fromkeys(seq, 10)
                print((True if 'name' in dict1 else False))
            dict.items()
                Returns a list of dict's (key, value) tuple pairs
                seq = ('name', 'age', 'sex')
                dict1 = dict.fromkeys(seq, 10)
                print(dict1.items())
            dict.keys()
                Returns list of dictionary dict's keys
                
                seq = ('name', 'age', 'sex')
                dict1 = dict.fromkeys(seq, 10)

                items = list(dict1.items())
                keys = list(dict1.keys())
                values = list(dict1.values())

                print(type(items))
                print(type(keys))

                print(items[0])
                print(keys[1])
                print(values[2])

                for item in items: 
                    print(item)

                for item in keys: 
                    print(item)

                for item in values: 
                    print(item)
            dict.values()
                Returns list of dictionary dict's values
            dict.setdefault(key, default=None)
                allows us to add items to a dictionay with a default value. if exists it does keeps the value already assigned
                dict = {'Name': 'Zara', 'Age': 7}
                dict.setdefault('Age', None)
                dict.setdefault('Sex', None)
                print(dict)
            dict.update(dict2)
                Adds dictionary dict2's key-values pairs to dict
                dict1 = {'Name': 'Zara', 'Age': 7}
                dict1.update({'contry': 'Panama'})
                print(dict1)
                            

bool:    
    Python bool() function allows you to evaluate the value of any expression and returns either True or False based on the expression.

    # Returns false as a is not equal to b
    a = 2
    b = 4
    print(bool(a==b))

    # Following also prints the same
    print(a==b)

    # Returns False as a is None
    a = None
    print(bool(a))

    # Returns false as a is an empty sequence
    a = ()
    print(bool(a))

    # Returns false as a is 0
    a = 0.0
    print(bool(a))

    # Returns false as a is 10
    a = 10
    print(bool(a))

Date types:
    modules: 
        time
        datetime
        calendar
        pytz
        dateutil
'''

#***** datatypes convertions
'''
To convert data between different Python data types, you simply use the type name as a function.

Conversion to int
    a = int(1)     # a will be 1
    b = int(2.2)   # b will be 2
    c = int("3")   # c will be 3

Conversion to float
    a = float(1)     # a will be 1.0
    b = float(2.2)   # b will be 2.2
    c = float("3.3") # c will be 3.3

Conversion to string
    a = str(1)     # a will be "1" 
    b = str(2.2)   # b will be "2.2"
    c = str("3.3") # c will be "3.3"

Data Type Conversion Functions
    int(x [,base])
        Converts x to an integer. base specifies the base if x is a string.
    long(x [,base] )
        Converts x to a long integer. base specifies the base if x is a string.
    float(x)
        Converts x to a floating-point number.
    complex(real [,imag])
        Creates a complex number.
    str(x)
        Converts object x to a string representation.
    repr(x)
        Converts object x to an expression string.
    eval(str)
        Evaluates a string and returns an object.
    tuple(s)
        Converts s to a tuple.
    list(s)
        Converts s to a list.
    set(s)
        Converts s to a set.
    dict(d)
        Creates a dictionary. d must be a sequence of (key,value) tuples.
    frozenset(s)
        Converts s to a frozen set.
    chr(x)
        Converts an integer to a character.
    unichr(x)
        Converts an integer to a Unicode character.
    ord(x)
        Converts a single character to its integer value.
    hex(x)
        Converts an integer to a hexadecimal string.
    oct(x)
        Converts an integer to an octal string.
'''

#operators
'''
    Arithmetic Operators
    Comparison (Relational) Operators
    Assignment Operators
    Logical Operators
    Bitwise Operators
    Membership Operators
    Identity Operators

Arithmetic Operators
    Python arithmetic operators are used to perform mathematical operations on numerical values. These operations are Addition, Subtraction, Multiplication, Division, Modulus, Expoents and Floor Division.
    +       Addition            10 + 20 = 30
    -       Subtraction         20 – 10 = 10
    *       Multiplication      10 * 20 = 200
    /       Division            20 / 10 = 2
    %       Modulus             22 % 10 = 2
    **      Exponent            4**2 = 16
    //      Floor Division      9//2 = 4

Comparison Operators
    ==	Equal	                    4 == 5 is not true.
    !=	Not Equal	                4 != 5 is true.
    >	Greater Than	            4 > 5 is not true.
    <	Less Than	                4 < 5 is true.
    >=	Greater than or Equal to	4 >= 5 is not true.
    <=	Less than or Equal to	    4 <= 5 is true.

Assignment Operators
    =	Assignment Operator	            a = 10
    +=	Addition Assignment	            a += 5 (Same as a = a + 5)
    -=	Subtraction Assignment	        a -= 5 (Same as a = a - 5)
    *=	Multiplication Assignment	    a *= 5 (Same as a = a * 5)
    /=	Division Assignment	            a /= 5 (Same as a = a / 5)
    %=	Remainder Assignment	        a %= 5 (Same as a = a % 5)
    **=	Exponent Assignment	            a **= 2 (Same as a = a ** 2)
    //=	Floor Division Assignment	    a //= 3 (Same as a = a // 3)

Bitwise Operators
    Bitwise operator works on bits and performs bit by bit operation. Assume if a = 60; and b = 13; Now in the binary format their values will be 0011 1100 and 0000 1101 respectively. Following table lists out the bitwise operators supported by Python language with an example each in those, we use the above two variables (a and b) as operands

    a = 0011 1100
    b = 0000 1101

    a&b = 12 (0000 1100)
    a|b = 61 (0011 1101)
    a^b = 49 (0011 0001)
    ~a  = -61 (1100 0011)
    a << 2 = 240 (1111 0000)
    a>>2 = 15 (0000 1111)

There are following Bitwise operators supported by Python language
    &	    Binary AND	            Sets each bit to 1 if both bits are 1
    |	    Binary OR	            Sets each bit to 1 if one of two bits is 1
    ^	    Binary XOR	            Sets each bit to 1 if only one of two bits is 1
    ~	    Binary Ones             Complement	Inverts all the bits
    <<	    Binary Left Shift	    Shift left by pushing zeros in from the right and let the leftmost bits fall off
    >>	    Binary Right Shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

    EXAMPLES:
        a = 60            # 60 = 0011 1100
        b = 13            # 13 = 0000 1101

    # Binary AND
        c = a & b        # 12 = 0000 1100
        print ("a & b : ", c)

    # Binary OR
        c = a | b        # 61 = 0011 1101
        print ("a | b : ", c)

    # Binary XOR
        c = a ^ b        # 49 = 0011 0001
        print ("a ^ b : ", c)

    # Binary Ones Complement
        c = ~a;           # -61 = 1100 0011
        print ("~a : ", c)

    # Binary Left Shift
        c = a << 2;       # 240 = 1111 0000
        print ("a << 2 : ", c)

    # Binary Right Shift
        c = a >> 2;       # 15 = 0000 1111
        print ("a >> 2 : ", c)

    This produce the following result:
        a & b :  12
        a | b :  61
        a ^ b :  49
        ~a :  -61
        a >> 2 :  240
        a >> 2 :  15

Logical Operators
    and
    or
    not

Membership Operators
    Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples:
    in
    not in

Identity Operators
    Identity operators compare the memory locations of two objects.
    is
    is not

    Examples:
    a = 20
    b = 20

    if ( a is b ):
    print "Line 1 - a and b have same identity"
    else:
    print "Line 1 - a and b do not have same identity"

    if ( id(a) == id(b) ):
    print "Line 2 - a and b have same identity"
    else:
    print "Line 2 - a and b do not have same identity"

    b = 30
    if ( a is b ):
    print "Line 3 - a and b have same identity"
    else:
    print "Line 3 - a and b do not have same identity"

    if ( a is not b ):
    print "Line 4 - a and b do not have same identity"
    else:
    print "Line 4 - a and b have same identity"
    When you execute the above program it produces the following result −

    Line 1 - a and b have same identity
    Line 2 - a and b have same identity
    Line 3 - a and b do not have same identity
    Line 4 - a and b do not have same identity


Operators Precedence
    Operator precedence affects how an expression is evaluated.
    For example, x = 7 + 3 * 2; here, x is assigned 13, not 20 because operator * has higher precedence than +, so it first multiplies 3*2 and then adds into 7.
    Here, operators with the highest precedence appear at the top of the table, those with the lowest appear at the bottom.

    The following table lists all operators from highest precedence to lowest.
    **	                        Exponentiation (raise to the power)
    ~ + -	                    Complement, unary plus and minus (method names for the last two are +@ and -@)
    * / % //	                Multiply, divide, modulo and floor division
    + -	                        Addition and subtraction
    >> <<	                    Right and left bitwise shift
    &	                        Bitwise 'AND'td>
    ^ |	                        Bitwise exclusive `OR' and regular `OR'
    <= < > >=	                Comparison operators
    <> == !=	                Equality operators
    = %= /= //= -= += *= **=	Assignment operators
    is is not	                Identity operators
    in not in	                Membership operators
    not or and	                Logical operators


    EXAMPLES:
        a = 20
        b = 10
        c = 15
        d = 5
        e = 0

        e = (a + b) * c / d       #( 30 * 15 ) / 5
        print "Value of (a + b) * c / d is ",  e

        e = ((a + b) * c) / d     # (30 * 15 ) / 5
        print "Value of ((a + b) * c) / d is ",  e

        e = (a + b) * (c / d);    # (30) * (15/5)
        print "Value of (a + b) * (c / d) is ",  e

        e = a + (b * c) / d;      #  20 + (150/5)
        print "Value of a + (b * c) / d is ",  e
        When you execute the above program, it produces the following result

        Value of (a + b) * c / d is 90
        Value of ((a + b) * c) / d is 90
        Value of (a + b) * (c / d) is 90
        Value of a + (b * c) / d is 50
'''

#control structures
'''
sequence, sequential structure, sequence logic, or sequential flow:
    follows a top to bottom flow in executing a program, such that the step 1 is first to perform, followed by step 2, all the way until the last step is performed.
selection structure, selection logic, or conditional flow:
    deals with conditional statements, which mean codes are executed depending on the evaluation of conditional as being true or false. Not code is executed because there are alternative flows.
repetition structure , Loop structures, Iteration logic, or repetitive flow:
    repeat one or two program statements set by a counter.

    selection structure:
        if
        else if
        else

    repetition structure:
        while
        for        
        loop Control Statements
            break - Terminates the loop statement and transfers execution to the statement immediately following the loop.
            continue - Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
            pass - The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

        for loop examnples:
            for letter in 'Python':     # First Example
                print 'Current Letter :', letter

            fruits = ['banana', 'apple',  'mango']
            for fruit in fruits:        # Second Example
                print 'Current fruit :', fruit

            print "Good bye!"

            fruits = ['banana', 'apple',  'mango']
            for index in range(len(fruits)):
            print 'Current fruit :', fruits[index]

            print "Good bye!"


            for num in range(10,20):     #to iterate between 10 to 20
                for i in range(2,num):    #to iterate on the factors of the number
                    if num%i == 0:         #to determine the first factor
                        j=num/i             #to calculate the second factor
                        print '%d equals %d * %d' % (num,i,j)
                        break #to move to the next number, the #first FOR
                else:                  # else part of the loop
                    print num, 'is a prime number'
                    break

        while loop examples: 
            count = 0
            while (count < 9):
                print 'The count is:', count
                count = count + 1

            print "Good bye!"

            count = 0
            while count < 5:
                print count, " is  less than 5"
                count = count + 1
            else:
                print count, " is not less than 5"

'''

#functions
'defining a function'
def printme(str):
   print(str)
   return

'Pass by reference vs value'
'''All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. '''
def changeme(mylist):
   for item in [1,2,3,4] : mylist.append(item)    
   return
mylist = [10,20,30]
print(id(mylist))
changeme( mylist )
print(mylist)   
print(id(mylist))

'Function Arguments'
'''You can call a function by using the following types of formal arguments
        Required arguments:
            def printme( str ):   
                print(str)
                return
            printme('some string')
        Keyword arguments:
            the key word is restricted
            def printme( str ):   
                print(str)
                return
            printme(str =  'some string')
        Default arguments:
            def printme( str="Hello" ):   
                print(str)
                return
            printme(str =  'some string')
            printme()
        Variable-length arguments:
            def printinfo( arg1, *vartuple ):      
                print(arg1)
                print(type(vartuple))
                for item in vartuple: print(item)
                return
            printinfo( 10 )
            printinfo( 70, 60, 50 )
'''

'The Anonymous Functions'
'''These functions are called anonymous because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.
    Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
    An anonymous function cannot be a direct call to print because lambda requires an expression.
    Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.
    Although it appears that lambda's are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is by passing function stack allocation during invocation for performance reasons.

    param1 = 1
    param2 = 2
    param3 = 3
    sum = lambda arg1, arg2, arg3: arg1 + arg2 + arg3
    print(sum(param1, param2, param3))

    arg1 = 1
    arg2 = 2
    arg3 = 3
    sum = lambda : arg1 + arg2 + arg3
    print(sum())
'''


#modules
'''
    import module_name
    from module_name import function
    from module_name import *

    The reload() Function
        When the module is imported into a script, the code in the top-level portion of a module is executed only once.

        Therefore, if you want to reexecute the top-level code in a module, you can use the reload() function. The reload() function imports a previously imported module again. The syntax of the reload() function is this −

        reload(module_name)
    
    Packages in Python
        modules_structure folder (phone will be the package)

    The globals() and locals() Functions
        The globals() and locals() functions can be used to return the names in the global and local namespaces depending on the location from where they are called.

        If locals() is called from within a function, it will return all the names that can be accessed locally from that function.

        If globals() is called from within a function, it will return all the names that can be accessed globally from that function.

        The return type of both these functions is dictionary. Therefore, names can be extracted using the keys() function.
    
    The dir( ) Function
        The dir() built-in function returns a sorted list of strings containing the names defined by a module.

        The list contains the names of all the modules, variables and functions that are defined in a module. Following is a simple example −

        Live Demo
        #!/usr/bin/python

        # Import built-in module math
        import math

        content = dir(math)
        print content

    Namespaces and Scoping
        Variables are names (identifiers) that map to objects. A namespace is a dictionary of variable names (keys) and their corresponding objects (values).

        A Python statement can access variables in a local namespace and in the global namespace. If a local and a global variable have the same name, the local variable shadows the global variable.

        Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions.

        Python makes educated guesses on whether variables are local or global. It assumes that any variable assigned a value in a function is local.

        Therefore, in order to assign a value to a global variable within a function, you must first use the global statement.

        The statement global VarName tells Python that VarName is a global variable. Python stops searching the local namespace for the variable.

        For example, we define a variable Money in the global namespace. Within the function Money, we assign Money a value, therefore Python assumes Money as a local variable. However, we accessed the value of the local variable Money before setting it, so an UnboundLocalError is the result. Uncommenting the global statement fixes the problem.

        Money = 2000
        def AddMoney():
            # Uncomment the following line to fix the code:
            global Money
            Money = Money + 1
        
        print(Money)
        AddMoney()
        print(Money)
'''


#python - fiels i/o
'''
    print
        print("Python is really a great language,", "isn't it?")
    
    The input Function
        str = input("Enter your input: ")
        print("Entered Data: ", str)
    
    Opening and Closing Files:
        Syntax
            file object = open(file_name, access_mode, buffering)

            file_name
                The file_name argument is a string value that contains the name of the file that you want to access.
            access_mode
                The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. A complete list of possible values is given below in the table. This is optional parameter and the default file access mode is read (r).
            buffering
                If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).
    
    Modes of opening a file:
        r
            Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
        rb
            Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
        r+
            Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
        rb+
            Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
        w
            Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
        wb
            Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
        w+
            Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
        wb+
            Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
        a
            Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
        ab
            Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
        a+
            Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
        ab+
            Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

    The file Object Attributes:
        file.closed
            Returns true if file is closed, false otherwise.
        file.mode
            Returns access mode with which file was opened.
        file.name
            Returns name of the file.
        file.softspace
            Returns false if space explicitly required with print, true otherwise.

        fo = open("foo.txt", "wb")
        print("Name of the file: ", fo.name)
        print("Closed or not : ", fo.closed)
        print("Opening mode : ", fo.mode)

    The close() Method
        fo.close()
    
    Reading and Writing Files
        The write() Method
            The write() method writes any string to an open file. It is important to note that Python strings can have binary data and not just text.
            # Open a file
            fo = open("foo.txt", "wb")
            fo.write( "Python is a great language.\nYeah its great!!\n")
            # Close opend file
            fo.close()
        The read() Method
            The read() method reads a string from an open file. It is important to note that Python strings can have binary data. apart from text data.
            Syntax
                fileObject.read([count])
                Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of file.
            # Open a file
            fo = open("foo.txt", "r+")
            str = fo.read(10);
            print ("Read String is : ", str)
            # Close opend file
            fo.close()

    File Positions
        The tell() method tells you the current position within the file; in other words, the next read or write will occur at that many bytes from the beginning of the file.

        The seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved.

        If from is set to 0, it means use the beginning of the file as the reference position and 1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.
        # Open a file
        fo = open("foo.txt", "r+")
        str = fo.read(10)
        print("Read String is : ", str)

        # Check current position
        position = fo.tell()
        print("Current file position : ", position)

        # Reposition pointer at the beginning once again
        position = fo.seek(0, 0);
        str = fo.read(10)
        print("Again read String is : ", str)
        # Close opend file
        fo.close()

    Renaming and Deleting Files and Folders
        Python os module provides methods that help you perform file-processing operations, such as renaming and deleting files.

        The rename() Method
            The rename() method takes two arguments, the current filename and the new filename.
            os.rename(current_file_name, new_file_name)

            import os
            # Rename a file from test1.txt to test2.txt
            os.rename( "test1.txt", "test2.txt" )
        
        The remove() Method
            import os
            # Delete file test2.txt
            os.remove("text2.txt")

        The mkdir() Method
            You can use the mkdir() method of the os module to create directories in the current directory. You need to supply an argument to this method which contains the name of the directory to be created.
            os.mkdir("newdir")

            import os
            # Create a directory "test"
            os.mkdir("test")

        The chdir() Method
            You can use the chdir() method to change the current directory. The chdir() method takes an argument, which is the name of the directory that you want to make the current directory.
            import os
            # Changing a directory to "/home/newdir"
            os.chdir("/home/newdir")
        
        The getcwd() Method
            The getcwd() method displays the current working directory.
            import os
            # This would give location of the current directory
            os.getcwd()
        
        The rmdir() Method
        import os
        # This would  remove "/tmp/test"  directory.
        os.rmdir( "/tmp/test"  )

    File & Directory Related Methods
        File Object Methods
            file.close()
                Close the file. A closed file cannot be read or written any more.
            file.flush()
                Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.
            file.fileno()
                Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.
            file.isatty()
                Returns True if the file is connected to a tty(-like) device, else False.
            file.next()
                Returns the next line from the file each time it is being called.
            file.read([size])
                Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).
            file.readline([size])
                Reads one entire line from the file. A trailing newline character is kept in the string.
            file.readlines([sizehint])
                Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.
            file.seek(offset[, whence])
                Sets the file's current position
            file.tell()
                Returns the file's current position
            file.truncate([size])
                Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.
            file.write(str)
                Writes a string to the file. There is no return value.
            file.writelines(sequence)
                Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings.
        The os module
            os.access(path, mode)
                Use the real uid/gid to test for access to path.
            os.chdir(path)
                Change the current working directory to path
            os.chflags(path, flags)
                Set the flags of path to the numeric flags.
            os.chmod(path, mode)
                Change the mode of path to the numeric mode.
            os.chown(path, uid, gid)
                Change the owner and group id of path to the numeric uid and gid.
            os.chroot(path)
                Change the root directory of the current process to path.
            os.close(fd)
                Close file descriptor fd.
            os.closerange(fd_low, fd_high)
                Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors.
            os.dup(fd)
                Return a duplicate of file descriptor fd.
            os.dup2(fd, fd2)
                Duplicate file descriptor fd to fd2, closing the latter first if necessary.
            os.fchdir(fd)
                Change the current working directory to the directory represented by the file descriptor fd.
            os.fchmod(fd, mode)
                Change the mode of the file given by fd to the numeric mode.
            os.fchown(fd, uid, gid)
                Change the owner and group id of the file given by fd to the numeric uid and gid.
            os.fdatasync(fd)
                Force write of file with filedescriptor fd to disk.
            os.fdopen(fd[, mode[, bufsize]])
                Return an open file object connected to the file descriptor fd.
            os.fpathconf(fd, name)
                Return system configuration information relevant to an open file. name specifies the configuration value to retrieve.
            os.fstat(fd)
                Return status for file descriptor fd, like stat().
            os.fstatvfs(fd)
                Return information about the filesystem containing the file associated with file descriptor fd, like statvfs().
            os.fsync(fd)
                Force write of file with filedescriptor fd to disk.
            os.ftruncate(fd, length)
                Truncate the file corresponding to file descriptor fd, so that it is at most length bytes in size.
            os.getcwd()
                Return a string representing the current working directory.
            os.getcwdu()
                Return a Unicode object representing the current working directory.
            os.isatty(fd)
                Return True if the file descriptor fd is open and connected to a tty(-like) device, else False.
            os.lchflags(path, flags)
                Set the flags of path to the numeric flags, like chflags(), but do not follow symbolic links.
            os.lchmod(path, mode)
                Change the mode of path to the numeric mode.
            os.lchown(path, uid, gid)
                Change the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links.
            os.link(src, dst)
                Create a hard link pointing to src named dst.
            os.listdir(path)
                Return a list containing the names of the entries in the directory given by path.
            os.lseek(fd, pos, how)
                Set the current position of file descriptor fd to position pos, modified by how.
            os.lstat(path)
                Like stat(), but do not follow symbolic links.
            os.major(device)
                Extract the device major number from a raw device number.
            os.makedev(major, minor)
                Compose a raw device number from the major and minor device numbers.
            os.makedirs(path[, mode])
                Recursive directory creation function.
            os.minor(device)
                Extract the device minor number from a raw device number.
            os.mkdir(path[, mode])
                Create a directory named path with numeric mode mode.
            os.mkfifo(path[, mode])
                Create a FIFO (a named pipe) named path with numeric mode mode. The default mode is 0666 (octal).
            os.mknod(filename[, mode=0600, device])
                Create a filesystem node (file, device special file or named pipe) named filename.
            os.open(file, flags[, mode])
                Open the file file and set various flags according to flags and possibly its mode according to mode.
            os.openpty()
                Open a new pseudo-terminal pair. Return a pair of file descriptors (master, slave) for the pty and the tty, respectively.
            os.pathconf(path, name)
                Return system configuration information relevant to a named file.
            os.pipe()
                Create a pipe. Return a pair of file descriptors (r, w) usable for reading and writing, respectively.
            os.popen(command[, mode[, bufsize]])
                Open a pipe to or from command.
            os.read(fd, n)
                Read at most n bytes from file descriptor fd. Return a string containing the bytes read. If the end of the file referred to by fd has been reached, an empty string is returned.
            os.readlink(path)
                Return a string representing the path to which the symbolic link points.
            os.remove(path)
                Remove the file path.
            os.removedirs(path)
                Remove directories recursively.
            os.rename(src, dst)
                Rename the file or directory src to dst.
            os.renames(old, new)
                Recursive directory or file renaming function.
            os.rmdir(path)
                Remove the directory path
            os.stat(path)
                Perform a stat system call on the given path.
            os.stat_float_times([newvalue])
                Determine whether stat_result represents time stamps as float objects.
            os.statvfs(path)
                Perform a statvfs system call on the given path.
            os.symlink(src, dst)
                Create a symbolic link pointing to src named dst.
            os.tcgetpgrp(fd)
                Return the process group associated with the terminal given by fd (an open file descriptor as returned by open()).
            os.tcsetpgrp(fd, pg)
                Set the process group associated with the terminal given by fd (an open file descriptor as returned by open()) to pg.
            os.tempnam([dir[, prefix]])
                Return a unique path name that is reasonable for creating a temporary file.
            os.tmpfile()
                Return a new file object opened in update mode (w+b).
            os.tmpnam()
                Return a unique path name that is reasonable for creating a temporary file.
            os.ttyname(fd)
                Return a string which specifies the terminal device associated with file descriptor fd. If fd is not associated with a terminal device, an exception is raised.
            os.unlink(path)
                Remove the file path.
            os.utime(path, times)
                Set the access and modified times of the file specified by path.
            os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
                Generate the file names in a directory tree by walking the tree either top-down or bottom-up.
            os.write(fd, str)
                Write the string str to file descriptor fd. Return the number of bytes actually written.
'''


#exceptions
'''
Python provides two very important features to handle any unexpected error in your Python programs and to add debugging capabilities in them

Exception Handling
    This would be covered in this tutorial. Here is a list of standard Exceptions available in Python.
    Standard Exceptions:
        Exception
            Base class for all exceptions
        StopIteration
            Raised when the next() method of an iterator does not point to any object.
        SystemExit
            Raised by the sys.exit() function.
        StandardError
            Base class for all built-in exceptions except StopIteration and SystemExit.
        ArithmeticError
            Base class for all errors that occur for numeric calculation.
        OverflowError
            Raised when a calculation exceeds maximum limit for a numeric type.
        FloatingPointError
            Raised when a floating point calculation fails.
        ZeroDivisionError
            Raised when division or modulo by zero takes place for all numeric types.
        AssertionError
            Raised in case of failure of the Assert statement.
        AttributeError
            Raised in case of failure of attribute reference or assignment.
        EOFError
            Raised when there is no input from either the raw_input() or input() function and the end of file is reached.
        ImportError
            Raised when an import statement fails.
        KeyboardInterrupt
            Raised when the user interrupts program execution, usually by pressing Ctrl+c.
        LookupError
            Base class for all lookup errors.
        IndexError
            Raised when an index is not found in a sequence.
        KeyError
            Raised when the specified key is not found in the dictionary.
        NameError
            Raised when an identifier is not found in the local or global namespace.
        UnboundLocalError
            Raised when trying to access a local variable in a function or method but no value has been assigned to it.
        EnvironmentError
            Base class for all exceptions that occur outside the Python environment.
        IOError
            Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.
        OSError
            Raised for operating system-related errors.
        SyntaxError
            Raised when there is an error in Python syntax.
        IndentationError
            Raised when indentation is not specified properly.
        SystemError
            Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.
        SystemExit
            Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.
        TypeError
            Raised when an operation or function is attempted that is invalid for the specified data type.
        ValueError
            Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
        RuntimeError
            Raised when a generated error does not fall into any category.
        NotImplementedError
            Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.


Assertions
    This would be covered in Assertions in Python tutorial.
    An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program.

    The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false, an exception is raised.

    Assertions are carried out by the assert statement, the newest keyword to Python, introduced in version 1.5.

    Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.

    The assert Statement
    When it encounters an assert statement, Python evaluates the accompanying expression, which is hopefully true. If the expression is false, Python raises an AssertionError exception.

    The syntax for assert is
        assert Expression[, Arguments]
        If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError. AssertionError exceptions can be caught and handled like any other exception using the try-except statement, but if not handled, they will terminate the program and produce a traceback.

    Example
        Here is a function that converts a temperature from degrees Kelvin to degrees Fahrenheit. Since zero degrees Kelvin is as cold as it gets, the function bails out if it sees a negative temperature

        def KelvinToFahrenheit(Temperature):
            assert (Temperature >= 0),"Colder than absolute zero!"
            return ((Temperature-273)*1.8)+32

        print KelvinToFahrenheit(273)
        print int(KelvinToFahrenheit(505.78))
        print KelvinToFahrenheit(-5)

        When the above code is executed, it produces the following result:
            32.0
            451
            Traceback (most recent call last):
            File "test.py", line 9, in <module>
                print KelvinToFahrenheit(-5)
            File "test.py", line 4, in KelvinToFahrenheit
                assert (Temperature >= 0),"Colder than absolute zero!"
            AssertionError: Colder than absolute zero!


What is Exception?
    An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error.
    When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.
Handling an exception
    If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.
    Syntax
        try:
            You do your operations here;
            ......................
        except ExceptionI:
            If there is ExceptionI, then execute this block.
        except ExceptionII:
            If there is ExceptionII, then execute this block.
            ......................
        else:
            If there is no exception then execute this block. 

    Here are few important points about the above-mentioned syntax:
        -A single try statement can have multiple except statements. This is useful when the try block contains statements that may throw different types of exceptions.
        -You can also provide a generic except clause, which handles any exception.
        -After the except clause(s), you can include an else-clause. The code in the else-block executes if the code in the try: block does not raise an exception.
        The else-block is a good place for code that does not need the try: block's protection.

        Example1:
            This example opens a file, writes content in the, file and comes out gracefully because there is no problem at all
            try:
                fh = open("testfile", "w")
                fh.write("This is my test file for exception handling!!")
            except IOError:
                print "Error: can\'t find file or read data"
            else:
                print "Written content in the file successfully"
            fh.close()

            This produces the following result:
                Written content in the file successfully
        
        Example2:
           This example tries to open a file where you do not have write permission, so it raises an exception
            try:
                fh = open("testfile", "r")
                fh.write("This is my test file for exception handling!!")
            except IOError:
                print ("Error: can\'t find file or read data")
            else:
                rint ("Written content in the file successfully")
                        
            This produces the following result:
                Error: can't find file or read data

    The except Clause with No Exceptions:
        You can also use the except statement with no exceptions defined as follows
        try:
            You do your operations here;
        except:
            If there is any exception, then execute this block.
        else:
            If there is no exception then execute this block. 

        This kind of a try-except statement catches all the exceptions that occur. Using this kind of try-except statement is not considered a good programming practice though, because it catches all exceptions but does not make the programmer identify the root cause of the problem that may occur.

    
    The except Clause with Multiple Exceptions:
        You can also use the same except statement to handle multiple exceptions as follows
        try:
            You do your operations here;            
        except(Exception1[, Exception2[,...ExceptionN]]]):
            If there is any exception from the given exception list, 
            then execute this block.            
        else:
            If there is no exception then execute this block. 

    The try-finally Clause:
        You can use a finally: block along with a try: block. The finally block is a place to put any code that must execute, whether the try-block raised an exception or not. The syntax of the try-finally statement is this:
        try:
            You do your operations here;        
            Due to any exception, this may be skipped.
        finally:
            This would always be executed.        

        Example:        
            try:
                fh = open("testfile", "w")
                fh.write("This is my test file for exception handling!!")
            finally:
                print "Error: can\'t find file or read data"

            If you do not have permission to open the file in writing mode, then this will produce the following result:
            Error: can't find file or read data

        Same example can be written more cleanly as follows:
            try:
                fh = open("testfile", "w")
                try:
                    fh.write("This is my test file for exception handling!!")
                finally:
                    print "Going to close the file"
                    fh.close()
            except IOError:
                print "Error: can\'t find file or read data"

            When an exception is thrown in the try block, the execution immediately passes to the finally block. After all the statements in the finally block are executed, the exception is raised again and is handled in the except statements if present in the next higher layer of the try-except statement.

    Argument of an Exception:
        An exception can have an argument, which is a value that gives additional information about the problem. The contents of the argument vary by exception. You capture an exception's argument by supplying a variable in the except clause as follows:
        Syntax:
            try:
                You do your operations here;                
            except ExceptionType, Argument:
                You can print value of Argument here...
        Example:
            If you write the code to handle a single exception, you can have a variable follow the name of the exception in the except statement. If you are trapping multiple exceptions, you can have a variable follow the tuple of the exception.
            This variable receives the value of the exception mostly containing the cause of the exception. The variable can receive a single value or multiple values in the form of a tuple. This tuple usually contains the error string, the error number, and an error location.

            # Define a function here.
            def temp_convert(var):
                try:
                    return int(var)
                except ValueError, Argument:
                    print "The argument does not contain numbers\n", Argument

            # Call above function here.
            temp_convert("xyz");

            This produces the following result:
                The argument does not contain numbers
                invalid literal for int() with base 10: 'xyz'

    Raising an Exceptions:
        You can raise exceptions in several ways by using the raise statement. The general syntax for the raise statement is as follows.

        Syntax
            raise [Exception [, args [, traceback]]]
            Here, Exception is the type of exception (for example, NameError) and argument is a value for the exception argument. The argument is optional; if not supplied, the exception argument is None.
            The final argument, traceback, is also optional (and rarely used in practice), and if present, is the traceback object used for the exception.

        Example
            An exception can be a string, a class or an object. Most of the exceptions that the Python core raises are classes, with an argument that is an instance of the class. Defining new exceptions is quite easy and can be done as follows

            def functionName( level ):
                if level < 1:
                    raise "Invalid level!", level
                    # The code below to this would not be executed
                    # if we raise the exception

            Note: In order to catch an exception, an "except" clause must refer to the same exception thrown either class object or simple string. For example, to capture above exception, we must write the except clause as follows:
            try:
                Business Logic here...
            except "Invalid level!":
                Exception handling here...
            else:
                Rest of the code here...
        
        User-Defined Exceptions:
            Python also allows you to create your own exceptions by deriving classes from the standard built-in exceptions.
            Here is an example related to RuntimeError. Here, a class is created that is subclassed from RuntimeError. This is useful when you need to display more specific information when an exception is caught.
            In the try block, the user-defined exception is raised and caught in the except block. The variable e is used to create an instance of the class Networkerror.

            class Networkerror(RuntimeError):
                def __init__(self, arg):
                    self.args = arg
            
            So once you defined above class, you can raise the exception as follows:

            try:
                raise Networkerror("Bad hostname")
            except Networkerror,e:
                print e.args            
'''

#OOP
'''
Terminology
    Class:
        A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
    Class variable:
        A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.
    Data member:
        A class variable or instance variable that holds data associated with a class and its objects.
    Function overloading:
        The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.
    Instance variable:
        A variable that is defined inside a method and belongs only to the current instance of a class.
    Inheritance:
        The transfer of the characteristics of a class to other classes that are derived from it.
    Instance:
        An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
    Instantiation:
        The creation of an instance of a class.
    Method:
        A special kind of function that is defined in a class definition.
    Object:
        A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.
    Operator overloading:
        The assignment of more than one function to a particular operator.

Class structure
    class ClassName:
        'Optional class documentation string'
        class_suite
 
    The class has a documentation string, which can be accessed via ClassName.__doc__.
    The class_suite consists of all the component statements defining class members, data attributes and functions.
'''
# __doc__
class Person:
   'any documentation'
print(Person.__doc__)


# example of a simple Python class
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

emp_one = Employee('Carlos', 800)
emp_two = Employee('Jhon', 700)

emp_one.displayCount()

emp_two.displayEmployee()
emp_one.displayEmployee()

print(Employee.empCount)

emp_two.age = 7  # Add an 'age' attribute.
emp_two.age = 8  # Modify 'age' attribute.

print(emp_two.age)

print(emp_one.__getattribute__('name'))
print(getattr(emp_one, 'name'))
print(hasattr(emp_one,'name')) #True / False
setattr(emp_one,'country', 'Panama')

print(emp_one.country)

delattr(emp_one, 'country')

del emp_two.age  # Delete 'age' attribute.

del emp_one

#Built-In Class Attributes
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__bases__)



# functions to handle object attributes
'''
Instead of using the normal statements to access attributes, you can use the following functions
    getattr(obj, name[, default])
        to access the attribute of object.
    hasattr(obj,name)
        to check if an attribute exists or not.
    setattr(obj,name,value)
        to set an attribute. If attribute does not exist, then it would be created.
    delattr(obj, name)
        to delete an attribute.
'''

# Destroying Objects (Garbage Collection)
'''
The process by which Python periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.
Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space. 
Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. An object's reference count changes as the number of aliases that point to it changes.
An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python collects it automatically.

    a = 40      # Create object <40>
    b = a       # Increase ref. count  of <40> 
    c = [b]     # Increase ref. count  of <40> 

    del a       # Decrease ref. count  of <40>
    b = 100     # Decrease ref. count  of <40> 
    c[0] = -1   # Decrease ref. count  of <40> 

You normally will not notice when the garbage collector destroys an orphaned instance and reclaims its space. But a class can implement the special method __del__(), called a destructor, that is invoked when the instance is about to be destroyed. This method might be used to clean up any non memory resources used by an instance.

Note:
    Ideally, you should define your classes in separate file, then you should import them in your main program file using import statement.

'''

# Class Inheritance
'''
Instead of starting from scratch, you can create a class by deriving it from a preexisting class by listing the parent class in parentheses after the new class name.
The child class inherits the attributes of its parent class, and you can use those attributes as if they were defined in the child class. A child class can also override data members and methods from the parent.
'''
class Parent:        # define parent class
   parentAttr = 100
   
   def __init__(self):      
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):         
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


# 
'''
Similar way, you can drive a class from multiple parent classes as follows:
class A:        # define your class A
    .....
class B:         # define your class B
    .....
class C(A, B):   # subclass of A and B
    .....

You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.
    The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.
    The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class
'''


# Overriding Methods
'''
You can always override your parent class methods. One reason for overriding parent's methods is because you may want special or different functionality in your subclass.
'''
class Parent:        # define parent class
   def myMethod(self):
      print('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method

# Base Overloading Methods
'''
Following table lists some generic functionality that you can override in your own classes:
    __init__ ( self [,args...] )
        Constructor (with any optional arguments)
        Sample Call : obj = className(args)
    __del__( self )
        Destructor, deletes an object
        Sample Call : del obj
    __repr__( self )
        Evaluable string representation
        Sample Call : repr(obj)
    __str__( self )
        Printable string representation
        Sample Call : str(obj)
'''

# Overloading Operators
'''
Suppose you have created a Vector class to represent two-dimensional vectors, what happens when you use the plus operator to add them? Most likely Python will yell at you.

You could, however, define the __add__ method in your class to perform vector addition and then the plus operator would behave as per expectation
'''
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)

# Data Hiding
'''
An object's attributes may or may not be visible outside the class definition. You need to name attributes with a double underscore prefix, and those attributes then are not be directly visible to outsiders.
'''
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount)

'''
When the above code is executed, it produces the following result:
    1
    2
    Traceback (most recent call last):
    File "test.py", line 12, in <module>
        print counter.__secretCount
    AttributeError: JustCounter instance has no attribute '__secretCount'

Python protects those members by internally changing the name to include the class name. You can access such attributes as object._className__attrName. If you would replace your last line as following, then it works for you.
'''
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__secretCount)


# Regular Expressions
'''
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

The Python module re provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression.

We would cover two important functions, which would be used to handle regular expressions. But a small thing first: There are various characters, which would have special meaning when they are used in regular expression. To avoid any confusion while dealing with regular expressions, we would use Raw Strings as r'expression'.
'''
# The match Function
'''
This function attempts to match RE pattern to string with optional flags.
re.match(pattern, string, flags=0)
    pattern
        This is the regular expression to be matched.
    string
        This is the string, which would be searched to match the pattern at the beginning of string.
    flags
        You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

The re.match function returns a match object on success, None on failure. We usegroup(num) or groups() function of match object to get matched expression.
    group(num=0)
        This method returns entire match (or specific subgroup num)
    groups()
        This method returns all matching subgroups in a tuple (empty if there weren't any)
'''

import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

'''
 re.M significa "multiline", lo que permite que la expresión regular coincida con el inicio de cada línea en lugar de solo al principio de la cadena completa. re.I significa "ignore case", lo que hace que la coincidencia de patrones sea insensible a mayúsculas y minúsculas.
'''

print(re.match(r'(.*) are', line).groups())
print(re.match(r'(.*) are', line).group(1))

print(matchObj.groups())
if matchObj:
   print(matchObj.group())
   print(matchObj.groups())
   print(matchObj.group(1))
   print(matchObj.group(2))
else:
   print("No match!!")

print(re.match(r'(.*) are (.*?) (.*?) (.*)', line).groups())


#The Search Function
'''
This function searches for first occurrence of RE pattern within string with optional flags.
Here is the syntax for this function
re.search(pattern, string, flags=0)
    pattern
        This is the regular expression to be matched.
    string
        This is the string, which would be searched to match the pattern anywhere in the string.
    flags
        You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

The re.search function returns a match object on success, none on failure. We use group(num) or groups() function of match object to get matched expression.
'''
import re
line = "Cats are smarter than dogs"
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print(searchObj.group())
   print(searchObj.groups())
   print(searchObj.group(1))
   print(searchObj.group(2))
else:
   print("Nothing found!!")

# Matching Versus Searching
'''
Python offers two different primitive operations based on regular expressions: match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).
'''
import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print( "match --> matchObj.group() : ", matchObj.group())
else:
   print( "No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print( "search --> searchObj.group() : ", searchObj.group())
else:
   print( "Nothing found!!")


#Search and Replace
'''
This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max provided. This method returns modified string.
re.sub(pattern, repl, string, max=0)
'''
import re
phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print("Phone Num : ", num)


# Regular Expression Modifiers: Option Flags
'''
Regular expression literals may include an optional modifier to control various aspects of matching. The modifiers are specified as an optional flag. You can provide multiple modifiers using exclusive OR (|), as shown previously and may be represented by one of these
re.I
    Performs case-insensitive matching.
re.L
    Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B).
re.M
    Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
re.S
    Makes a period (dot) match any character, including a newline.
re.U
    Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.
re.X
    Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.
'''

# Regular Expression Patterns
'''
Except for control characters, (+ ? . * ^ $ ( ) [ ] { } | \), all characters match themselves. You can escape a control character by preceding it with a backslash.
Following table lists the regular expression syntax that is available in Python
    ^
        Matches beginning of line.
    $
        Matches end of line.
    .
        Matches any single character except newline. Using m option allows it to match newline as well.
    [...]
        Matches any single character in brackets.
    [^...]
        Matches any single character not in brackets
    re*
        Matches 0 or more occurrences of preceding expression.
    re+
        Matches 1 or more occurrence of preceding expression.
    re?
        Matches 0 or 1 occurrence of preceding expression.
    re{ n}
        Matches exactly n number of occurrences of preceding expression.
    re{ n,}
        Matches n or more occurrences of preceding expression.
    re{ n, m}
        Matches at least n and at most m occurrences of preceding expression.
    a| b
        Matches either a or b.
    (re)
        Groups regular expressions and remembers matched text.
    (?imx)
        Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.
    (?-imx)
        Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.
    (?: re)
        Groups regular expressions without remembering matched text.
    (?imx: re)
        Temporarily toggles on i, m, or x options within parentheses.
    (?-imx: re)
        Temporarily toggles off i, m, or x options within parentheses.
    (?#...)
        Comment.
    (?= re)
        Specifies position using a pattern. Doesn't have a range.
    (?! re)
        Specifies position using pattern negation. Doesn't have a range.
    (?> re)
        Matches independent pattern without backtracking.
    \w
        Matches word characters.
    \W
        Matches nonword characters.
    \s
        Matches whitespace. Equivalent to [\t\n\r\f].
    \S
        Matches nonwhitespace.
    \d
        Matches digits. Equivalent to [0-9].
    \D
        Matches nondigits.
    \A
        Matches beginning of string.
    \Z
        Matches end of string. If a newline exists, it matches just before newline.
    \z
        Matches end of string.
    \G
        Matches point where last match finished.
    \b
        Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.
    \B
        Matches nonword boundaries.
    \n, \t, etc.
        Matches newlines, carriage returns, tabs, etc.
    \1...\9
        Matches nth grouped subexpression.
    \10
        Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.

'''


# Regular Expression Examples -  Literal characters
'''	
python
    Match "python".
'''

# Regular Expression Examples -  Character classes
'''
[Pp]ython
    Match "Python" or "python"
rub[ye]
    Match "ruby" or "rube"
[aeiou]
    Match any one lowercase vowel
[0-9]
    Match any digit; same as [0123456789]
[a-z]
    Match any lowercase ASCII letter
[A-Z]
    Match any uppercase ASCII letter
[a-zA-Z0-9]
    Match any of the above
[^aeiou]
    Match anything other than a lowercase vowel
[^0-9]
    Match anything other than a digit
'''


# Regular Expression Examples - Special Character Classes
'''
.
    Match any character except newline
\d
    Match a digit: [0-9]
\D
    Match a nondigit: [^0-9]
\s
    Match a whitespace character: [ \t\r\n\f]
\S
    Match nonwhitespace: [^ \t\r\n\f]
\w
    Match a single word character: [A-Za-z0-9_]
\W
    Match a nonword character: [^A-Za-z0-9_]
'''

# Regular Expression Examples - Repetition Cases
'''
ruby?
    Match "rub" or "ruby": the y is optional
ruby*
    Match "rub" plus 0 or more ys	
ruby+
    Match "rub" plus 1 or more ys
\d{3}
    Match exactly 3 digits
\d{3,}
    Match 3 or more digits
\d{3,5}
    Match 3, 4, or 5 digits
'''

# Regular Expression Examples - Nongreedy repetition
'''
<.*>
    Greedy repetition: matches "<python>perl>"	
<.*?>
    Nongreedy: matches "<python>" in "<python>perl>"
'''

# Regular Expression Examples - Grouping with Parentheses
'''
\D\d+
    No group: + repeats \d
(\D\d)+
    Grouped: + repeats \D\d pair
([Pp]ython(, )?)+
    Match "Python", "Python, python, python", etc.
'''

# Regular Expression Examples - Backreferences
'''
This matches a previously matched group again
([Pp])ython&\1ails
    Match python&pails or Python&Pails
(['"])[^\1]*\1
    Single or double-quoted string. \1 matches whatever the 1st group matched. \2 matches whatever the 2nd group matched, etc.
'''

# Regular Expression Examples - Alternatives
'''
python|perl
    Match "python" or "perl"
rub(y|le))
    Match "ruby" or "ruble"
Python(!+|\?)
    "Python" followed by one or more ! or one ?
'''

# Regular Expression Examples - Anchors
'''		
^Python
    Match "Python" at the start of a string or internal line
Python$
    Match "Python" at the end of a string or line
\APython
    Match "Python" at the start of a string
Python\Z
    Match "Python" at the end of a string
\bPython\b
    Match "Python" at a word boundary
\brub\B
    \B is nonword boundary: match "rub" in "rube" and "ruby" but not alone
Python(?=!)
    Match "Python", if followed by an exclamation point.
Python(?!!)
    Match "Python", if not followed by an exclamation point.
'''

# Regular Expression Examples - Special Syntax with Parentheses
'''
R(?#comment)
    Matches "R". All the rest is a comment	
R(?i)uby
    Case-insensitive while matching "uby"	
R(?i:uby)
    Same as above
rub(?:y|le))
    Group only without creating \1 backreference
'''

# Python - CGI Programming
'''
The Common Gateway Interface, or CGI, is a set of standards that define how information is exchanged between the web server and a custom script. The CGI specs are currently maintained by the NCSA.

What is CGI?
    The Common Gateway Interface, or CGI, is a standard for external gateway programs to interface with information servers such as HTTP servers.
    The current version is CGI/1.1 and CGI/1.2 is under progress.

Web Browsing
    To understand the concept of CGI, let us see what happens when we click a hyper link to browse a particular web page or URL.
        Your browser contacts the HTTP web server and demands for the URL, i.e., filename.
        Web Server parses the URL and looks for the filename. If it finds that file then sends it back to the browser, otherwise sends an error message indicating that you requested a wrong file.
        Web browser takes response from web server and displays either the received file or error message.
    However, it is possible to set up the HTTP server so that whenever a file in a certain directory is requested that file is not sent back; instead it is executed as a program, and whatever that program outputs is sent back for your browser to display. This function is called the Common Gateway Interface or CGI and the programs are called CGI scripts. These CGI programs can be a Python Script, PERL Script, Shell Script, C or C++ program, etc.

Web Server Support and Configuration
    Before you proceed with CGI Programming, make sure that your Web Server supports CGI and it is configured to handle CGI Programs. All the CGI Programs to be executed by the HTTP server are kept in a pre-configured directory. This directory is called CGI Directory and by convention it is named as /var/www/cgi-bin. By convention, CGI files have extension as. cgi, but you can keep your files with python extension .py as well.

    By default, the Linux server is configured to run only the scripts in the cgi-bin directory in /var/www. If you want to specify any other directory to run your CGI scripts, comment the following lines in the httpd.conf file

    <Directory "/var/www/cgi-bin">
        AllowOverride None
        Options ExecCGI
        Order allow,deny
        Allow from all
    </Directory>
    <Directory "/var/www/cgi-bin">
        Options All
    </Directory>

    Here, we assume that you have Web Server up and running successfully and you are able to run any other CGI program like Perl or Shell, etc.

First CGI Program
    Here is a simple link, which is linked to a CGI script called hello.py. This file is kept in /var/www/cgi-bin directory and it has following content. Before running your CGI program, make sure you have change mode of file using chmod 755 hello.py UNIX command to make file executable.

    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<title>Hello World - First CGI Program</title>')
    print('</head>')
    print('<body>')
    print('<h2>Hello World! This is my first CGI program</h2>')
    print('</body>')
    print('</html>')

    If you click hello.py, then this produces the following output
        Hello World! This is my first CGI program

    This hello.py script is a simple Python script, which writes its output on STDOUT file, i.e., screen. There is one important and extra feature available which is first line to be printed Content-type:text/html\r\n\r\n. This line is sent back to the browser and it specifies the content type to be displayed on the browser screen.

HTTP Header
    The line Content-type:text/html\r\n\r\n is part of HTTP header which is sent to the browser to understand the content. All the HTTP header will be in the following form

    HTTP Field Name: Field Content

    For Example
    Content-type: text/html\r\n\r\n

    There are few other important HTTP headers, which you will use frequently in your CGI Programming.
        Content-type:
            A MIME string defining the format of the file being returned. Example is Content-type:text/html
        Expires: Date
            The date the information becomes invalid. It is used by the browser to decide when a page needs to be refreshed. A valid date string is in the format 01 Jan 1998 12:00:00 GMT.
        Location: URL
            The URL that is returned instead of the URL requested. You can use this field to redirect a request to any file.
        Last-modified: Date
            The date of last modification of the resource.
        Content-length: N
            The length, in bytes, of the data being returned. The browser uses this value to report the estimated download time for a file.
        Set-Cookie: String
            Set the cookie passed through the string

CGI Environment Variables
    All the CGI programs have access to the following environment variables. These variables play an important role while writing any CGI program.
        CONTENT_TYPE
            The data type of the content. Used when the client is sending attached content to the server. For example, file upload.
        CONTENT_LENGTH
            The length of the query information. It is available only for POST requests.
        HTTP_COOKIE
            Returns the set cookies in the form of key & value pair.
        HTTP_USER_AGENT
            The User-Agent request-header field contains information about the user agent originating the request. It is name of the web browser.
        PATH_INFO
            The path for the CGI script.
        QUERY_STRING
            The URL-encoded information that is sent with GET method request.
        REMOTE_ADDR
            The IP address of the remote host making the request. This is useful logging or for authentication.
        REMOTE_HOST
            The fully qualified name of the host making the request. If this information is not available, then REMOTE_ADDR can be used to get IR address.
        REQUEST_METHOD
            The method used to make the request. The most common methods are GET and POST.
        SCRIPT_FILENAME
            The full path to the CGI script.
        SCRIPT_NAME
            The name of the CGI script.
        SERVER_NAME
            The server's hostname or IP Address
        SERVER_SOFTWARE
            The name and version of the software the server is running.

Here is small CGI program to list out all the CGI variables. Click this link to see the result Get Environment

    import os

    print "Content-type: text/html\r\n\r\n";
    print "<font size=+1>Environment</font><\br>";
    for param in os.environ.keys():
    print "<b>%20s</b>: %s<\br>" % (param, os.environ[param])

GET and POST Methods
    You must have come across many situations when you need to pass some information from your browser to web server and ultimately to your CGI Program. Most frequently, browser uses two methods two pass this information to web server. These methods are GET Method and POST Method.

    Passing Information using GET method
        The GET method sends the encoded user information appended to the page request. The page and the encoded information are separated by the ? character as follows

        http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2

        The GET method is the default method to pass information from browser to web server and it produces a long string that appears in your browser's Location:box. Never use GET method if you have password or other sensitive information to pass to the server. The GET method has size limitation: only 1024 characters can be sent in a request string. The GET method sends information using QUERY_STRING header and will be accessible in your CGI Program through QUERY_STRING environment variable.

        You can pass information by simply concatenating key and value pairs along with any URL or you can use HTML <FORM> tags to pass information using GET method.

        Simple URL Example:Get Method
        Python Code
            # Import modules for CGI handling 
            import cgi, cgitb 

            # Create instance of FieldStorage 
            form = cgi.FieldStorage() 

            # Get data from fields
            first_name = form.getvalue('first_name')
            last_name  = form.getvalue('last_name')

            print("Content-type:text/html\r\n\r\n")
            print("<html>")
            print("<head>")
            print("<title>Hello - Second CGI Program</title>")
            print("</head>")
            print("<body>")
            print("<h2>Hello %s %s</h2>" % (first_name, last_name))
            print("</body>")
            print("</html>")
        
        html code
            <form action = "./cgi-bin//hello_get.py" method = "get">
                <label for="first_name">First Name</label>
                <input id="first_name" type = "text" name = "first_name">  <br />
                
                <label for="last_name">First Name</label>
                <input id="last_name" type = "text" name = "last_name" />

                <input type = "submit" value = "Submit" />
            </form>

    Passing Information Using POST Method
        A generally more reliable method of passing information to a CGI program is the POST method. This packages the information in exactly the same way as GET methods, but instead of sending it as a text string after a ? in the URL it sends it as a separate message. This message comes into the CGI script in the form of the standard input.

        Below is same hello_get.py script which handles GET as well as POST method.
        python code
            import cgi, cgitb 

            # Create instance of FieldStorage 
            form = cgi.FieldStorage() 

            # Get data from fields
            first_name = form.getvalue('first_name')
            last_name  = form.getvalue('last_name')

            print "Content-type:text/html\r\n\r\n"
            print "<html>"
            print "<head>"
            print "<title>Hello - Second CGI Program</title>"
            print "</head>"
            print "<body>"
            print "<h2>Hello %s %s</h2>" % (first_name, last_name)
            print "</body>"
            print "</html>"
        
        html code
        <form action = "/cgi-bin/hello_get.py" method = "post">
            First Name: <input type = "text" name = "first_name"><br />
            Last Name: <input type = "text" name = "last_name" />

            <input type = "submit" value = "Submit" />
        </form>
    
    Passing Checkbox Data to CGI Program
        html code
        <form action = "/cgi-bin/checkbox.cgi" method = "POST" target = "_blank">
            <input type = "checkbox" name = "maths" value = "on" /> Maths
            <input type = "checkbox" name = "physics" value = "on" /> Physics
            <input type = "submit" value = "Select Subject" />
        </form>

        python code
        # Import modules for CGI handling 
        import cgi, cgitb 

        # Create instance of FieldStorage 
        form = cgi.FieldStorage() 

        # Get data from fields
        if form.getvalue('maths'):
        math_flag = "ON"
        else:
        math_flag = "OFF"

        if form.getvalue('physics'):
        physics_flag = "ON"
        else:
        physics_flag = "OFF"

        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Checkbox - Third CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2> CheckBox Maths is : %s</h2>" % math_flag
        print "<h2> CheckBox Physics is : %s</h2>" % physics_flag
        print "</body>"
        print "</html>"
    
    Passing Radio Button Data to CGI Program
        html code
        <form action = "/cgi-bin/radiobutton.py" method = "post" target = "_blank">
            <input type = "radio" name = "subject" value = "maths" /> Maths
            <input type = "radio" name = "subject" value = "physics" /> Physics
            <input type = "submit" value = "Select Subject" />
        </form>

        python code
        # Import modules for CGI handling 
        import cgi, cgitb 

        # Create instance of FieldStorage 
        form = cgi.FieldStorage() 

        # Get data from fields
        if form.getvalue('subject'):
        subject = form.getvalue('subject')
        else:
        subject = "Not set"

        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Radio - Fourth CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2> Selected Subject is %s</h2>" % subject
        print "</body>"
        print "</html>"

    Passing Text Area Data to CGI Program
        html code
        <form action = "/cgi-bin/textarea.py" method = "post" target = "_blank">
            <textarea name = "textcontent" cols = "40" rows = "4">
            Type your text here...
            </textarea>
            <input type = "submit" value = "Submit" />
        </form>

        python code        
        # Import modules for CGI handling 
        import cgi, cgitb 

        # Create instance of FieldStorage 
        form = cgi.FieldStorage() 

        # Get data from fields
        if form.getvalue('textcontent'):
        text_content = form.getvalue('textcontent')
        else:
        text_content = "Not entered"

        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>";
        print "<title>Text Area - Fifth CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2> Entered Text Content is %s</h2>" % text_content
        print "</body>"

    Passing Drop Down Box Data to CGI Program
        html code
        <form action = "/cgi-bin/dropdown.py" method = "post" target = "_blank">
            <select name = "dropdown">
            <option value = "Maths" selected>Maths</option>
            <option value = "Physics">Physics</option>
            </select>
            <input type = "submit" value = "Submit"/>
        </form>

    python code
        # Import modules for CGI handling 
        import cgi, cgitb 

        # Create instance of FieldStorage 
        form = cgi.FieldStorage() 

        # Get data from fields
        if form.getvalue('dropdown'):
        subject = form.getvalue('dropdown')
        else:
        subject = "Not entered"

        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Dropdown Box - Sixth CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2> Selected Subject is %s</h2>" % subject
        print "</body>"
        print "</html>"

    Using Cookies in CGI
        HTTP protocol is a stateless protocol. For a commercial website, it is required to maintain session information among different pages. For example, one user registration ends after completing many pages. How to maintain user's session information across all the web pages?

        In many situations, using cookies is the most efficient method of remembering and tracking preferences, purchases, commissions, and other information required for better visitor experience or site statistics.

        How It Works?
        Your server sends some data to the visitor's browser in the form of a cookie. The browser may accept the cookie. If it does, it is stored as a plain text record on the visitor's hard drive. Now, when the visitor arrives at another page on your site, the cookie is available for retrieval. Once retrieved, your server knows/remembers what was stored.
        Cookies are a plain text data record of 5 variable-length fields:
            Expires
                The date the cookie will expire. If this is blank, the cookie will expire when the visitor quits the browser.
            Domain
                The domain name of your site.
            Path
                The path to the directory or web page that sets the cookie. This may be blank if you want to retrieve the cookie from any directory or page.
            Secure
                If this field contains the word "secure", then the cookie may only be retrieved with a secure server. If this field is blank, no such restriction exists.
            Name=Value
                Cookies are set and retrieved in the form of key and value pairs.
            
    Setting up Cookies
        It is very easy to send cookies to browser. These cookies are sent along with HTTP Header before to Content-type field. Assuming you want to set UserID and Password as cookies. Setting the cookies is done as follows:
        html code
            print("Set-Cookie:UserID = XYZ;\r\n")
            print("Set-Cookie:Password = XYZ123;\r\n")
            print("Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT";\r\n")
            print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
            print("Set-Cookie:Path = /perl;\n")
            print("Content-type:text/html\r\n\r\n")
            ...........Rest of the HTML Content....

        From this example, you must have understood how to set cookies. We use Set-Cookie HTTP header to set cookies.
        It is optional to set cookies attributes like Expires, Domain, and Path. It is notable that cookies are set before sending magic line "Content-type:text/html\r\n\r\n.

    Retrieving Cookies
        It is very easy to retrieve all the set cookies. Cookies are stored in CGI environment variable HTTP_COOKIE and they will have following form.
            key1 = value1;key2 = value2;key3 = value3....

        python code
            # Import modules for CGI handling 
            from os import environ
            import cgi, cgitb

            if environ.has_key('HTTP_COOKIE'):
            for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
                (key, value ) = split(cookie, '=');
                if key == "UserID":
                    user_id = value

                if key == "Password":
                    password = value

            print "User ID  = %s" % user_id
            print "Password = %s" % password
    
        This produces the following result for the cookies set by above script 
            User ID = XYZ
            Password = XYZ123
        
    File Upload Example
        To upload a file, the HTML form must have the enctype attribute set to multipart/form-data. The input tag with the file type creates a "Browse" button.

        html code
            <html>
            <body>
                <form enctype = "multipart/form-data" 
                                    action = "save_file.py" method = "post">
                <p>File: <input type = "file" name = "filename" /></p>
                <p><input type = "submit" value = "Upload" /></p>
                </form>
            </body>
            </html>
        
        python code
            import cgi, os
            import cgitb; cgitb.enable()

            form = cgi.FieldStorage()

            # Get filename here.
            fileitem = form['filename']

            # Test if the file was uploaded
            if fileitem.filename:
            # strip leading path from file name to avoid 
            # directory traversal attacks
            fn = os.path.basename(fileitem.filename)
            open('/tmp/' + fn, 'wb').write(fileitem.file.read())

            message = 'The file "' + fn + '" was uploaded successfully'
            
            else:
            message = 'No file was uploaded'
            
            print """\
            Content-Type: text/html\n
            <html>
            <body>
            <p>%s</p>
            </body>
            </html>
            """ % (message,)

    How To Raise a "File Download" Dialog Box?
        print "Content-Type:application/octet-stream; name = \"FileName\"\r\n";
        print "Content-Disposition: attachment; filename = \"FileName\"\r\n\n";

        # Actual File Content will go here.
        fo = open("foo.txt", "rb")

        str = fo.read();
        print str

        # Close opend file
        fo.close()
'''



# Python - MySQL Database Access
'''
The Python standard for database interfaces is the Python DB-API. Most Python database interfaces adhere to this standard.
You can choose the right database for your application. Python Database API supports a wide range of database servers such as:
    GadFly
    mSQL
    MySQL
    PostgreSQL
    Microsoft SQL Server 2000
    Informix
    Interbase
    Oracle
    Sybase

Here is the list of available Python database interfaces:
    https://wiki.python.org/moin/DatabaseInterfaces
    You must download a separate DB API module for each database you need to access. For example, if you need to access an Oracle database as well as a MySQL database, you must download both the Oracle and the MySQL database modules.

The DB API provides a minimal standard for working with databases using Python structures and syntax wherever possible. This API includes the following:
    Importing the API module.
    Acquiring a connection with the database.
    Issuing SQL statements and stored procedures.
    Closing the connection

What is MySQLdb?
    We would learn all the concepts using MySQL, so let us talk about MySQLdb module.
    MySQLdb is an interface for connecting to a MySQL database server from Python. It implements the Python Database API v2.0 and is built on top of the MySQL C API.

    How do I Install MySQLdb?
    import MySQLdb

    Database Connection
        Before connecting to a MySQL database, make sure of the followings:
        You have created a database TESTDB.
        You have created a table EMPLOYEE in TESTDB.
        This table has fields FIRST_NAME, LAST_NAME, AGE, SEX and INCOME.
        User ID "testuser" and password "test123" are set to access TESTDB.
        Python module MySQLdb is installed properly on your machine.
        You have gone through MySQL tutorial to understand MySQL Basics.

        Example
        Following is the example of connecting with MySQL database "TESTDB"
            import MySQLdb

            # Open database connection
            db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # execute SQL query using execute() method.
            cursor.execute("SELECT VERSION()")

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            print "Database version : %s " % data

            # disconnect from server
            db.close()
    
    Creating Database Table
        import MySQLdb

        # Open database connection
        db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Drop table if it already exist using execute() method.
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

        # Create table as per requirement
        sql = """CREATE TABLE EMPLOYEE (
                FIRST_NAME  CHAR(20) NOT NULL,
                LAST_NAME  CHAR(20),
                AGE INT,  
                SEX CHAR(1),
                INCOME FLOAT )"""

        cursor.execute(sql)

        # disconnect from server
        db.close()
    
    INSERT Operation
        import MySQLdb

        # Open database connection
        db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                LAST_NAME, AGE, SEX, INCOME)
                VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
        db.close()

    Above example can be written as follows to create SQL queries dynamically 
        import MySQLdb

        # Open database connection
        db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
            LAST_NAME, AGE, SEX, INCOME) \
            VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
            ('Mac', 'Mohan', 20, 'M', 2000)
        try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
        db.close()

    READ Operation
        import MySQLdb

        # Open database connection
        db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = "SELECT * FROM EMPLOYEE \
            WHERE INCOME > '%d'" % (1000)
        try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # Now print fetched result
            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                    (fname, lname, age, sex, income )
        except:
        print "Error: unable to fecth data"

        # disconnect from server
        db.close()

    Update Operation
            
        import MySQLdb

        # Open database connection
        db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to UPDATE required records
        sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
                                WHERE SEX = '%c'" % ('M')
        try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
        db.close()

    DELETE Operation
            
        import MySQLdb

        # Open database connection
        db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to DELETE required records
        sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
        try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        except:
        # Rollback in case there is any error
        db.rollback()

        # disconnect from server
        db.close()

    Performing Transactions
        Transactions are a mechanism that ensures data consistency. Transactions have the following four properties:
            Atomicity
                Either a transaction completes or nothing happens at all.
            Consistency
                A transaction must start in a consistent state and leave the system in a consistent state.
            Isolation
                Intermediate results of a transaction are not visible outside the current transaction.
            Durability
                Once a transaction was committed, the effects are persistent, even after a system failure.

    The Python DB API 2.0 provides two methods to either commit or rollback a transaction.

    You already know how to implement transactions. Here is again similar example
        # Prepare SQL query to DELETE required records
        sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
        try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        except:
        # Rollback in case there is any error
        db.rollback()
    
    COMMIT Operation
        Commit is the operation, which gives a green signal to database to finalize the changes, and after this operation, no change can be reverted back.
        Here is a simple example to call commit method.
        db.commit()

    ROLLBACK Operation
        If you are not satisfied with one or more of the changes and you want to revert back those changes completely, then use rollback() method.        
        db.rollback()
    
    Disconnecting Database
        db.close()

    Handling Errors
        There are many sources of errors. A few examples are a syntax error in an executed SQL statement, a connection failure, or calling the fetch method for an already canceled or finished statement handle.
        he DB API defines a number of errors that must exist in each database module. The following table lists these exceptions.
            Warning
                Used for non-fatal issues. Must subclass StandardError.
            Error
                Base class for errors. Must subclass StandardError.
            InterfaceError
                Used for errors in the database module, not the database itself. Must subclass Error.
            DatabaseError
                Used for errors in the database. Must subclass Error.
            DataError
                Subclass of DatabaseError that refers to errors in the data.
            OperationalError
                Subclass of DatabaseError that refers to errors such as the loss of a connection to the database. These errors are generally outside of the control of the Python scripter.
            IntegrityError
                Subclass of DatabaseError for situations that would damage the relational integrity, such as uniqueness constraints or foreign keys.
            InternalError
                Subclass of DatabaseError that refers to errors internal to the database module, such as a cursor no longer being active.
            ProgrammingError
                Subclass of DatabaseError that refers to errors such as a bad table name and other things that can safely be blamed on you.
            NotSupportedError
                Subclass of DatabaseError that refers to trying to call unsupported functionality.
'''

# Networking - Sockets
'''
Los sockets son una poderosa herramienta de comunicación que se utiliza ampliamente en el mundo real, tanto en aplicaciones de red como en diversas áreas de desarrollo de software. Algunos ejemplos de cómo se utilizan los sockets en la vida real en Python son:

    Comunicación en red: Los sockets son esenciales para implementar la comunicación en red entre diferentes dispositivos y computadoras. Esto permite que los programas se comuniquen a través de Internet o una red local para intercambiar datos, compartir información y trabajar de manera colaborativa.

    Servidores y clientes: Los sockets son fundamentales en la implementación de arquitecturas cliente-servidor. Un servidor escucha en un socket y responde a las solicitudes que recibe de los clientes. Los clientes se conectan a los sockets del servidor para enviar solicitudes y recibir respuestas.

    Transferencia de datos: Los sockets son útiles para la transferencia de datos en tiempo real entre aplicaciones. Esto incluye la transmisión de archivos, la comunicación en tiempo real (como chat o videoconferencias) y la sincronización de información entre diferentes sistemas.

    APIs y servicios web: Muchas API y servicios web utilizan sockets para permitir que aplicaciones y servicios externos se comuniquen con ellos. Esto permite la integración de funcionalidades y el acceso a datos proporcionados por terceros.

    Streaming de datos: Los sockets se utilizan para la transmisión continua de datos, como en la transmisión de video y audio en tiempo real, donde los datos se envían y reciben a medida que están disponibles, en lugar de esperar a que se complete toda la transmisión.

    Juegos en línea y aplicaciones multiusuario: Los juegos en línea y otras aplicaciones multiusuario utilizan sockets para permitir que varios jugadores o usuarios interactúen y jueguen juntos en tiempo real.

    Internet de las cosas (IoT): En el contexto del IoT, los dispositivos inteligentes pueden comunicarse entre sí y con servicios en la nube a través de sockets, lo que permite la recopilación y el intercambio de datos.

    En resumen, los sockets son una herramienta versátil y esencial para la comunicación entre aplicaciones y dispositivos en redes. Python proporciona una API sencilla y potente para trabajar con sockets, lo que lo convierte en un lenguaje popular para desarrollar aplicaciones de red y servicios en el mundo real.

Python provides two levels of access to network services. At a low level, you can access the basic socket support in the underlying operating system, which allows you to implement clients and servers for both connection-oriented and connectionless protocols.
Python also has libraries that provide higher-level access to specific application-level network protocols, such as FTP, HTTP, and so on.
This chapter gives you understanding on most famous concept in Networking - Socket Programming.

What is Sockets?
    Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.
    Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on. The socket library provides specific classes for handling the common transports as well as a generic interface for handling the rest.

Socket Vocabulary
Sockets have their own vocabulary
    Domain
        The family of protocols that is used as the transport mechanism. These values are constants such as AF_INET, PF_INET, PF_UNIX, PF_X25, and so on.	
    type
        The type of communications between the two endpoints, typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.	
    protocol
        Typically zero, this may be used to identify a variant of a protocol within a domain and type.	
    hostname
        The identifier of a network interface:
        A string, which can be a host name, a dotted-quad address, or an IPV6 address in colon (and possibly dot) notation
        A string "<broadcast>", which specifies an INADDR_BROADCAST address.
        A zero-length string, which specifies INADDR_ANY, or
        An Integer, interpreted as a binary address in host byte order.	
    port
        Each server listens for clients calling on one or more ports. A port may be a Fixnum port number, a string containing a port number, or the name of a service.


The socket Module
    To create a socket, you must use the socket.socket() function available in socket module, which has the general syntax:
    s = socket.socket (socket_family, socket_type, protocol=0)
    Here is the description of the parameters
        socket_family
            This is either AF_UNIX or AF_INET, as explained earlier.
        socket_type
            This is either SOCK_STREAM or SOCK_DGRAM.
        protocol
            This is usually left out, defaulting to 0.

Server Socket Methods
    Once you have socket object, then you can use required functions to create your client or server program. Following is the list of functions required
    s.bind()
        This method binds address (hostname, port number pair) to socket.
    s.listen()
        This method sets up and start TCP listener.
    s.accept()
        This passively accept TCP client connection, waiting until connection arrives (blocking).
    
Client Socket Methods
s.connect()
    This method actively initiates TCP server connection.

General Socket Methods
    s.recv()
        This method receives TCP message
    s.send()
        This method transmits TCP message
    s.recvfrom()
        This method receives UDP message
    s.sendto()
        This method transmits UDP message
    s.close()
        This method closes socket
    socket.gethostname()
        Returns the hostname.

A Simple Server
    To write Internet servers, we use the socket function available in socket module to create a socket object. A socket object is then used to call other functions to setup a socket server.
    Now call bind(hostname, port) function to specify a port for your service on the given host.
    Next, call the accept method of the returned object. This method waits until a client connects to the port you specified, and then returns a connection object that represents the connection to that client.

        import socket               # Import socket module

        s = socket.socket()         # Create a socket object
        host = socket.gethostname() # Get local machine name
        print(host)
        port = 2345                # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port

        s.listen(5)                 # Now wait for client connection.
        while True:
            c, addr = s.accept()     # Establish connection with client.
            print('Got connection from', addr)
            c.send('Thank you for connecting'.encode('utf-8'))
            c.close()                # Close the connection

A Simple Client
    To write Internet servers, we use the socket function available in socket module to create a socket object. A socket object is then used to call other functions to setup a socket server.

    Now call bind(hostname, port) function to specify a port for your service on the given host.

    Next, call the accept method of the returned object. This method waits until a client connects to the port you specified, and then returns a connection object that represents the connection to that client.

        import socket               # Import socket module

        s = socket.socket()         # Create a socket object
        host = socket.gethostname() # Get local machine name
        port = 2345                # Reserve a port for your service.

        s.connect((host, port))
        print(s.recv(1024))
        s.close()                     # Close the socket when done


Python Internet modules
    Protocol	Common function	    Port No	    Python module
    HTTP	    Web pages	        80	        httplib, urllib, xmlrpclib
    NNTP	    Usenet news	        119	        nntplib
    FTP	        File transfers	    20	        ftplib, urllib
    SMTP	    Sending email	    25	        smtplib
    POP3	    Fetching email	    110	        poplib
    IMAP4	    Fetching email	    143	        imaplib
    Telnet	    Command lines	    23	        telnetlib
    Gopher	    Document transfers	70	        gopherlib, urllib

Please check all the libraries mentioned above to work with FTP, SMTP, POP, and IMAP protocols.


Further Readings
    https://www.tutorialspoint.com/unix_sockets/index.htm
    https://docs.python.org/3.0/library/socket.html
'''


# Python - Sending Email using SMTP
'''
Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.

Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

Here is a simple syntax to create one SMTP object, which can later be used to send an e-mail:
    import smtplib
    smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

Here is the detail of the parameters:
    host
        This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. This is optional argument.
    port
        If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.
    local_hostname
        If your SMTP server is running on your local machine, then you can specify just localhost as of this option.

An SMTP object has an instance method called sendmail, which is typically used to do the work of mailing a message. It takes three parameters:
    The sender
        A string with the address of the sender.
    The receivers
        A list of strings, one for each recipient.
    The message
        A message as a string formatted as specified in the various RFCs.

python code example:
    import yagmail

    # Configurar las credenciales yagmail
    yag = yagmail.SMTP('zelmobedra@gufum.com',  '')

    # El mensaje a enviar
    subject = "SMTP e-mail test"
    body = "This is a test e-mail message."

    # Enviar el correo electrónico
    yag.send('zelmobedra@gufum.com', subject, body)

    print("Successfully sent email")


Sending an HTML e-mail using Python

    import smtplib

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: SMTP HTML e-mail test

    This is an e-mail message to be sent in HTML format

    <b>This is HTML message.</b>
    <h1>This is headline.</h1>
    """

    try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"
    except SMTPException:
    print "Error: unable to send email"

Sending Attachments as an E-mail

    import smtplib
    import base64

    filename = "/tmp/test.txt"

    # Read a file and encode it into base64 format
    fo = open(filename, "rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)  # base64

    sender = 'webmaster@tutorialpoint.com'
    reciever = 'amrood.admin@gmail.com'

    marker = "AUNIQUEMARKER"

    body ="""
    This is a test email to send an attachement.
    """
    # Define the main headers.
    part1 = """From: From Person <me@fromdomain.net>
    To: To Person <amrood.admin@gmail.com>
    Subject: Sending Attachement
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary=%s
    --%s
    """ % (marker, marker)

    # Define the message action
    part2 = """Content-Type: text/plain
    Content-Transfer-Encoding:8bit

    %s
    --%s
    """ % (body,marker)

    # Define the attachment section
    part3 = """Content-Type: multipart/mixed; name=\"%s\"
    Content-Transfer-Encoding:base64
    Content-Disposition: attachment; filename=%s

    %s
    --%s--
    """ %(filename, filename, encodedcontent, marker)
    message = part1 + part2 + part3

    try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, reciever, message)
    print "Successfully sent email"
    except Exception:
    print "Error: unable to send email"
   
'''

# Python - Multithreaded Programming
'''
Running several threads is similar to running several different programs concurrently, but with the following benefits −

Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.

Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context it is currently running.

It can be pre-empted (interrupted)

It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.



Starting a New Thread
    To spawn another thread, you need to call following method available in thread module −

    thread.start_new_thread ( function, args[, kwargs] )
    This method call enables a fast and efficient way to create new threads in both Linux and Windows.

    The method call returns immediately and the child thread starts and calls function with the passed list of args. When function returns, the thread terminates.

    Here, args is a tuple of arguments; use an empty tuple to call function without passing any arguments. kwargs is an optional dictionary of keyword arguments.

        import thread
        import time

        # Define a function for the thread
        def print_time( threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % ( threadName, time.ctime(time.time()) ))

        # Create two threads as follows
        try:
        thread.start_new_thread( print_time, ("Thread-1", 2, ) )
        thread.start_new_thread( print_time, ("Thread-2", 4, ) )
        except:
        print("Error: unable to start thread")

        while 1:
        pass


    When the above code is executed, it produces the following result −

    Thread-1: Thu Jan 22 15:42:17 2009
    Thread-1: Thu Jan 22 15:42:19 2009
    Thread-2: Thu Jan 22 15:42:19 2009
    Thread-1: Thu Jan 22 15:42:21 2009
    Thread-2: Thu Jan 22 15:42:23 2009
    Thread-1: Thu Jan 22 15:42:23 2009
    Thread-1: Thu Jan 22 15:42:25 2009
    Thread-2: Thu Jan 22 15:42:27 2009
    Thread-2: Thu Jan 22 15:42:31 2009
    Thread-2: Thu Jan 22 15:42:35 2009

Although it is very effective for low-level threading, but the thread module is very limited compared to the newer threading module.

The Threading Module
    The newer threading module included with Python 2.4 provides much more powerful, high-level support for threads than the thread module discussed in the previous section.

    The threading module exposes all the methods of the thread module and provides some additional methods:

        threading.activeCount()
            Returns the number of thread objects that are active.

        threading.currentThread()
            Returns the number of thread objects in the caller's thread control.

        threading.enumerate()
            Returns a list of all thread objects that are currently active.

In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows:
    run()
        The run() method is the entry point for a thread.
    start()
        The start() method starts a thread by calling the run method.
    join([time])
        The join() waits for threads to terminate.
    isAlive()
        The isAlive() method checks whether a thread is still executing.
    getName()
        The getName() method returns the name of a thread.
    setName()
        The setName() method sets the name of a thread.

Creating Thread Using Threading Module
    To implement a new thread using the threading module, you have to do the following
        Define a new subclass of the Thread class.
        Override the __init__(self [,args]) method to add additional arguments.
        Then, override the run(self [,args]) method to implement what the thread should do when started.
    
    Once you have created the new Thread subclass, you can create an instance of it and then start a new thread by invoking the start(), which in turn calls run() method.

    import threading
    import time

    exitFlag = 0

    class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print_time(self.name, 5, self.counter)
        print "Exiting " + self.name

    def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()

    print "Exiting Main Thread"

When the above code is executed, it produces the following result −

    Starting Thread-1
    Starting Thread-2
    Exiting Main Thread
    Thread-1: Thu Mar 21 09:10:03 2013
    Thread-1: Thu Mar 21 09:10:04 2013
    Thread-2: Thu Mar 21 09:10:04 2013
    Thread-1: Thu Mar 21 09:10:05 2013
    Thread-1: Thu Mar 21 09:10:06 2013
    Thread-2: Thu Mar 21 09:10:06 2013
    Thread-1: Thu Mar 21 09:10:07 2013
    Exiting Thread-1
    Thread-2: Thu Mar 21 09:10:08 2013
    Thread-2: Thu Mar 21 09:10:10 2013
    Thread-2: Thu Mar 21 09:10:12 2013
    Exiting Thread-2


Synchronizing Threads
    The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to synchronize threads. A new lock is created by calling the Lock() method, which returns the new lock.

    The acquire(blocking) method of the new lock object is used to force threads to run synchronously. The optional blocking parameter enables you to control whether the thread waits to acquire the lock.

    If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for the lock to be released.

    The release() method of the new lock object is used to release the lock when it is no longer required.

        import threading
        import time

        class myThread (threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
        def run(self):
            print "Starting " + self.name
            # Get lock to synchronize threads
            threadLock.acquire()
            print_time(self.name, self.counter, 3)
            # Free lock to release next thread
            threadLock.release()

        def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print "%s: %s" % (threadName, time.ctime(time.time()))
            counter -= 1

        threadLock = threading.Lock()
        threads = []

        # Create new threads
        thread1 = myThread(1, "Thread-1", 1)
        thread2 = myThread(2, "Thread-2", 2)

        # Start new Threads
        thread1.start()
        thread2.start()

        # Add threads to thread list
        threads.append(thread1)
        threads.append(thread2)

        # Wait for all threads to complete
        for t in threads:
            t.join()
        print "Exiting Main Thread"

    When the above code is executed, it produces the following result −

        Starting Thread-1
        Starting Thread-2
        Thread-1: Thu Mar 21 09:11:28 2013
        Thread-1: Thu Mar 21 09:11:29 2013
        Thread-1: Thu Mar 21 09:11:30 2013
        Thread-2: Thu Mar 21 09:11:32 2013
        Thread-2: Thu Mar 21 09:11:34 2013
        Thread-2: Thu Mar 21 09:11:36 2013
        Exiting Main Thread

Multithreaded Priority Queue
    The Queue module allows you to create a new queue object that can hold a specific number of items. There are following methods to control the Queue:
        get()
            The get() removes and returns an item from the queue.
        put()
            The put adds item to a queue.
        qsize()
            The qsize() returns the number of items that are currently in the queue.
        empty()
            The empty( ) returns True if queue is empty; otherwise, False.
        full()
            the full() returns True if queue is full; otherwise, False.
    
    python code
        import Queue
        import threading
        import time

        exitFlag = 0

        class myThread (threading.Thread):
        def __init__(self, threadID, name, q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
        def run(self):
            print "Starting " + self.name
            process_data(self.name, self.q)
            print "Exiting " + self.name

        def process_data(threadName, q):
        while not exitFlag:
            queueLock.acquire()
                if not workQueue.empty():
                    data = q.get()
                    queueLock.release()
                    print "%s processing %s" % (threadName, data)
                else:
                    queueLock.release()
                time.sleep(1)

        threadList = ["Thread-1", "Thread-2", "Thread-3"]
        nameList = ["One", "Two", "Three", "Four", "Five"]
        queueLock = threading.Lock()
        workQueue = Queue.Queue(10)
        threads = []
        threadID = 1

        # Create new threads
        for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

        # Fill the queue
        queueLock.acquire()
        for word in nameList:
        workQueue.put(word)
        queueLock.release()

        # Wait for queue to empty
        while not workQueue.empty():
        pass

        # Notify threads it's time to exit
        exitFlag = 1

        # Wait for all threads to complete
        for t in threads:
        t.join()
        print "Exiting Main Thread"

When the above code is executed, it produces the following result −

    Starting Thread-1
    Starting Thread-2
    Starting Thread-3
    Thread-1 processing One
    Thread-2 processing Two
    Thread-3 processing Three
    Thread-1 processing Four
    Thread-2 processing Five
    Exiting Thread-3
    Exiting Thread-1
    Exiting Thread-2
    Exiting Main Thread
'''


# Python - XML Processing
'''
XML is a portable, open source language that allows programmers to develop applications that can be read by other applications, regardless of operating system and/or developmental language.

What is XML?
    The Extensible Markup Language (XML) is a markup language much like HTML or SGML. This is recommended by the World Wide Web Consortium and available as an open standard.

    XML is extremely useful for keeping track of small to medium amounts of data without requiring a SQL-based backbone.

XML Parser Architectures and APIs
    The Python standard library provides a minimal but useful set of interfaces to work with XML.
    The two most basic and broadly used APIs to XML data are the SAX and DOM interfaces.

    Simple API for XML (SAX) − Here, you register callbacks for events of interest and then let the parser proceed through the document. This is useful when your documents are large or you have memory limitations, it parses the file as it reads it from disk and the entire file is never stored in memory.

    Document Object Model (DOM) API − This is a World Wide Web Consortium recommendation wherein the entire file is read into memory and stored in a hierarchical (tree-based) form to represent all the features of an XML document.

    SAX obviously cannot process information as fast as DOM can when working with large files. On the other hand, using DOM exclusively can really kill your resources, especially if used on a lot of small files.

    SAX is read-only, while DOM allows changes to the XML file. Since these two different APIs literally complement each other, there is no reason why you cannot use them both for large projects.

For all our XML code examples, let's use a simple XML file movies.xml as an input −

    <collection shelf="New Arrivals">
    <movie title="Enemy Behind">
    <type>War, Thriller</type>
    <format>DVD</format>
    <year>2003</year>
    <rating>PG</rating>
    <stars>10</stars>
    <description>Talk about a US-Japan war</description>
    </movie>
    <movie title="Transformers">
    <type>Anime, Science Fiction</type>
    <format>DVD</format>
    <year>1989</year>
    <rating>R</rating>
    <stars>8</stars>
    <description>A schientific fiction</description>
    </movie>
    <movie title="Trigun">
    <type>Anime, Action</type>
    <format>DVD</format>
    <episodes>4</episodes>
    <rating>PG</rating>
    <stars>10</stars>
    <description>Vash the Stampede!</description>
    </movie>
    <movie title="Ishtar">
    <type>Comedy</type>
    <format>VHS</format>
    <rating>PG</rating>
    <stars>2</stars>
    <description>Viewable boredom</description>
    </movie>
    </collection>


Parsing XML with SAX APIs
    SAX is a standard interface for event-driven XML parsing. Parsing XML with SAX generally requires you to create your own ContentHandler by subclassing xml.sax.ContentHandler.

    Your ContentHandler handles the particular tags and attributes of your flavor(s) of XML. A ContentHandler object provides methods to handle various parsing events. Its owning parser calls ContentHandler methods as it parses the XML file.

    The methods startDocument and endDocument are called at the start and the end of the XML file. The method characters(text) is passed character data of the XML file via the parameter text.

    The ContentHandler is called at the start and end of each element. If the parser is not in namespace mode, the methods startElement(tag, attributes) and endElement(tag) are called; otherwise, the corresponding methods startElementNS and endElementNS are called. Here, tag is the element tag, and attributes is an Attributes object.

Here are other important methods to understand before proceeding −
    The make_parser Method
    Following method creates a new parser object and returns it. The parser object created will be of the first parser type the system finds.

    xml.sax.make_parser( [parser_list] )
    Here is the detail of the parameters −

    parser_list − The optional argument consisting of a list of parsers to use which must all implement the make_parser method.

The parse Method
    Following method creates a SAX parser and uses it to parse a document.

    xml.sax.parse( xmlfile, contenthandler[, errorhandler])
    Here is the detail of the parameters −

    xmlfile − This is the name of the XML file to read from.

    contenthandler − This must be a ContentHandler object.

    errorhandler − If specified, errorhandler must be a SAX ErrorHandler object.


The parseString Method
    There is one more method to create a SAX parser and to parse the specified XML string.

    xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
    Here is the detail of the parameters −

    xmlstring − This is the name of the XML string to read from.

    contenthandler − This must be a ContentHandler object.

    errorhandler − If specified, errorhandler must be a SAX ErrorHandler object.

python code
        import xml.sax

        class MovieHandler( xml.sax.ContentHandler ):
        def __init__(self):
            self.CurrentData = ""
            self.type = ""
            self.format = ""
            self.year = ""
            self.rating = ""
            self.stars = ""
            self.description = ""

        # Call when an element starts
        def startElement(self, tag, attributes):
            self.CurrentData = tag
            if tag == "movie":
                print "*****Movie*****"
                title = attributes["title"]
                print "Title:", title

        # Call when an elements ends
        def endElement(self, tag):
            if self.CurrentData == "type":
                print "Type:", self.type
            elif self.CurrentData == "format":
                print "Format:", self.format
            elif self.CurrentData == "year":
                print "Year:", self.year
            elif self.CurrentData == "rating":
                print "Rating:", self.rating
            elif self.CurrentData == "stars":
                print "Stars:", self.stars
            elif self.CurrentData == "description":
                print "Description:", self.description
            self.CurrentData = ""

        # Call when a character is read
        def characters(self, content):
            if self.CurrentData == "type":
                self.type = content
            elif self.CurrentData == "format":
                self.format = content
            elif self.CurrentData == "year":
                self.year = content
            elif self.CurrentData == "rating":
                self.rating = content
            elif self.CurrentData == "stars":
                self.stars = content
            elif self.CurrentData == "description":
                self.description = content
        
        if ( __name__ == "__main__"):
        
        # create an XMLReader
        parser = xml.sax.make_parser()
        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        # override the default ContextHandler
        Handler = MovieHandler()
        parser.setContentHandler( Handler )
        
        parser.parse("movies.xml")

This would produce following result
    *****Movie*****
    Title: Enemy Behind
    Type: War, Thriller
    Format: DVD
    Year: 2003
    Rating: PG
    Stars: 10
    Description: Talk about a US-Japan war
    *****Movie*****
    Title: Transformers
    Type: Anime, Science Fiction
    Format: DVD
    Year: 1989
    Rating: R
    Stars: 8
    Description: A schientific fiction
    *****Movie*****
    Title: Trigun
    Type: Anime, Action
    Format: DVD
    Rating: PG
    Stars: 10
    Description: Vash the Stampede!
    *****Movie*****
    Title: Ishtar
    Type: Comedy
    Format: VHS
    Rating: PG
    Stars: 2
    Description: Viewable boredom

For a complete detail on SAX API documentation, please refer to standard Python SAX APIs.
    Parsing XML with DOM APIs
    The Document Object Model ("DOM") is a cross-language API from the World Wide Web Consortium (W3C) for accessing and modifying XML documents.

    The DOM is extremely useful for random-access applications. SAX only allows you a view of one bit of the document at a time. If you are looking at one SAX element, you have no access to another.

    Here is the easiest way to quickly load an XML document and to create a minidom object using the xml.dom module. The minidom object provides a simple parser method that quickly creates a DOM tree from the XML file.

    The sample phrase calls the parse( file [,parser] ) function of the minidom object to parse the XML file designated by file into a DOM tree object.

Python code
    from xml.dom.minidom import parse
    import xml.dom.minidom

    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse("movies.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
    print "Root element : %s" % collection.getAttribute("shelf")

    # Get all the movies in the collection
    movies = collection.getElementsByTagName("movie")

    # Print detail of each movie.
    for movie in movies:
    print "*****Movie*****"
    if movie.hasAttribute("title"):
        print "Title: %s" % movie.getAttribute("title")

    type = movie.getElementsByTagName('type')[0]
    print "Type: %s" % type.childNodes[0].data
    format = movie.getElementsByTagName('format')[0]
    print "Format: %s" % format.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    print "Rating: %s" % rating.childNodes[0].data
    description = movie.getElementsByTagName('description')[0]
    print "Description: %s" % description.childNodes[0].data

This would produce the following result

    Root element : New Arrivals
    *****Movie*****
    Title: Enemy Behind
    Type: War, Thriller
    Format: DVD
    Rating: PG
    Description: Talk about a US-Japan war
    *****Movie*****
    Title: Transformers
    Type: Anime, Science Fiction
    Format: DVD
    Rating: R
    Description: A schientific fiction
    *****Movie*****
    Title: Trigun
    Type: Anime, Action
    Format: DVD
    Rating: PG
    Description: Vash the Stampede!
    *****Movie*****
    Title: Ishtar
    Type: Comedy
    Format: VHS
    Rating: PG
    Description: Viewable boredom
'''

# Python - GUI Programming (Tkinter)
''' TKInter
Python provides various options for developing graphical user interfaces (GUIs). Most important are listed below.

    Tkinter:
        Tkinter is the Python interface to the Tk GUI toolkit shipped with Python. We would look this option in this chapter.
    wxPython:
        This is an open-source Python interface for wxWindows http://wxpython.org.
    JPython:
        JPython is a Python port for Java which gives Python scripts seamless access to Java class libraries on the local machine http://www.jython.org.

There are many other interfaces available, which you can find them on the net.

Tkinter Programming
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

Creating a GUI application using Tkinter is an easy task. All you need to do is perform the following steps:
    Import the Tkinter module.
    Create the GUI application main window.
    Add one or more of the above-mentioned widgets to the GUI application.
    Enter the main event loop to take action against each event triggered by the user.

Tkinter Widgets
    Button
        The Button widget is used to display buttons in your application.
    Canvas
        The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.
    Checkbutton
        The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.
    Entry
        The Entry widget is used to display a single-line text field for accepting values from a user.
    Frame
        The Frame widget is used as a container widget to organize other widgets.
    Label
        The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
    Listbox
        The Listbox widget is used to provide a list of options to a user.
    Menubutton
        The Menubutton widget is used to display menus in your application.
    Menu
        The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.
    Message
        The Message widget is used to display multiline text fields for accepting values from a user.
    Radiobutton
        The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.
    Scale
        The Scale widget is used to provide a slider widget.
    Scrollbar
        The Scrollbar widget is used to add scrolling capability to various widgets, such as list boxes.
    Text
        The Text widget is used to display text in multiple lines.
    Toplevel
        The Toplevel widget is used to provide a separate window container.
    Spinbox
        The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed number of values.
    PanedWindow
        A PanedWindow is a container widget that may contain any number of panes, arranged horizontally or vertically.
    LabelFrame
        A labelframe is a simple container widget. Its primary purpose is to act as a spacer or container for complex window layouts.
    tkMessageBox
        This module is used to display message boxes in your applications.


Standard attributes
    Dimensions
    Colors
    Fonts
    Anchors
    Relief styles
    Bitmaps
    Cursors

Geometry Management
    All Tkinter widgets have access to specific geometry management methods, which have the purpose of organizing widgets throughout the parent widget area. Tkinter exposes the following geometry manager classes: pack, grid, and place.

    The pack() Method
        This geometry manager organizes widgets in blocks before placing them in the parent widget.
    The grid() Method
        This geometry manager organizes widgets in a table-like structure in the parent widget.
    The place() Method
        This geometry manager organizes widgets by placing them in a specific position in the parent widget.

    Let us study the geometry management methods briefly

'''


# Python Generators
# Python Closures
# Python Decorators
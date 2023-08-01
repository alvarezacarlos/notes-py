#..............................LANGUAGE STRUCTURE Fundamental Elements: https://www.python.org/doc/
''' 
    1. Interactive Modes
    2. Syntax
    3. Data Types
    4. Variables
    5. Operators
    6. Control Structures
    7. Functions/Methods
    8. Input/Output
    9. Libraries/Modules
    10. Error Handling
    11. Comments
'''

#Python
'''
    general-purpose
    interpreted
    interactive
    object-oriented
    high-level

    Python is Interpreted: Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to PERL and PHP.
    Python is Interactive: You can actually sit at a Python prompt and interact with the interpreter directly to write your programs.
    Python is Object-Oriented: Python supports Object-Oriented style or technique of programming that encapsulates code within objects.
    Python is Open Source which means its available free of cost.
    Python is simple and so easy to learn.
    Python is versatile and can be used to create many different things.
    Python has powerful development libraries include AI, ML etc.
    It supports functional and structured programming methods as well as OOP.
    It can be used as a scripting language or can be compiled to byte-code for building large applications.
    It provides very high-level dynamic data types and supports dynamic type checking.
    It supports automatic garbage collection.
    It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java.
    Portable: Python can run on a wide variety of hardware platforms and has the same interface on all platforms.
    Extendable: You can add low-level modules to the Python interpreter. These modules enable programmers to add to or customize their tools to be more efficient.
    Databases: Python provides interfaces to all major commercial databases.
    GUI Programming: Python supports GUI applications that can be created and ported to many system calls, libraries and windows systems, such as Windows MFC, Macintosh, and the X Window system of Unix.
    Scalable: Python provides a better structure and support for large programs than shell scripting.

    created by: Guido van Rossum
    on: 1985-1990
    where: The National Research Institute for Mathematics and Computer Science in the Netherlands.
    Python is derived from many other languages, including ABC, Modula-3, C, C++, Algol-68, SmallTalk, and Unix shell and other scripting languages.
    Python source code is also available under the GNU General Public License (GPL).
    Python is copyrighted. Like Perl, Python source code is now available under the GNU General Public License (GPL).

    Programming Paradigms:
        Procedural
        Object Oriented
        Functional

    Python Jobs: 
        websites
        software components
        Data Science
        AI
        ML technologies

    Careers with Python
    If you know Python nicely, then you have a great career ahead. 
    Here are just a few of the career options where Python is a key skill:
    Game developer
    Web designer
    Python developer
    Full-stack developer
    Machine learning engineer
    Data scientist
    Data analyst
    Data engineer
    DevOps engineer
    Software engineer
    Many more other roles
'''


#**********Interactive Modes
'''
    CLI Interactive Mode
    Script Mode Programming
'''

#********** Syntax
'''
    Syntax defines the set of rules and conventions that dictate how code should be written in a particular programming language. 
    It specifies how statements and expressions should be structured and how different elements should be combined.
'''

#********** Data Types
'''
    Programming languages typically provide various data types to represent different kinds of values, such as integers, floating-point numbers, strings, booleans, and more. These data types determine how data is stored in memory and the operations that can be performed on them.
'''

#********** Variables
'''
    Variables are used to store and manipulate data within a program. They have a name and a data type and can hold different values during program execution. Variables allow programmers to manage and manipulate data dynamically.
'''

#********** Operators
'''
    Arithmetic Operators
    Comparison (Relational) Operators
    Assignment Operators
    Logical Operators
    Bitwise Operators
    Membership Operators
    Identity Operators
'''

#********** Control Structures
'''
    Control structures enable programmers to control the flow of execution within a program. Common control structures include conditionals (if-else statements, switch statements), loops (for loops, while loops), and branching (goto statements, function calls).
'''

#********** Functions/Methods
'''
    Functions or methods are reusable blocks of code that perform a specific task. They encapsulate a series of instructions and can be called multiple times within a program. Functions enhance code modularity, reusability, and maintainability.
'''

#********** Input/Output
'''
    Programming languages provide mechanisms to interact with the user or the outside world. Input mechanisms allow the program to receive data from external sources, such as user input or files. Output mechanisms enable the program to display information, write to files, or communicate with other systems.
'''


#********** Libraries/Modules
'''
    Many programming languages offer libraries or modules that provide pre-written code to perform common tasks. These libraries contain functions, classes, and other resources that can be imported into a program to extend its capabilities and reduce development time.
'''

#********** Error Handling
'''
    Languages include mechanisms to handle errors and exceptions that may occur during program execution. Error handling allows programmers to anticipate and handle exceptional situations gracefully, preventing crashes or unexpected behavior.
'''

#********** Comments
''' 
    Comments are non-executable lines of code used to provide explanations or annotate the code. They are ignored by the compiler or interpreter and serve as documentation for programmers and future maintainers of the code.
    These are the fundamental elements of a coding language structure. However, it's important to note that different programming languages have their own specific features, paradigms, and additional constructs that may not be present in all languages.
'''


#................................PYTHON LANGEUAGE SRUCTURE
#********** Syntax
#***** Identifiers
'''
    A Python identifier is a name used to identify a variable, function, class, module or other object
    Python Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
    Starting an identifier with a single leading underscore indicates that the identifier is private identifier.
    Starting an identifier with two leading underscores indicates a strongly private identifier.
    If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.
'''

#***** Reserved Words
'''
    and
    as
    assert
    break
    class
    continue
    def
    del
    elif
    else
    except
    False
    finally
    for
    from
    global
    if
    import
    in
    is
    lambda
    None
    nonlocal
    not
    or
    pass
    raise
    return
    True
    try
    while
    with
    yield
'''

#***** Lines and Indentation
'''
    Python programming provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.
'''

#***** Multi-Line Statements
'''
    Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character (\) to denote that the line should continue.
'''
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

'''
    Statements contained within the [], {}, or () brackets do not need to use the line continuation character. For example following statement works well in Python −
'''
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']



#***** Quotations in Python
    # Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
    # The triple quotes are used to span the string across multiple lines. For example, all the following are legal

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is 
made up of multiple 
lines and sentences."""

#***** Comments
'''
    explanation or annotation in the Python source code. They are added with the purpose of making the source code easier for humans to understand, and are ignored by Python interpreter
    A hash sign (#) that is not inside a string literal begins a comment.
    Rriple-quoted string is also ignored by Python interpreter and can be used as a multiline comments:
'''
# First comment
'''
This is a multiline
comment.
'''

#***** Blank Lines
'''
    A line containing only whitespace, possibly with a comment, is known as a blank line and Python totally ignores it.
    In an interactive interpreter session, you must enter an empty physical line to terminate a multiline statement.
'''

#***** input stetaments
input("\n\nPress the enter key to exit.")

#***** Multiple Statements on a Single Line
import sys; x = 'foo'; sys.stdout.write(x + '\n')

#***** Multiple Statement Groups as Suites
'''
    Compound or complex statements, such as if, while, def, and class require a header line and a suite.
    Header lines begin the statement (with the keyword) and terminate with a colon ( : ) and are followed by one or more lines which make up the suite.
'''
'''
    if expression :
    suite
    elif expression :
    suite
    else :
    suite
'''

#***** Command Line Arguments in Python
'''
    You can program your script in such a way that it should accept various options. Command Line Arguments    
'''
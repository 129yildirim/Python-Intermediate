import re

print('Inside \'re\' module, there are these:\t', dir(re), '\n')


#   ----------------- RE MODULE--------------------

strn = "Hey this is a text. To be or not. Maybe to not be is better right? Maybe not. Actually the answer is simple enough: I don't know"

find_all = re.findall('be', strn)
print('all \'be\' words in str:\t', find_all)
print('how many are they:\t', len(find_all))

sub = re.sub(' ', '-', strn)
print('sub:\t', sub)

search = re.search('be', strn)
print('search:\t', search)
print('span:\t', search.span())
print('group:\t', search.group())

# --------------- REGULAR EXPRESSION --------------

"""
    [] -> Search all characters inside brackets
        [abc]   ->      a:1 match   ac:2 matches    Phython:No matches
        [a-e]   ->      [abcde]
        [1-5]   ->      [12345]
        [0-39]  ->      [01239]
        [^abc]  ->      the characters except abc
        [^0-9]  ->      the characters that are not number
"""

print('abc chars in strn:\t', re.findall("[abc]", strn))
print('cde chars in strn:\t', re.findall("[c-e]", strn))
print('cde chars in strn:\t', re.findall("[c-e]", strn))
print('chars except abc:\t', re.findall("[^abc]", strn))

"""
    .   -> A single character
        ..  ->      a:No match    az:1 match    asj:1 match    asdg:2 match      

"""

print('The words that starts with \'May\' and have 2 ch after:\t', re.findall("May..", strn))

"""
    ^   ->  Starts with the characters that shown or not?
        ^H  ->      tetx:No match   hey:no Match    Hello:1 match

    $   ->  Ends with the characters that shown or not?
        w$  ->      tax:no match    know:1 match    

"""

print('Starts with \'He\' or not?', re.findall('^He', strn))
print('Starts with \'a\' or not?', re.findall('^a', strn))
print('Ends with \'w\' or not?', re.findall('w$', strn))
print('Ends with \'r\' or not?', re.findall('r$', strn))

"""
    *   ->  Check a character whether exists 0 or more times in the right order.
        ma*n    ->    mn:1 match(a exists 0 time)    man:1 match(a exists)    maaaaan:1 match(exists)    main:No match('n' char should be after a) 

    +   -> almost same as the '*'. Only difference is it cheks if it exists 1 or more but not less

    ?   -> similiar to the examples above. Difference is this one checks if it exists 1 or 0 times
    
"""
"""
    {}  ->  It checks the number of a character
        al{2}       ->    'l' character should repeat 2 times after 'a' character
        al{2,3}     ->    'l' character should repeat at least 2 and at most 3 times after 'a' character
        [0-9]{2,4}  ->    the numbers at least 2 at most 4

"""
"""
    |   -> Or operation
        a|b     ->      cde:No match    hau:1 match    ababpoia:5 matches

    ()  -> Used for grouping
"""

"""
    \   -> Used for checking the special characters but not alphanumeric characters
        \$a     ->      hea:No match    he$a:1 match(the engine doesn't interpret the '$' character. It sees it as a normal character like all others)

"""




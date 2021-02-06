'''
s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
s.strip() -- returns a string with whitespace removed from the start and end
s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
'''

def format_example():
    first_name ="Jake"
    last_name ="state Farm"
    name = f"{first_name} from {last_name}"

    second_name ='{} from second {}'.format(first_name,last_name)
    print(name)
    print(second_name)

def strip_whitespace():
    fav_language =' Java 11 '
    print(fav_language.lstrip())
    print(fav_language.lstrip())
    if fav_language.lstrip() == fav_language.rstrip():
        print('same')
    elif fav_language.strip() == 'Java 11':
        print('cool')
    else:
        print('not lucky')

# format_example()
strip_whitespace()
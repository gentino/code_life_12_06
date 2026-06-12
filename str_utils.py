def vowels_count(word):
    count =sum(1 for alpha in word if  alpha in 'aeouiAEOUI')
    return count

def vowels_list(word):
    '''
        returns the list of vowels found in a word 
    '''
    vowels = [ x for x in  word if x in 'aeouiAEOUI']
    return vowels

# help('modules')

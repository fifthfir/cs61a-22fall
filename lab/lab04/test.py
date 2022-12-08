def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """
    def add_chars_helper(w1, w2, add = ''):
        if len(w1) == 0:
            return add + w2
        else:
            if w1[0] == w2[0]:
                return add_chars_helper(w1[1:], w2[1:], add)
            else:
                return add_chars_helper(w1, w2[1:], add + w2[0])
        
    return add_chars_helper(w1, w2)
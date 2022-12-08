def degit_replacer(predicate, transformer):
    def replace(n):
        digit = 0
        result = 0
        while n > 0:
            i = n % 10
            if predicate(i):
                i = transformer(i)
            result += transformer(i) * (10 ** digit)
            digit += 1
            n = n // 10
        return result    
    return replace
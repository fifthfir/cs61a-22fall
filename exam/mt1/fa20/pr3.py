def chatbot(response):
    '''A chatbot that reaponds using the replies it learns.
    
    >>> siri = chatbot(lambda m: print('What?!?'))
    >>> siri, hey = siri('Weather?', 'smoky')
    >>> siri, hey = siri('Globe?', 'warm')
    >>> siri, hey = siri('Vaccine?', 'not yet')
    >>> siri, hey = siri('Classes?', 'online')
    >>> hey('Classes?')
    online
    >>> hey('Weather?')
    smoky
    >>> hey('Play some Hog?')
    What?!?
    >>> hey('Vaccine?')
    not yet
    '''
    def learn(message, reply):
        def chat(m):
            if m == message:
                print(reply)
            else:
                response(m)
        return chatbot(chat),chat
    return learn
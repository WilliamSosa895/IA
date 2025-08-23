#0a
a = ""
length = len(a)

#0b
b = "it's ok"
length = len(b)

#0c
c = 'it\'s ok'
length = len(c) 

#0d
d = """hey"""
length = len(d) 

#0e
e = '\n'
length = len(e)

#1
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    print(zip_code)
    if(len(zip_code)==5 and zip_code.isdigit()): 
        return True
    else:
        return False
pass

#2
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    lista=[]
    i=0
    doc_list
    keyword=keyword.upper()
    if(len(doc_list)>0):
        for doc in doc_list:
            doc=doc.upper()
            narreglo=doc.split()
            for prueba in narreglo:
                prueba=prueba.strip(',.')
                if((prueba == keyword) and len(keyword)==len(prueba) ):
                    lista.append(i)
                    break
            i=i+1
        
            
    elif(keyword in doc_list):
        return [i]
    return lista
pass

#3
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices
pass
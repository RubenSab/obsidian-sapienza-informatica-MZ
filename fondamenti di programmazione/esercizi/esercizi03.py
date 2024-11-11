from typing import Any, Callable, List


# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')


################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che restituisce una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return f'Ciao {name} Buona giornata!'

# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    
    try:
        while string[0]==' ' and string[-1]==' ':
            if string[0]==' ':
                string = string[ 1*(string[0]==' ') : -1*(string[-1]==' ') ] 
    except:
        return string
    
    return string


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    
    separators = list(characters)
    words = []    
    word = []
    for i in string:
        if i not in separators:
            word.append(i)
        else:
            word = ''.join(word)
            if word != '':
                words.append(word)
            word = []

    return words


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    
    corrected_string = ''

    while string.find(find) != -1:
        
        string_lower_index = string.find(find)
        bounds_of_string_to_replace = [string_lower_index, string_lower_index+len(find)]
        string_first_half = string[0:bounds_of_string_to_replace[0]]
        string_second_half = string[bounds_of_string_to_replace[1]:]
        corrected_string = string_first_half + replace + string_second_half
        string = corrected_string
        
    return string

# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    
    plain_message = list(string)
    alphabet=list('abcdefghijklmnopqrstuvwxyz')
    indexes = list(range(0,len(alphabet)))
    
    if decrypt:
        shifted_indexes = [(i - offset)%26 for i in indexes]
    else:
        shifted_indexes = [(i + offset)%26 for i in indexes]
    
    alphabet_dict=dict(zip(alphabet,shifted_indexes))
    cyphered_chars = []
    
    for char_to_cypher in plain_message:
        if char_to_cypher != ' ':
            cyphered_chars.append(alphabet[alphabet_dict[char_to_cypher]]) 
        else:
            cyphered_chars.append(' ')
    
    cyphered_message = ''.join(cyphered_chars)
    return cyphered_message


# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto. Ciao Paperino', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 17, False)
print_test(caesar_cypher, 'tzrf gzggf', 17, True)

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    return sum([i**2 for i in elements])
    # oppure sum(list(map(lambda x : x**2, [1,2,3])))


# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    return sorted(elements)[-1]


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    for element_to_check in elements:
        for possible_duplicate in elements:
            if element_to_check == possible_duplicate:
                elements.pop(element_to_check)
    return elements
        


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    pass


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e restituisce una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    pass


# Test funzioni
print_test(sum_squares, [1, 2, 3])
print_test(max_element, [1, 2, 3, -1, -2])
print_test(max_element, [-1, -2])
print_test(max_element, [])
print_test(remove_duplicates, [1, 2, 3, 2, 3])
print_test(reverse_list, [1, 2, 3])
print_test(flatten_list, [1, [2, 3]])
print_test(flatten_list, [1, [2, [3, 4]]])

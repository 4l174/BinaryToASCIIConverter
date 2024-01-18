# Define uma função que converte uma string binária em um caractere ASCII
def binary_to_ascii(binary_string):
    decimal_value = int(binary_string, 2)  # Converte a string binária para um valor decimal
    ascii_character = chr(decimal_value)   # Converte o valor decimal para um caractere ASCII
    return ascii_character  # Retorna o caractere ASCII resultante

# Lê o arquivo de texto com 0's e 1's
with open('LookFindReplace.txt', 'r') as file:
    binary_data = file.read().replace('\n', '')  # Lê o conteúdo do arquivo e remove caracteres de nova linha

# Remove hífens e outros caracteres não desejados da string binária
binary_data = binary_data.replace('-', '').replace(' ', '')

# Divide a string binária em grupos de 8 bits (1 byte)
byte_strings = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

# Converte cada grupo binário em um caractere ASCII usando a função definida acima
ascii_text = ''.join([binary_to_ascii(byte) for byte in byte_strings])

# Imprime o texto ASCII resultante
print(ascii_text)

 # Tipos de Dados

print(-975)         # prints: -975
print("Infinito")   # prints: Infinito
print('Simon')      # prints: Simon
print('positivo @') # prints: positivo @
#===========================================================================

#Python usa "[]" para acessar os itens de uma sequencia.

print("Hard Times" [5]) # prints: T
print("Girafa" [0])     # prints: G
#===========================================================================

#Converter um item de dados de um tipo para outro.
#Sintaxe  --datetype(item)--

print(int("45")) # prints: 45
print(str(975))  # prints: 975
#===========================================================================

#Referencia de objeto
#Sintaxe  --referencia de objeto(Indicadores) = valor.

x = "Blue"
y = "Green"
z = x

#Saída entre parênteses separado por virgula isso significa uma Tuple(tupla) = Uma sequência ordenada e imutável de objetos.

print(x, y, z) # prints: Blue Green Blue.
z = y
print(x, y, z) # prints: Blue Green Green.
x = z
print(x, y, z) # prints: Green Green Green.
#============================================================================

#Tipagem Dinâmica (Dynamic typing).
#A função "type()" retorna os tipos de dados (também conhecidos como "classe").

centena = 100
print(centena, type(centena)) # prints: 100 <class 'int'>
centena = "North"
print(centena, type(centena)) # prints: North <class 'str'>
#=============================================================================



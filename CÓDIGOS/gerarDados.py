from random import randint
import numpy as np


number = [randint(8000000, 8000000) for i in range(0, 800000)]  # Para gerar os códigos da pasta DADOS, essa linha foi alterada conforme o arquivo INFO.
             
print(f'Números randomizados: {number}')
    
np.savetxt('nomeDoArquivo.txt', [number], fmt='%d', delimiter=', ', encoding=None) # Especifique um nome para o arquivo que será criado

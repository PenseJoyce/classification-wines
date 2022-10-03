"""
@author: Joyce
Objetivo: prever o tipo do vinho: red or white (coluna style)

"""

#carregandos os dados 

import pandas as pd 

arquivo = pd.read_csv('C:/Users/Thinc_29/Desktop/Python/Projeto - Vinho/wine_dataset.csv')


arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)


#separando as variaveis entre preditoras e variaveis alvo 
y = arquivo['style']
x = arquivo.drop('style', axis = 1) # 1 é coluna 

# ML

from sklearn.model_selection import train_test_split

# criando conjuntos de dados de treino e teste 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)



# algoritmo de machine learning
from sklearn.ensemble import ExtraTreesClassifier #arvore de decisao

# criacao do modelo, treino com 70% dos dados 
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

#imprimindo os resultados 
resultado = modelo.score(x_teste, y_teste)
print('Acurácia: ', resultado)


#gabarito
y_teste[400:403]
#dados de amostra
x_teste[400:403]
#previsao do modelo 
previsoes = modelo.predict(x_teste[400:403])

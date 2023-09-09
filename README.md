# Classificação de vinhos

Projeto de Machine Learning para identificação do tipo de vinho (Red or White) em python.

![image](https://github.com/PenseJoyce/classification-wines/assets/77034969/2e568b75-3f52-4b26-a851-bd7904053941)

## Objetivos

O script tem os seguintes objetivos:

1- Explorar os dados do dataset 'wine_quality'. 

2- Visualizar a distribuição no datasets. 

3- Classificar os vinhos que nela constam usando algorítmo de árvore de decisão.


## Bibliotecas 

Estas foram as bibliotecas utilizadas

```
pip install pandas
pip install sklearn
```

## Informações da base 

O dataset está disponível no seguinte endereço: https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009 

Esses dados são os resultados de uma análise química de vinhos cultivados na mesma região da Itália, mas derivados de três cultivares diferentes. A análise determinou as quantidades de 13 constituintes encontrados em cada um dos três tipos de vinhos.

|Caracteristicas||
|:-----|:----:|
|Características do conjunto de dados|Multivariada|
|Características do Atributo|String|
|Número de atributos|13|
|Tarefas associadas|Classificação|
|Valores ausentes|Não|

## Os atributos são:

1) fixed_acidity
2) volatile_acidity
3) citric_acid
4) residual_sugar
5) chlorides
6) free_sulfur_dioxide
7) total_sulfur_dioxide
8) density
9) pH
10) sulphates
11) alcohol
12) quality
13) style

# Introdução 

## Testes realizados 

Foi realizado teste com 1 algoritmo de Machine Learning de Classificação:
> wine.py

## Tabelas de resultados

| Algoritmo  | Best Acurácia |
|:--|:--:|
| ExtraTreesClassifier | 99.59% |


## Links

[Data Set](https://archive.ics.uci.edu/ml/datasets/Wine)  
[SkLearnf ](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

## Citações

Dua, D. e Graff, C. (2019). Repositório de aprendizado de máquina da UCI [http://archive.ics.uci.edu/ml]. Irvine, CA: Universidade da Califórnia, Escola de Informação e Ciência da Computação.

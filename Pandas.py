import pandas as pd
#criando um datagrame
data={'Alunos':['Caio','Jorge','Breno Juan','Lambisgoia','Puta','Cachorra','Safada'],
      'Idade':[16,15,14,12,13,14,17],
      'Nota':[8,9,7,5,3,2,10]}

df=pd.DataFrame(data,columns=['Alunos','Idade','Nota'])

#Algumas funções
df = df.drop([0,1])
df = df.drop('Idade',axis=1)
# Extraindo valores de um dataframe
df.describe()
df.count()
df.columns
df.shape
#Gerando dados estatísticos
df.max()
df['Nota'].max()
df.min()
df['Nota'].min()
df.mean()
df.median()
df.sum()
#Operções com pandas
df['Nota'].add(10)
df= df['Nota'].add(10)
df['Nota'].sub(3)
df['Nota'].mul(3)
df['Nota'].div(3)
Idade_Jorge = df['Idade'][1]
#Limitando Buscas no D.F.
df.head()
df.tail()
l = df.loc[df['Nota']>=6]
l.count()
#Lendo arquivos CSV e ler Excel e transorma-los em dataframe


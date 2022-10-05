#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
import matplotlib.pyplot as plt


# In[89]:


df = pd.read_excel("AdventureWorks.xlsx")


# In[90]:


df.head(5)


# In[91]:


df.shape


# In[92]:


df.info()


# In[93]:


# receita total
df["Valor Venda"].sum()


# In[94]:


# custo unitario por quantidade
df["custo"] = df["Custo Unitário"].mul(df.Quantidade)
df.head(3)


# In[95]:


# custo total
df.custo.sum()


# In[96]:


# lucro total
df["lucro"] = df["Valor Venda"] - df.custo
df.head(2)


# In[97]:


#lucro total 
df.lucro.sum()


# In[98]:


# criar coluna com o tempo de envio
df["tempo_envio"] = df["Data Envio"] - df["Data Venda"]
df.head(2)


# In[99]:


# colocar so osdoas
df["tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
df.head(2)


# In[100]:


# verificar tipo de dados do tempo de envio
df.tempo_envio.dtype


# In[101]:


# media do tempo de envio por marca
df.groupby("Marca")["tempo_envio"].mean()


# In[102]:


# valores nulos
df.isnull().sum()


# In[103]:


# lucro por ano e por marca
pd.options.display.float_format = "{:20,.2f}".format
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()


# In[104]:


# criar tabela
lucro_anual = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_anual


# In[105]:


# total de vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)


# In[106]:


# criar grafico com total de vendido
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total de produtos vendido")
plt.xlabel("Total")
plt.ylabel("Produto");


# In[107]:


# Grafico Lucro por ano
df.groupby(df["Data Venda"].dt.year,)["lucro"].sum().sort_values(ascending=True).plot.bar(title="Lucro por ano")
plt.ylabel("Lucro")
plt.xlabel("ano");


# In[108]:


#Dados do grafico
df.groupby(df["Data Venda"].dt.year,)["lucro"].sum()


# In[109]:


# Filtrar vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
df_2009.head(5)


# In[111]:


# grafico de linha com lucro por mes em 2009
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro por mes ano de 2009")
plt.xlabel("Mês")
plt.ylabel("lucro");


# In[120]:


# lucro por marca em 2009
df_2009.groupby("Marca")["lucro"].sum().plot.bar(title=" Lucro por Marca 2009")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");


# In[124]:


# lucro por classe, 2009
df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro por classe, 2009")
plt.xlabel("Classe")
plt.ylabel("lucro")
plt.xticks(rotation="horizontal");


# In[112]:


# grafico de linha com lucro por mes em 2008
df_2008 = df[df["Data Venda"].dt.year == 2008]
df_2008.groupby(df_2008["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro por mes ano de 2008")
plt.xlabel("Mês")
plt.ylabel("lucro");


# In[119]:


# lucro por marca em 2008
df_2008.groupby("Marca")["lucro"].sum().plot.bar(title=" Lucro por Marca 2008")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");


# In[125]:


# lucro por classe, 2008
df_2008.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro por classe, 2008")
plt.xlabel("Classe")
plt.ylabel("lucro")
plt.xticks(rotation="horizontal");


# In[126]:


# analise estatísticas
df.tempo_envio.describe()


# In[129]:



plt.boxplot(df.tempo_envio);


# In[132]:


# histograma
plt.hist(df.tempo_envio);


# In[133]:


# indentificar o autlier
df[df.tempo_envio == 20]


# In[134]:


df.to_csv("novo_df_venda.cvs", index=False)


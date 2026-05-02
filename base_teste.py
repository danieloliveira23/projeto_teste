import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Criando um dataset de exemplo
data = {
    'horas_estudo': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nota_exame': [100, 20, 30, 40, 50, 60, 70, 80, 90, 100],

}

df = pd.DataFrame(data)
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Configura o estilo
sns.set_theme(style="whitegrid")

# 2. Define o tamanho da figura (opcional)
plt.figure(figsize=(8, 6))

# 3. Cria o gráfico de dispersão com linha de regressão
# Vamos calcular a correlação antes para colocar no título
correlacao = df["horas_estudo"].corr(df["nota_exame"])

sns.regplot(x='horas_estudo', y='nota_exame', data=df,
            line_kws={"color": "red"},
            scatter_kws={"alpha": 0.6})

# 4. Adiciona títulos e rótulos
plt.title(f'Visualização de Correlação (Spearman: {correlacao:.2f})')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota no Exame')

# 5. Exibe o gráfico
plt.show()
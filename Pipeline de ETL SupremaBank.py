#Pipeline Suprema-BANK 

# === E do Etl ===
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Pudim@localhost/suprema_bank')

# extraindo cada tabela
print('Iniciando a extracao dos dados... tu te acalma')
df_clientes  = pd.read_sql('SELECT * FROM clientes', engine)
df_contas    = pd.read_sql('SELECT * FROM contas', engine)
df_agencias  = pd.read_sql('SELECT * FROM agencias', engine)
df_gerentes  = pd.read_sql('SELECT * FROM gerentes', engine)
df_regionais = pd.read_sql('SELECT * FROM regionais', engine)
df_transacoes = pd.read_sql('SELECT * FROM transacoes', engine)
print('Deu bom mo fi!')

# uma conferencia de desencargo de consciencia
tabelas = {
    'Clientes': df_clientes,
    'Contas': df_contas,
    'Agências': df_agencias,
    'Gerentes': df_gerentes,
    'Regionais': df_regionais,
    'Transações': df_transacoes
}

# conferindo
for nome, df in tabelas.items():
    print(f'--{nome}--')
    print(f'Linhas/Colunas:{df.shape}')
    print(df.info()) #agilizar algumas coisas
    print('-'* 15 +'\n')


# === O T do eTl ===

#Precisamos saber sobre as contas e clientes pra saber o status da conta e uma informacao demografica
df_base = pd.merge(df_contas, 
    df_clientes[['cod_cliente', 'status', 'cidade', 'estado']], 
    on='cod_cliente',
    how='left')

#Juntando com as agencias pra ter a visao geografica
df_base = pd.merge(
    df_base, 
    df_agencias[['cod_agencia', 'nome']], 
    on='cod_agencia', 
    how='left')
df_base =df_base.rename(columns={'nome':'nome_agencia'}) #tive que renomear pra na confundir!!!

#Pra pegar o cod regional
df_base = pd.merge(
    df_base, 
    df_gerentes[['cod_gerente', 'cod_regional']], 
    on='cod_gerente', 
    how='left'
)

#Uma visao de gestao misturando a base com a regional 
df_base = pd.merge(
    df_base, 
    df_regionais[['cod_regional', 'nome']], 
    on='cod_regional', 
    how='left'
)
df_base = df_base.rename(columns={'nome': 'nome_regional'})

#Tratar o campo temporal dos dados
df_base['data_abertura'] = pd.to_datetime(df_base['data_abertura'])
df_base['data_abertura'] = df_base['data_abertura'].dt.year

#Um tratamento nas colunas duplicadas que vieram os merges
remover_colunas = [
    col for col in df_base.columns
        if col.endswith('_y')
        or col.endswith('_x')
]
df_base = df_base.drop(columns=remover_colunas)
print(f'Pode ficar ssgd que base foi consolidada!! Linhas: {df_base.shape[0]}, Colunas: {df.shape[1]}\n ')

# Analise 1: Distribuição de clientes por status
print("=== RESULTADOS DAS ANÁLISES ===")
print("\n📍 Distribuição de clientes por status:")
print(df_base['status'].value_counts())

#Analise 2: saldo medio por tipo de conta e agencia
print("\n💰 Saldo médio por tipo de conta e agência (Top 5):")
saldo_medio = df_base.groupby(['nome_agencia', 'cod_tipo_conta'])['saldo_inicial'].mean().reset_index()
print(saldo_medio.head(5))

# Analise 3: Ranking de agências por volume de contas abertas
print("\n🏆 Ranking de agências por volume de contas abertas (Top 5):")
ranking_agencias = df_base['nome_agencia'].value_counts()
print(ranking_agencias.head(5))

# Analise 4: Clientes bloqueados por regional (com filtro à prova de balas)
print("\n🔒 Clientes bloqueados por regional:")
# Transformamos tudo em maiúsculo na hora de comparar pra não ter erro de digitação no banco
bloqueados = df_base[df_base['status'].str.upper() == 'BLOQUEADO'].groupby('nome_regional')['cod_cliente'].count()
print(bloqueados)

# Criando a coluna ano_abertura ANTES da Analise 5
df_base['data_abertura'] = pd.to_datetime(df_base['data_abertura'])
df_base['ano_abertura'] = df_base['data_abertura'].dt.year

# Analise 5: Crescimento de contas abertas por ano
print("\n📈 Crescimento de contas abertas por ano:")
crescimento = df_base['ano_abertura'].value_counts().sort_index()
print(crescimento)


# === o L do etL ===

print("\nGerando relatório final CSV...")
# Selecionando colunas chave pro relatório final
colunas_finais = ['cod_conta', 'cod_cliente', 'status', 'cod_tipo_conta', 
                'nome_agencia', 'nome_regional', 'saldo_inicial', 'data_abertura']
df_base[colunas_finais].to_csv('output/relatorio_final.csv', index=False)

print("🚀 Sucesso! Arquivo 'relatorio_final.csv' salvo na pasta output.")
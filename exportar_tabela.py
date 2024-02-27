import pandas as pd
import mysql.connector as sql

# Conectar ao banco de dados MySQL
conexao = sql.connect(
    host='localhost',
    user='root',
    password='senha123',
    database='analise_risco'
)

# Consulta SQL para obter todos os dados da tabela
consulta_sql ="""   select  ids.id_pessoa, ids.id_bc, ids.id_emprestimo, idade_pessoa, salario_pessoa, situacao_propriedade_pessoa, 
                            tempo_trabalhado_pessoa, foi_inadimplente_bc, tempo_primeira_solicitacao_credito_bc, motivo_emprestimo,
                            pontuacao_emprestimo, valor_emprestimo, taxa_juros_emprestimo, possibilidade_inadimplencia, 
                            porcentagem_salario_emprestimo
			        from dados_mutuarios inner join ids on dados_mutuarios.id_pessoa = ids.id_pessoa
				            inner join  historicos_banco on historicos_banco.id_bc = ids.id_bc
				            inner join emprestimos on emprestimos.id_emprestimo = ids.id_emprestimo;"""

# Ler os dados da tabela para um DataFrame do Pandas
tabela = pd.read_sql_query(consulta_sql, conexao)

# Fechar a conexão com o banco de dados
conexao.close()

# Caminho do arquivo
caminho_do_arquivo_csv = 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\dados_unidos_id.csv'

# Exportar o DataFrame para um arquivo CSV
tabela.to_csv(caminho_do_arquivo_csv, index=False)

print(f'A tabela foi exportada para {caminho_do_arquivo_csv}')

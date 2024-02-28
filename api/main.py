import pandas as pd
from fastapi import FastAPI
import joblib

app = FastAPI()
xgb = joblib.load(r"C:\Users\rodri\OneDrive\Documentos\ALURA\ANALISE DE DADOS\Alura Challenges dados 1\api\modelo_xgb.pkl")
dados = pd.read_csv(r"C:\Users\rodri\OneDrive\Documentos\ALURA\ANALISE DE DADOS\Alura Challenges dados 1\Dados\dados_inadimplencia_tratados.csv")
one_hot = joblib.load(r"C:\Users\rodri\OneDrive\Documentos\ALURA\ANALISE DE DADOS\Alura Challenges dados 1\api\modelo_onehotenc.pkl")
dados.drop("Unnamed: 0", axis =1, inplace = True)

@app.get("/predict")
def predict(idade_pessoa: int, salario_pessoa: float, situacao_propriedade_pessoa: str, tempo_trabalhado_pessoa: int,
                      motivo_emprestimo: str, pontuacao_emprestimo: str, valor_emprestimo: int, taxa_juros_emprestimo: float,
                      foi_inadimplente_bc: int):

    novo_dado = pd.DataFrame({
        "idade_pessoa" : idade_pessoa,
        "salario_pessoa" : salario_pessoa,
        "situacao_propriedade_pessoa": situacao_propriedade_pessoa,
        "tempo_trabalhado_pessoa": tempo_trabalhado_pessoa,
        "foi_inadimplente_bc": foi_inadimplente_bc,
        "motivo_emprestimo": motivo_emprestimo,
        "pontuacao_emprestimo": pontuacao_emprestimo,
        "valor_emprestimo": valor_emprestimo,
        "taxa_juros_emprestimo": taxa_juros_emprestimo,
        
    }, index = [0])
    novo_dado_one = one_hot.transform(novo_dado)
    previsao = xgb.predict(novo_dado_one)[0]
    return {"idade_pessoa" : idade_pessoa, "salario_pessoa": salario_pessoa, "situacao_propriedade_pessoa": situacao_propriedade_pessoa, "tempo_trabalhado_pessoa": tempo_trabalhado_pessoa,
                      "motivo_emprestimo": motivo_emprestimo, "pontuacao_emprestimo": pontuacao_emprestimo, "valor_emprestimo": valor_emprestimo, "taxa_juros_emprestimo": taxa_juros_emprestimo,
                      "foi_inadimplente_cb": foi_inadimplente_bc, "previsao" :int(previsao), "chance_inadimplencia":xgb.predict_proba(novo_dado_one).tolist()[0][0]}



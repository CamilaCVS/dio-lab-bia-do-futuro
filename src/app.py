import json
import pandas as pd 
import streamlit

# =========CARREGAR DADOS ==========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# =========MONTAR CONTEXTO ==========
contexto = f"""
CLIENTE:{perfil['nome']},{perfil['idade']} anos, perfil{perfil['perfil_investidor']}
OBJETIVO:{perfil['objetivo_principal']}
PATRIMONIO:R${perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos,indent=2,ensure_ascii=False)}
"""
# =========SYSTEM PROMPT ==========
SYSTEM_PROMPT = """ Você é o mIAjuda, um assistente de finanças pessoais.

OBJETIVO:
Auxiliar na reduçao de custos e consolidar a reserva de emergencia do cliente.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos, personalizando as respostas.
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Sempre pergunte se o cliente entendeu
"""

# =========CHAMAR OLLAMA ==========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta:{msg}"""
    
    r = requests.post(OLLAMA_URL,json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# =========INTERFACE ==========
st.title("mIAjuda, Seu orientador financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    st.chat_message("assistant").write(perguntar(pergunta)) 

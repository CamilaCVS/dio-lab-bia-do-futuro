# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Como o mIAjuda vai utilizar |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Conhecendo o cliente para atender com maior precisão|
| `perfil_investidor.json` | JSON | Verificar a frequencia em que o cliente faz algum investimento |
| `transacoes.csv` | CSV | Analisar padrão de consumo do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Retirei os produtos financeiros, pois a aplicação não recomendará nenhuma carteira de investimento ao cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados no prompt(Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:
```python
import pandas as pd
import json

#CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

#JSONs
with open('data/perfil_investidor.json', 'r', encoding = 'utf-8') as f:
    perfil = json.load(f)
```
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
Para simplificar, podemos simplesmente"injetar" os dados em nosso prompt, garantindo que o agente tenha o melhor contexto posssível. Lembrando que, em soluções mais robustas, o idel é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade.
  
```text
PERFIL E DADOS DO CLIENTE (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

HISTORICO DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

TRANSACOES DO CLIENTE(data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto anotado abaixo, se baseia nos dados originais da base de conhecimento, mas sintetiza deixando apenas os dados mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Consolidar reserva de emergencia
- Renda mensal: R$ 5.000

Últimas transações:
- Aluguel: R$1.200
- Supermercado:R$ 450
- Streaming:R$ 55,90
- Farmácia:R$ 89
- Restaurante:R$ 120
- Uber:R$ 45
- Conta de Luz: R$ 180
- Academia: R$ 99
- Combustível: R$ 250
- Total de saida: R$ 2488,90
```

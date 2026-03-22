# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e atender com maior precisão|
| `perfil_investidor.json` | JSON | Verificar a frequencia em que o cliente faz algum investimento |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Retirei os produtos financeiros, pois a aplicação não recomendará nanhuma carteira de investimento ao cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados no prompt(Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:
'''python
import pandas as pd
import json

#CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = ps.read_csv('data/transacoes.csv')

#JSONs
with open('data/perfil_investidor.jason', 'r', encoding = 'utf-8') as f:
    perfil = json.load(f)
'''
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```

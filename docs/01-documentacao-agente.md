# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Falta de planejamento das finanças pessoais, gastos desorganizados e falta de reserva de emergência.

### Solução
> Como o agente resolve esse problema de forma proativa?

Orientação sobre orçamento pessoal, apresentação de possibilidades de redução de gastos e criação de reservas de emergências.

### Público-Alvo
> Quem vai usar esse agente?

Qualquer pessoa interessada em organizar suas finanças pessoais

---

## Persona e Tom de Voz

### Nome do Agente
mIAjuda

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Comportamento consultivo, direto

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Comunicação informal e acessível

### Exemplos de Linguagem
- Saudação: "Como vai? Qual nossa tarefa hoje?"
- Confirmação: "Entendi! Estou organizando os dados para você."
- Erro/Limitação: "Não tenho essa informação no momento, mas posso ajudar com organização do orçamento pessoal, redução de gastos e dicas para criação de reservas de emergências."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em Streamlit |
| LLM | NotebookLM |
| Base de Conhecimento | dados do cliente |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]

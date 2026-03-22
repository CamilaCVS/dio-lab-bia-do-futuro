## Passo a passo de Execução

## Setup do Ollama

```bash
#1. Instalar Ollama(ollama.com)
#2. Baixar um modelo leve
ollama pull gpt-oss

#Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo
Todo o código-fonte está no arquivo `app.py`.

```

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
Ollama serve
Rodar a aplicação

# 3. Rodar o app
streamlit run .\src\app.py
```

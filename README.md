
# Controle Financeiro (CLI)

Aplicação de terminal em Python para registrar receitas e despesas,
consultar o saldo e listar movimentações, com dados salvos em JSON.

## Funcionalidades
- Cadastro de receitas e despesas com categorias específicas para cada tipo
- Cálculo de saldo com alertas (negativo, zerado, positivo)
- Listagem de movimentações
- Persistência em arquivo JSON

## Como executar
Requer Python 3.10 ou superior.

```bash
python Controle_Financeiro.py
```

## Testes
```bash
pip install pytest
pytest
```

## Estrutura
- `Controle_Financeiro.py`: lógica e menu
- `test_financeiro.py`: testes automatizados

## Decisões e aprendizados
- Separei a lógica (cálculo, persistência) da interface (menu) para facilitar os testes.
- Usei uma lista única de dicionários em vez de listas separadas, para evitar inconsistência.
- Categorias diferentes para receita e despesa, em uma constante CATEGORIAS, de modo que adicionar categoria vira editar um dicionário.

## Persistência em JSON
Salvo as movimentações em `movimentacoes.json` para os dados não sumirem ao fechar o programa. Escolhi JSON porque cada movimentação já é um dicionário, então `json.dump` e `json.load` salvam e carregam a lista sem conversão, e o arquivo continua legível. O arquivo fica no `.gitignore` por conter dados pessoais.  

## Próximos passos
- Data em cada movimentação, edição/exclusão, relatório por categoria

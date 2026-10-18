
import json
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).with_name('movimentacoes.json')

CATEGORIAS = {
    'receita': {
        '1': 'Salário',
        '2': 'Freelance',
        '3': 'Investimento',
        '4': 'Presente',
        '5': 'Outros',
    },
    'despesa': {
        '1': 'Aluguel',
        '2': 'Compras',
        '3': 'Transporte',
        '4': 'Saúde',
        '5': 'Educação',
        '6': 'Lazer',
        '7': 'Outros',
    },
}


def carregar_movimentacoes() -> list:
    """Lê as movimentações salvas. Retorna lista vazia se não houver arquivo."""
    if not ARQUIVO_DADOS.exists():
        return []
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        print('Aviso: não foi possível ler o arquivo de dados. Iniciando vazio.')
        return []


def salvar_movimentacoes(movimentacoes: list) -> None:
    """Grava a lista de movimentações no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(movimentacoes, arquivo, ensure_ascii=False, indent=4)

# Try para que o usuário insira um valor válido, caso contrário, ele será solicitado a inserir novamente.


def obter_valor(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")


def escolher_categoria(tipo: str) -> str | None:
    """Mostra as categorias do tipo e retorna o nome da escolhida, ou None se inválida."""
    opcoes = CATEGORIAS[tipo]

    print('=' * 30)
    print(f'CATEGORIAS DE {tipo.upper()}:')
    for chave, nome in opcoes.items():
        print(f'{chave} - {nome}')
    print('=' * 30)

    chave = input(f'Escolha a categoria da {tipo}: ').strip()
    return opcoes.get(chave)


def cadastrar_movimentacao(tipo: str, movimentacoes: list) -> None:
    """Cadastra uma receita ou despesa. O tipo é 'receita' ou 'despesa'."""
    valor = obter_valor(f'Insira o valor da {tipo}: ')
    categoria = escolher_categoria(tipo)

    if categoria is None:
        print(f'Categoria inválida. {tipo.capitalize()} não cadastrada.')
        return

    movimentacoes.append(
        {'tipo': tipo, 'valor': valor, 'categoria': categoria})
    print(f'{tipo.capitalize()} de R${valor:.2f} cadastrada com sucesso!')
    print(f'{tipo.capitalize()} categorizada como: {categoria}')


def calcular_saldo(movimentacoes: list) -> float:
    receitas = sum(m['valor'] for m in movimentacoes if m['tipo'] == 'receita')
    despesas = sum(m['valor'] for m in movimentacoes if m['tipo'] == 'despesa')
    return receitas - despesas


def listar_por_tipo(movimentacoes: list, tipo: str, sinal: str) -> None:
    for m in movimentacoes:
        if m['tipo'] == tipo:
            print(f"  {sinal} R${m['valor']:.2f} ({m['categoria']})")


def controle_financeiro():
    movimentacoes = carregar_movimentacoes()

    operacoes = {
        '1': 'Cadastrar Receita',
        '2': 'Cadastrar Despesa',
        '3': 'Visualizar Saldo',
        '4': 'Listar movimentações',
        '5': 'Sair'
    }

    # Loop principal do controle financeiro, onde o usuário escolhe a operação desejada.
    while True:
        print('\n' + '=' * 30)
        print('CONTROLE FINANCEIRO')
        for chave, valor in operacoes.items():
            print(f'{chave} - {valor}')
        print('=' * 30)

        opcao = input('Escolha a operação: ').strip()

        if opcao not in operacoes:
            print('Operação inválida. Tente novamente.')
            continue

        if opcao == '1':
            cadastrar_movimentacao('receita', movimentacoes)
            salvar_movimentacoes(movimentacoes)

        elif opcao == '2':
            cadastrar_movimentacao('despesa', movimentacoes)
            salvar_movimentacoes(movimentacoes)

        elif opcao == '3':
            saldo = calcular_saldo(movimentacoes)
            print(f'Saldo atual: R${saldo:.2f}')
            if saldo < 0:
                print('Atenção: Você está com saldo negativo!')
            elif saldo == 0:
                print('Atenção: Seu saldo está zerado!')
            else:
                print('Saldo positivo. Continue assim!')

        elif opcao == '4':
            print('Listando movimentações...')
            print('Receitas:')
            listar_por_tipo(movimentacoes, 'receita', '+')
            print('Despesas:')
            listar_por_tipo(movimentacoes, 'despesa', '-')

        elif opcao == '5':
            print('Saindo do controle financeiro. Até logo!')
            break


if __name__ == "__main__":
    controle_financeiro()

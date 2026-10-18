
import pytest

import Controle_Financeiro
from Controle_Financeiro import calcular_saldo


def test_saldo_com_receita_e_despesa():
    movimentacoes = [
        {'tipo': 'receita', 'valor': 1000.0, 'categoria': 'Salário'},
        {'tipo': 'despesa', 'valor': 300.0, 'categoria': 'Lazer'},
    ]
    assert calcular_saldo(movimentacoes) == 700.0


def test_saldo_lista_vazia():
    assert calcular_saldo([]) == 0


def test_saldo_negativo():
    movimentacoes = [{'tipo': 'despesa', 'valor': 50.0, 'categoria': 'Compras'}]
    assert calcular_saldo(movimentacoes) == -50.0


def test_float_nao_e_exato():
    assert 0.1 + 0.2 != 0.3                    
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_salvar_e_carregar(tmp_path, monkeypatch):
    arquivo_teste = tmp_path / 'dados.json'
    monkeypatch.setattr(Controle_Financeiro, 'ARQUIVO_DADOS', arquivo_teste)

    dados = [{'tipo': 'receita', 'valor': 50.0, 'categoria': 'Freelance'}]
    Controle_Financeiro.salvar_movimentacoes(dados)

    assert Controle_Financeiro.carregar_movimentacoes() == dados


def test_carregar_sem_arquivo(tmp_path, monkeypatch):
    monkeypatch.setattr(Controle_Financeiro, 'ARQUIVO_DADOS', tmp_path / 'nao_existe.json')
    assert Controle_Financeiro.carregar_movimentacoes() == []

def test_categoria_invalida_nao_registra(monkeypatch):
    movimentacoes = []
    respostas = iter(['100', '99'])  # 1º input: valor, 2º input: categoria inexistente
    monkeypatch.setattr('builtins.input', lambda _: next(respostas))

    Controle_Financeiro.cadastrar_movimentacao('receita', movimentacoes)

    assert movimentacoes == []


def test_categoria_valida_registra(monkeypatch):
    movimentacoes = []
    respostas = iter(['100', '1'])  # valor 100, categoria 1 (Salário)
    monkeypatch.setattr('builtins.input', lambda _: next(respostas))

    Controle_Financeiro.cadastrar_movimentacao('receita', movimentacoes)

    assert movimentacoes == [{'tipo': 'receita', 'valor': 100.0, 'categoria': 'Salário'}]
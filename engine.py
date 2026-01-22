"""
Motor principal da aplicação.

Responsabilidades:
- Carregar perguntas, objeções e respostas
- Controlar navegação na árvore (IDs)
- Aplicar score
- Interpretar comandos globais (0, 9, 10)
- Encerrar corretamente
"""

from estado import Estado
from persistencia import Logger
from perguntas import PERGUNTAS
from objecoes import OBJECOES
from respostas import RESPOSTAS
import os


def iniciar_app():
    estado = Estado()
    logger = Logger(estado)

    while estado.ativo:
        os.system("clear")
        estado.exibir_cabecalho()
        estado.exibir_no_atual(PERGUNTAS, OBJECOES)
        entrada = input("\nEscolha: ").strip()

        # Comandos globais
        if entrada == "10":
            logger.salvar_saida("SALVAR E SAIR")
            break

        if entrada == "9":
            nota = input("Observação: ")
            logger.salvar_observacao(nota)
            continue

        if entrada == "0":
            estado.voltar()
            continue

        estado.processar_resposta(entrada, RESPOSTAS, logger)

    logger.finalizar()

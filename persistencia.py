"""
Responsável por salvar tudo em TXT.
"""

from datetime import datetime

class Logger:
    def __init__(self, estado):
        nome = estado.cliente.replace(" ", "_").lower()
        self.arquivo = f"venda_{nome}.txt"
        self.salvar("INÍCIO DA CONVERSA")

    def salvar(self, texto):
        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] {texto}\n")

    def salvar_passagem(self, no, escolha, resposta, score):
        self.salvar(
            f"NÓ: {no} | Escolha: {escolha} | Peso: {resposta['peso']} | Score: {round(score,2)}"
        )

    def salvar_observacao(self, texto):
        self.salvar(f"OBSERVAÇÃO: {texto}")

    def salvar_saida(self, motivo):
        self.salvar(f"SAÍDA: {motivo}")

    def finalizar(self):
        self.salvar("FIM DA CONVERSA")

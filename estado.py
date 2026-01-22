"""
Controla o estado atual da conversa:
- cliente
- perfil
- score
- nó atual
- histórico (pilha para voltar)
"""

class Estado:
    def __init__(self):
        self.cliente = input("Nome do cliente: ")
        self.perfil = self.definir_perfil()
        self.score = 0.0
        self.no_atual = "Q001"
        self.historico = []
        self.ativo = True

    def definir_perfil(self):
        print("Perfil do cliente:")
        print("1 - Defensivo (Mitnick)")
        print("2 - Lógico (Jordan Belfort)")
        print("3 - Ambos")
        while True:
            escolha = input("Escolha: ")
            if escolha == "1":
                return "DEFENSIVO"
            if escolha == "2":
                return "LOGICO"
            if escolha == "3":
                return "AMBOS"

    def exibir_cabecalho(self):
        print("=" * 60)
        print(f"Cliente: {self.cliente}")
        print(f"Perfil: {self.perfil}")
        print(f"Score: {round(self.score, 2)}")
        print(f"Nó atual: {self.no_atual}")
        print("=" * 60)

    def exibir_no_atual(self, perguntas, objecoes):
        base = perguntas if self.no_atual.startswith("Q") else objecoes
        no = base[self.no_atual]

        print(f"\n❓ {no['texto']}\n")
        for k, v in no["opcoes"].items():
            print(f"{k} - {v['texto']}")

        print("\n0 - Voltar | 9 - Observação | 10 - Salvar e sair")

    def voltar(self):
        if self.historico:
            self.no_atual = self.historico.pop()

    def processar_resposta(self, entrada, respostas, logger):
        base = respostas.get(self.no_atual, {})
        if entrada not in base:
            return

        resposta = base[entrada]
        self.historico.append(self.no_atual)
        self.no_atual = resposta["destino"]
        self.score += resposta["peso"]

        logger.salvar_passagem(self.no_atual, entrada, resposta, self.score)

        if self.no_atual.startswith("E"):
            self.ativo = False

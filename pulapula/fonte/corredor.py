from src.crianca import Crianca
from src.pula_pula import PulaPula

if __name__ == '__main__':
    #Inicializando o pulapula
    pulaPula = PulaPula(5)
    print(pulaPula)

    #Entrando na fila de espera
    crianca_mario = Crianca("mario", 5)
    pulaPula.entrarNaFila(crianca_mario)

    crianca_ana = Crianca("ana", 4)
    pulaPula.entrarNaFila(crianca_ana)

    crianca_diego = Crianca("diego", 3)
    pulaPula.entrarNaFila(crianca_diego)

    print(pulaPula)

    # Entrando no pulapula
    pulaPula.entrar()
    pulaPula.entrar()
    print(pulaPula)

    #Saindo e entrando novamente no pulapula
    pulaPula.sair()
    pulaPula.entrar()
    pulaPula.entrar()
    print(pulaPula)

    #Papai chegou e pagou a conta
    pulaPula.papaiChegou("mario")
    pulaPula.sair()
    print(pulaPula)

    if pulaPula.papaiChegou("pedro") is False:
        print("fail: não há nenhuma criança com esse nome na fila ou pulapula")

    pulaPula.papaiChegou("ana")
    print(pulaPula)

    #Fechar o pulapula
    crianca_luiza = Crianca("luiza", 8)
    pulaPula.entrarNaFila()
    pulaPula.sair()
    pulaPula.entrar()
    print(pulaPula)

    print(pulaPula.fechar())
    print(pulaPula)
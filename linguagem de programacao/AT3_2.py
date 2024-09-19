class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def ligar_desligar(self):
        self.ligada = not self.ligada

    def mudar_canal_cima(self):
        if self.ligada:
            self.canal += 1

    def mudar_canal_baixo(self):
        if self.ligada:
            self.canal -= 1


tv = Televisao()
print(tv.ligada)
tv.ligar_desligar()
print(tv.ligada)
print(tv.canal)
tv.mudar_canal_baixo()
print(tv.canal)
tv.mudar_canal_cima()
print(tv.canal)
tv.ligar_desligar()
print(tv.ligada)

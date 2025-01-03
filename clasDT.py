class Horario: 
    def __init__(self,hora, minu, seg):

        self.h = hora
        self.m = minu 
        self.s = seg
    
    def __repr__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __str__(self):
        return f" O horário é: {self.h:02d}:{self.m:02d}:{self.s:02d}"

agora = Horario(7, 8, 18)

print(agora)


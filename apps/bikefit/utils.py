from .models import ModelCalculos
from datetime import datetime


class CalculaBikeFit:
    def __init__(self, cavalo, esterno, braco, data, email=None):
        self._cavalo = float(cavalo)
        self._esterno = float(esterno)
        self._braco = float(braco)
        self._data = data
        self._email = email

    @property
    def tronco(self) -> float:
        return self._esterno - self._cavalo

    @property
    def quadro_speed(self) -> float:
        return self._cavalo * 0.67

    @property
    def quadro_mtb(self) -> float:
        return (self._cavalo * 0.67 - 10) * 0.393700787

    @property
    def altura_selim(self) -> float:
        return self._cavalo * 0.883

    @property
    def top_tube_efetivo(self) -> float:
        return ((self._esterno - self._cavalo + self._braco) / 2) + 4

    @property
    def dados(self) -> dict:
        return dict(
            cavalo=self._cavalo,
            esterno=self._esterno,
            braco=self._braco,
            data=self._data,
            email=self._email,
        )

    @property
    def calculos(self) -> dict:
        return dict(
            tronco=self.tronco,
            quadro_speed=self.quadro_speed,
            quadro_mtb=self.quadro_mtb,
            altura_selim=self.altura_selim,
            top_tube_efetivo=self.top_tube_efetivo,
        )

    @staticmethod
    def quantidade_de_calculos_do_dia():
        return len(
            ModelCalculos.objects.filter(
                data__icontains=datetime.today().strftime("%Y-%m-%d")
            )
        )

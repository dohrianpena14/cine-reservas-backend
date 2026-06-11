import reflex as rx


class ReservaState(rx.State):
    asiento_seleccionado: str = ""
    horario: str = ""
    boletos: str = ""
    mensaje: str = ""

    def seleccionar_asiento(self, asiento: str):
        self.asiento_seleccionado = asiento
        self.mensaje = f"Asiento seleccionado: {asiento}"

    def set_horario(self, horario: str):
        self.horario = horario

    def set_boletos(self, boletos: str):
        self.boletos = boletos

    def validar_reserva(self):
        if self.asiento_seleccionado == "":
            self.mensaje = "Selecciona un asiento"
            return

        if self.horario == "":
            self.mensaje = "Selecciona un horario"
            return

        if self.boletos == "":
            self.mensaje = "Selecciona la cantidad de boletos"
            return

        self.mensaje = (
            f"Reserva lista: asiento {self.asiento_seleccionado}, "
            f"horario {self.horario}, "
            f"{self.boletos} boleto(s)"
        )
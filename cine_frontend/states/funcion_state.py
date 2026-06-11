import reflex as rx
import requests
from typing import Any


API_URL = "https://tainted-posing-phrase.ngrok-free.dev"


class FuncionState(rx.State):
    funciones: list[dict[str, Any]] = []

    def cargar_funciones(self):
        try:
            response = requests.get(f"{API_URL}/funciones")

            if response.status_code == 200:
                self.funciones = response.json()

        except Exception as e:
            print(e)
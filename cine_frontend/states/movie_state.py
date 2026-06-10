import reflex as rx
import requests
from typing import Any


class MovieState(rx.State):

    peliculas: list[dict[str, Any]] = []

    def cargar_peliculas(self):
        try:
            response = requests.get(
                "https://tainted-posing-phrase.ngrok-free.dev/peliculas"
            )

            if response.status_code == 200:
                self.peliculas = response.json()

        except Exception as e:
            print(e)
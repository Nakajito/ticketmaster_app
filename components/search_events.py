import reflex as rx
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TICKETMASTER_API_KEY")


def search_events(self):
    self.is_loading = True
    self.error_message = ""
    self.events = []
    yield

    try:
        url = "https://app.ticketmaster.com/discovery/v2/events.json"

        params = {
            "apikey": API_KEY,
            "size": 12,  # 12 resutlados por página para que cargue rápido
            "page": self.page,  # <--- LE DECIMOS A LA API QUÉ PÁGINA QUEREMOS
            "sort": "date,asc",
            "countryCode": "MX",
        }

        if self.search_query.strip():
            params["keyword"] = self.search_query

        # Solo enviamos el parámetro 'city' si:
        # 1. Hay algo seleccionado.
        # 2. Y LO QUE SELECCIONARON NO ES "Todas las ciudades"
        if self.city_filter.strip() and self.city_filter != "Todas las ciudades":
            params["city"] = self.city_filter

        if self.category_filter and self.category_filter != "Todas":
            params["classificationName"] = self.category_filter

        # Debug para verificar
        # print(f"Enviando params: {params}")

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "_embedded" in data and "events" in data["_embedded"]:
            raw_events = data["_embedded"]["events"]
            self.events = self._process_events(raw_events)
        else:
            self.error_message = "No se encontraron eventos con esos filtros."

    except Exception as e:
        self.error_message = f"Error: {str(e)}"
    finally:
        self.is_loading = False

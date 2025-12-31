import reflex as rx

"""Llamar a esta función desde el botón BUSCAR en lugar de search_events directo"""


def start_new_search(self):
    self.page = 0  # Reseteamos a la primera página
    return self.search_events()

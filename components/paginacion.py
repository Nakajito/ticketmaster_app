import reflex as rx


def next_page(self):
    """Avanza a la siguiente página"""
    self.page += 1
    return self.search_events()


def prev_page(self):
    """Regresa a la página anterior"""
    if self.page > 0:
        self.page -= 1
        return self.search_events()

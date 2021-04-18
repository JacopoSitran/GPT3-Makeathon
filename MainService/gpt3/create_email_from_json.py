def create_email_response(orders):
    return 'Sehrgeehrte Kundin / Kunde\n\n' + '\n\n'.join([summarize(order) for order in orders] + ['Vielen dank'])

def summarize(order):
    resp = [
    f'Die Bestellung mit Ordnungsnummer {order.po} hat jetzt folgende Positionen: {order.positions}.']
    if "elk" in order.categories:
        resp.append('Endlieferung wurde gesetzt.')
    if "erk" in order.categories:
        resp.append('Endrechnung wurde gesetzt.')
    resp.append('Die Bestellung ist immer noch offen.' if order.is_open else 'Bestellung ist jetzt geschlossen.')

    return '\n'.join(resp)

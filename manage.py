#!/usr/bin/env python
"""
Utility da riga di comando per le attività amministrative di Boraso Gattini Cafe.
Sviluppato per la gestione del sistema backend e database.
"""
import os
import sys


def main():
    """Esecuzione delle attività amministrative."""
    # Sostituito 'CREAZZO_GattiniCafe.settings' con il tuo nuovo percorso
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Boraso_gattini_caffe.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossibile importare Django. Assicurati che sia installato e "
            "disponibile nel tuo PYTHONPATH. Hai attivato il virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
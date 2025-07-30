# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
import asyncore
from smtpd import SMTPServer
import threading

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  📧 Attrape-Mail v{VERSION}                                  ║
║                                                              ║
║  Serveur SMTP local pour capturer et afficher les e-mails.  ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

class MailCaptureServer(SMTPServer):
    """Un serveur SMTP qui imprime les e-mails reçus sur la console."""
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print("\n\n--- NOUVEL E-MAIL REÇU ---")
        print(f"De: {mailfrom}")
        print(f"Pour: {', '.join(rcpttos)}")
        print("--- Contenu de l'e-mail ---")
        try:
            # Tente de décoder en UTF-8, sinon affiche en brut
            print(data.decode('utf-8'))
        except UnicodeDecodeError:
            print(data)
        print("--- FIN DE L'E-MAIL ---\n")

def run_server(host, port):
    """Lance le serveur SMTP dans un thread séparé."""
    print(f"[*] Démarrage du serveur SMTP sur {host}:{port}")
    print("[*] En attente d'e-mails... (Appuyez sur Ctrl+C pour arrêter)")
    server = MailCaptureServer((host, port), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print("\n[*] Arrêt du serveur SMTP.")

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Lance un serveur SMTP local pour capturer tous les e-mails entrants.",
        epilog=f"Créé par ozGod."
    )
    parser.add_argument("-H", "--host", default="127.0.0.1", help="L'adresse IP sur laquelle écouter (par défaut: 127.0.0.1).")
    parser.add_argument("-p", "--port", type=int, default=1025, help="Le port sur lequel écouter (par défaut: 1025).")

    args = parser.parse_args()

    run_server(args.host, args.port)

if __name__ == "__main__":
    main()

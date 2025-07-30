# 📧 Attrape-Mail - Serveur SMTP de Capture

**Créé par ozGod-sh**

## Description

Attrape-Mail est un serveur SMTP local conçu pour capturer et afficher tous les e-mails entrants. Idéal pour les tests de développement, l'analyse de phishing et l'interception de communications lors d'audits de sécurité.

## Fonctionnalités

### 📨 Capture d'e-mails
- **Serveur SMTP complet** : Accepte toutes les connexions SMTP
- **Affichage en temps réel** : Montre immédiatement les e-mails reçus
- **Support multi-destinataires** : Gère plusieurs destinataires par e-mail
- **Décodage automatique** : Tente le décodage UTF-8, sinon affiche en brut

### 🔧 Configuration flexible
- **Host personnalisable** : Écoute sur n'importe quelle interface
- **Port configurable** : Par défaut 1025 (non-privilégié)
- **Arrêt propre** : Ctrl+C pour arrêter le serveur

## Installation

### Prérequis
- Python 3.6+
- Aucune dépendance externe (utilise la bibliothèque standard)

### Installation
```bash
cd Attrape-Mail
# Aucune installation requise - utilise uniquement la stdlib Python
```

## Utilisation

### Syntaxe de base
```bash
python attrape_mail.py [OPTIONS]
```

### Options disponibles
- `-H, --host HOST` : Adresse IP d'écoute (défaut: 127.0.0.1)
- `-p, --port PORT` : Port d'écoute (défaut: 1025)
- `-h, --help` : Affiche l'aide

### Exemples d'utilisation

#### 1. Serveur local basique
```bash
python attrape_mail.py
```

#### 2. Écoute sur toutes les interfaces
```bash
python attrape_mail.py --host 0.0.0.0
```

#### 3. Port personnalisé
```bash
python attrape_mail.py --port 2525
```

#### 4. Configuration complète
```bash
python attrape_mail.py -H 192.168.1.100 -p 587
```

## Structure des fichiers

```
Attrape-Mail/
├── attrape_mail.py     # Script principal
└── README.md          # Cette documentation
```

## Logique de fonctionnement

### 1. Serveur SMTP personnalisé
```python
class MailCaptureServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        # Traite chaque e-mail reçu
```

### 2. Gestion des connexions
- **Accepte toutes les connexions** : Pas d'authentification requise
- **Traitement asynchrone** : Utilise `asyncore.loop()`
- **Gestion des erreurs** : Continue même en cas d'e-mail malformé

### 3. Affichage formaté
```python
print(f"De: {mailfrom}")
print(f"Pour: {', '.join(rcpttos)}")
print("--- Contenu de l'e-mail ---")
```

## Cas d'usage

### Développement web
- **Tests d'applications** : Vérifier l'envoi d'e-mails sans spam
- **Debug de formulaires** : Capturer les e-mails de contact
- **Tests d'inscription** : Intercepter les e-mails de confirmation

### Tests de sécurité
- **Analyse de phishing** : Capturer les e-mails malveillants
- **Tests d'injection** : Vérifier les tentatives d'injection SMTP
- **Audit de serveurs mail** : Analyser le trafic SMTP

### Formation et démonstration
- **Ateliers de sécurité** : Démontrer les attaques par e-mail
- **Tests pédagogiques** : Environnement sûr pour apprendre
- **Simulations** : Reproduire des scénarios d'attaque

## Exemple de sortie

```
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  📧 Attrape-Mail v1.0.0                                  ║
║                                                              ║
║  Serveur SMTP local pour capturer et afficher les e-mails.  ║
║  Créé par ozGod                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝

[*] Démarrage du serveur SMTP sur 127.0.0.1:1025
[*] En attente d'e-mails... (Appuyez sur Ctrl+C pour arrêter)


--- NOUVEL E-MAIL REÇU ---
De: test@example.com
Pour: admin@localhost, user@localhost
--- Contenu de l'e-mail ---
Subject: Test d'e-mail
From: test@example.com
To: admin@localhost

Ceci est un e-mail de test capturé par Attrape-Mail.
--- FIN DE L'E-MAIL ---
```

## Configuration des clients mail

### Paramètres SMTP
- **Serveur** : 127.0.0.1 (ou l'IP configurée)
- **Port** : 1025 (ou le port configuré)
- **Sécurité** : Aucune (pas de TLS/SSL)
- **Authentification** : Aucune

### Exemple avec Python smtplib
```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Message de test")
msg['Subject'] = "Test Attrape-Mail"
msg['From'] = "test@example.com"
msg['To'] = "admin@localhost"

server = smtplib.SMTP('127.0.0.1', 1025)
server.send_message(msg)
server.quit()
```

### Exemple avec curl
```bash
curl --mail-from test@example.com \
     --mail-rcpt admin@localhost \
     --upload-file email.txt \
     smtp://127.0.0.1:1025
```

## Sécurité et limitations

### ⚠️ Avertissements de sécurité
- **Pas de chiffrement** : Tous les e-mails sont en clair
- **Pas d'authentification** : Accepte tous les expéditeurs
- **Logs visibles** : Tous les e-mails sont affichés en console
- **Usage local uniquement** : Ne pas exposer sur Internet

### Limitations techniques
- **Pas de stockage** : Les e-mails ne sont pas sauvegardés
- **Pas de relais** : Ne retransmet pas les e-mails
- **Décodage basique** : Peut avoir des problèmes avec certains encodages
- **Un seul thread** : Traite les e-mails séquentiellement

## Intégration avec d'autres outils

### Avec des frameworks web
```python
# Configuration Django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 1025
```

### Avec des outils de test
```bash
# Lancer le serveur en arrière-plan
python attrape_mail.py &
# Exécuter les tests
pytest tests/
# Arrêter le serveur
kill %1
```

## Dépannage

### Port déjà utilisé
```bash
# Vérifier les ports utilisés
netstat -an | grep 1025
# Utiliser un autre port
python attrape_mail.py --port 2525
```

### Permissions insuffisantes
```bash
# Les ports < 1024 nécessitent des privilèges root sur Unix
sudo python attrape_mail.py --port 25
```

## Améliorations futures

- Sauvegarde des e-mails en fichiers
- Interface web pour visualiser les e-mails
- Support TLS/SSL optionnel
- Filtrage par expéditeur/destinataire
- Export en formats standards (mbox, eml)

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Attrape-Mail v1.0.0** | Créé par ozGod-sh
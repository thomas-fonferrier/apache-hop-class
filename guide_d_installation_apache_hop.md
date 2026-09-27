# 🚀 Guide de Lancement d'Apache Hop

Ce document explique comment démarrer l'interface graphique d'Apache Hop (Hop GUI) en partant du principe que les fichiers sont déjà téléchargés et que votre terminal est actuellement ouvert dans le dossier `apache-hop-class`.

## ⚠️ Prérequis : Java

Apache Hop nécessite Java (version 11 ou 17 recommandée) pour fonctionner.
Vérifiez que Java est bien actif sur votre système en tapant cette commande :
```bash
java -version
```
*(Si cela retourne une erreur, vous devez installer Java avant de continuer).*

---

## 💻 Commandes de lancement

Choisissez la section correspondant à votre système d'exploitation. Assurez-vous que votre terminal ou invite de commandes est bien positionné dans le répertoire `apache-hop-class`.

### 🐧 Linux et 🍏 macOS

Sur les systèmes Unix, il faut s'assurer que les scripts ont les permissions nécessaires pour être exécutés avant de lancer l'application.

Copiez-collez les commandes suivantes dans votre terminal :

```bash
# 1. Entrer dans le sous-dossier "hop"
cd hop

# 2. Donner les droits d'exécution à tous les scripts shell
chmod +x *.sh

# 3. Lancer l'interface de développement (Hop GUI)
./hop-gui.sh
```

### 🪟 Windows

Sur Windows, vous n'avez pas besoin de gérer les droits d'exécution. Vous pouvez lancer le programme en ligne de commande ou visuellement.

**Option A : En ligne de commande (PowerShell / CMD)**
Copiez-collez ces commandes :

```powershell
# 1. Entrer dans le sous-dossier "hop"
cd hop

# 2. Lancer l'interface de développement (Hop GUI)
.\hop-gui.bat
```

**Option B : Via l'Explorateur de fichiers (Mode visuel)**
1. Depuis le dossier `apache-hop-class`, ouvrez le sous-dossier `hop`.
2. Repérez le fichier nommé `hop-gui.bat` et double-cliquez dessus.

---

## 🛠️ Dépannage rapide

* **L'interface ne s'ouvre pas ou se referme immédiatement (Windows) :** Cela indique généralement que Java n'est pas installé ou que votre variable d'environnement système `JAVA_HOME` n'est pas correctement configurée pour pointer vers votre installation Java.
* **Erreur "Permission denied" (Linux/Mac) :** Vous avez probablement sauté l'étape `chmod +x *.sh`.
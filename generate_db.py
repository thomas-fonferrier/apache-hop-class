import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

fake = Faker("fr_FR")
random.seed(42)
Faker.seed(42)

N_CLIENTS = 2000
N_PRODUITS = 100
N_COMMANDES = 15000

# -------------------------
# CLIENTS
# -------------------------

clients = []

villes = [
    "Lyon",
    "Paris",
    "Marseille",
    "Toulouse",
    "Bordeaux",
    "Nantes",
    "Lille",
    "Strasbourg",
    "Nice",
    "Montpellier",
]

for i in range(1, N_CLIENTS + 1):
    clients.append({
        "client_id": i,
        "nom": fake.name(),
        "email": fake.email(),
        "ville": random.choice(villes),
        "date_inscription": fake.date_between(
            start_date="-3y",
            end_date="today"
        )
    })

clients = pd.DataFrame(clients)


# -------------------------
# PRODUITS
# -------------------------

categories = [
    "Informatique",
    "Téléphonie",
    "Maison",
    "Sport",
    "Mode",
]

produits = []

for i in range(1, N_PRODUITS + 1):
    produits.append({
        "produit_id": i,
        "produit": fake.word().capitalize(),
        "categorie": random.choice(categories),
        "prix": round(random.uniform(10, 1500), 2)
    })

produits = pd.DataFrame(produits)


# -------------------------
# COMMANDES
# -------------------------

commandes = []

start_date = datetime.now() - timedelta(days=365)

for i in range(1, N_COMMANDES + 1):

    date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    commandes.append({
        "commande_id": i,
        "client_id": random.randint(1, N_CLIENTS),
        "produit_id": random.randint(1, N_PRODUITS),
        "date": date.strftime("%Y-%m-%d"),
        "quantite": random.randint(1, 5)
    })

commandes = pd.DataFrame(commandes)


# -------------------------
# AJOUT D'ANOMALIES
# -------------------------

# Valeurs manquantes
for index in random.sample(range(N_CLIENTS), 30):
    clients.loc[index, "ville"] = None

# Doublons
clients = pd.concat([
    clients,
    clients.sample(20, random_state=42)
])

# Prix manquants
for index in random.sample(range(N_PRODUITS), 5):
    produits.loc[index, "prix"] = None

# Quelques commandes avec des IDs inexistants
for index in random.sample(range(N_COMMANDES), 20):
    commandes.loc[index, "client_id"] = N_CLIENTS + random.randint(1, 100)

# Quantités aberrantes
for index in random.sample(range(N_COMMANDES), 10):
    commandes.loc[index, "quantite"] = random.choice([-5, 0, 100])

# Quelques dates incorrectes
for index in random.sample(range(N_COMMANDES), 10):
    commandes.loc[index, "date"] = "DATE_INVALIDE"


# -------------------------
# EXPORT
# -------------------------

clients.to_csv(
    "data/clients.csv",
    index=False,
    encoding="utf-8"
)

produits.to_csv(
    "data/produits.csv",
    index=False,
    encoding="utf-8"
)

commandes.to_csv(
    "data/commandes.csv",
    index=False,
    encoding="utf-8"
)

print("Dataset généré !")
print(f"Clients : {len(clients)}")
print(f"Produits : {len(produits)}")
print(f"Commandes : {len(commandes)}")
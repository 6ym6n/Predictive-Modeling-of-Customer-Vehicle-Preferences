# 🚗 Predictive Modeling of Customer Vehicle Preferences

Ce projet vise à prédire les préférences des clients pour différents types de véhicules en utilisant des techniques de Machine Learning.
Le modèle est entraîné à partir d’un jeu de données client, et une interface utilisateur est proposée pour effectuer des prédictions en local via Tkinter.

---

## 📊 Objectifs

* Analyse exploratoire des données
* Prétraitement et encodage des variables catégorielles
* Entraînement de modèles de classification (SVM, Random Forest, etc.)
* Comparaison des performances
* Création d'une interface graphique simple pour tester les prédictions

---

## 🛠️ Technologies utilisées

* **Python 3**
* **Pandas** — manipulation des données
* **Scikit-learn** — modèles ML, encodage, normalisation, évaluation
* **Matplotlib** — graphiques et visualisations
* **Seaborn** — visualisations statistiques
* **Joblib** — sauvegarde/chargement de modèles
* **Tkinter** — interface utilisateur graphique
* **Jupyter Notebook** — développement interactif

---

## 📁 Structure du projet

```
├── notebook_projet.ipynb     # Notebook principal du projet
├── app_prediction.py         # Application Tkinter à exécuter
├── model.joblib              # Modèle ML entraîné (Random Forest ou SVM)
├── dataset.csv               # Jeu de données client
├── requirements.txt          # Liste des dépendances Python
└── README.md                 # Documentation du projet
```

---

## 📦 Installation

### ✅ Prérequis

* Python 3.8 ou plus récent
* Git
* pip (installé avec Python)

### 📅 Étapes d’installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/6ym6n/Predictive-Modeling-of-Customer-Vehicle-Preferences.git
cd Predictive-Modeling-of-Customer-Vehicle-Preferences
```

2. **(Optionnel) Créer un environnement virtuel**

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

> 💡 **Remarque :** Si tu travailles avec Linux et que Tkinter n’est pas installé :

```bash
sudo apt install python3-tk
```

---

## ▶️ Exécution

Il y a deux façons d'exécuter ce projet :

### 1. 🔹 Interface graphique (recommandée)

Lance directement l'application via Tkinter :

```bash
python app_prediction.py
```

> Ce fichier contient l'interface utilisateur graphique pour charger des données et faire des prédictions.

### 2. 🔹 Notebook Jupyter

1. Lancer Jupyter Notebook :

```bash
jupyter notebook
```

2. Ouvrir le fichier `notebook_projet.ipynb` depuis l’interface web.

> 🧠 Si `jupyter` n’est pas installé :

```bash
pip install notebook
```

---

## 👤 Auteur

**Ayman Naaimi**
🔗 [GitHub](https://github.com/6ym6n)

---

## 📄 Licence

Ce projet est publié sous licence **MIT**.


📄 Voir le rapport complet : [rapport_DWBI_Projet_prediction.pdf](rapport_DWBI_Projet_prediction.pdf)

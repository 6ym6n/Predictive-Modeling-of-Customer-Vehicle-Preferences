import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# === Chargement du modèle et des fichiers ===
model = joblib.load('./Modeles/modele_final.pkl')
label_encoder = joblib.load('./Modeles/label_encoder.pkl')

vehicule_df = pd.read_csv("./Datasets/catalogue__voitures_avec_categories.csv")
features = ['age', 'sexe', 'taux', 'situationFamiliale', 'nbEnfantsAcharge', '2eme voiture']
situation_mapping = {'Célibataire': 0, 'En couple': 1, 'marié': 1}
sexe_mapping = {'F': 0, 'M': 1}
voiture2_mapping = {'Non': 0, 'Oui': 1}

# === Interface ===
root = tk.Tk()
root.title("🔍 Prédiction Catégorie de Véhicule")
root.geometry("900x600")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# === Entrées utilisateur ===
def create_labeled_input(label_text, row, widget):
    ttk.Label(main_frame, text=label_text + " :", anchor="e").grid(row=row, column=0, sticky="e", pady=5)
    widget.grid(row=row, column=1, sticky="we", pady=5)

entry_age = ttk.Entry(main_frame)
create_labeled_input("Âge", 0, entry_age)

combo_sexe = ttk.Combobox(main_frame, values=["F", "M"], state="readonly")
combo_sexe.current(0)
create_labeled_input("Sexe", 1, combo_sexe)

entry_taux = ttk.Entry(main_frame)
create_labeled_input("Taux", 2, entry_taux)

entry_enfants = ttk.Entry(main_frame)
create_labeled_input("Enfants à charge", 3, entry_enfants)

combo_situation = ttk.Combobox(main_frame, values=list(situation_mapping.keys()), state="readonly")
combo_situation.current(0)
create_labeled_input("Situation familiale", 4, combo_situation)

combo_voiture = ttk.Combobox(main_frame, values=["Non", "Oui"], state="readonly")
combo_voiture.current(0)
create_labeled_input("2ème voiture", 5, combo_voiture)

# === Widgets dynamiques ===
label_table = None
tree = None

# === Fonction de prédiction ===
def predire():
    global label_table, tree

    try:
        age = float(entry_age.get())
        sexe = sexe_mapping[combo_sexe.get()]
        taux = float(entry_taux.get())
        nb_enfants = int(entry_enfants.get())
        situation = situation_mapping[combo_situation.get()]
        voiture2 = voiture2_mapping[combo_voiture.get()]

        data = pd.DataFrame([{
            'age': age,
            'sexe': sexe,
            'taux': taux,
            'situationFamiliale': situation,
            'nbEnfantsAcharge': nb_enfants,
            '2eme voiture': voiture2
        }])

        # Prédiction
        pred = model.predict(data[features])
        categorie = label_encoder.inverse_transform(pred)[0]

        messagebox.showinfo("Résultat", f"✅ Catégorie prédite : {categorie}")

        # Nettoyer les widgets précédents s'ils existent
        if label_table:
            label_table.destroy()
        if tree:
            tree.destroy()

        # Affichage du titre
        label_table = ttk.Label(root, text="🚗 Modèles correspondant à la catégorie prédite :", font=("Arial", 11, "bold"))
        label_table.pack(pady=(10, 0))

        # Création du tableau
        tree = ttk.Treeview(root, columns=("marque", "nom", "puissance", "longueur", "nbPlaces", "nbPortes"), show="headings", height=10)
        tree.pack(pady=10)

        for col in tree["columns"]:
            tree.heading(col, text=col.capitalize(), anchor="center")
            tree.column(col, width=110, anchor="center")


        # Filtrer les modèles de la catégorie prédite
        models = vehicule_df[vehicule_df["categorie"] == categorie]

        for _, row in models.iterrows():
            tree.insert("", "end", values=(
                row["marque"], row["nom"], row["puissance"], row["longueur"],
                row["nbPlaces"], row["nbPortes"], row["cluster"]
            ))

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue :\n{e}")

# === Bouton de prédiction ===
btn_predire = ttk.Button(main_frame, text="Prédire", command=predire)
btn_predire.grid(row=6, column=0, columnspan=2, pady=20)

root.mainloop()

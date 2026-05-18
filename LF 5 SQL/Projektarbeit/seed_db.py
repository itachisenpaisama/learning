import sqlite3
import random
from datetime import date, timedelta

# Verbindung herstellen
connection = sqlite3.connect("Recipeportal.db")
connection.execute("PRAGMA foreign_keys = ON;")
cursor = connection.cursor()

print("Verbinde mit Datenbank und setze alte Daten zurück...")

# Alle alten Daten löschen, damit es nicht zu Duplikaten kommt
tables = [
    "Recipe_Ingredient", "Recipe_Category", "Recipe_Diet", "Recipe_Tool",
    "Review", "Nutrition", "Preparationstep", "Recipe", "User",
    "Ingredient", "Category", "Diet", "Tool"
]
for table in tables:
    cursor.execute(f"DELETE FROM {table}")

# Auto-Increment Counter zurücksetzen
cursor.execute("DELETE FROM sqlite_sequence")

# ==========================================
# 1. STAMMDATEN EINFÜGEN
# ==========================================
print("Generiere Benutzer...")
users = [
    ("Anna", "Müller", "anna.m@email.com", "pass123", "1990-05-14", "2023-01-10"),
    ("Ben", "Schmidt", "ben.s@email.com", "geheim", "1985-08-22", "2023-02-15"),
    ("Clara", "Weber", "clara.w@email.com", "qwertz", "1992-11-03", "2023-03-20"),
    ("David", "Wagner", "david.w@email.com", "davidpwd", "1978-01-30", "2023-04-05"),
    ("Emma", "Becker", "emma.b@email.com", "emma2020", "2000-07-19", "2023-05-11"),
    ("Felix", "Hoffmann", "felix.h@email.com", "felixpwd", "1995-12-12", "2023-06-21"),
    ("Greta", "Schäfer", "greta.s@email.com", "gretapwd", "1988-04-25", "2023-07-30"),
    ("Hans", "Koch", "hans.k@email.com", "koch123", "1965-09-09", "2023-08-14"),
    ("Ida", "Bauer", "ida.b@email.com", "bauerpwd", "1998-02-17", "2023-09-02"),
    ("Jan", "Richter", "jan.r@email.com", "janpwd", "1982-10-05", "2023-10-18")
]
cursor.executemany("INSERT INTO User (First_name, Last_name, EMail, Password, Birthday, Registration_day) VALUES (?, ?, ?, ?, ?, ?)", users)

print("Generiere Zutaten...")
ingredients = [
    "Mehl", "Zucker", "Salz", "Eier", "Milch", "Butter", "Olivenöl", "Zwiebeln", "Knoblauch", "Tomaten",
    "Spaghetti", "Hackfleisch", "Hähnchenbrust", "Kartoffeln", "Möhren", "Paprika", "Sahne", "Käse", "Pfeffer", "Basilikum",
    "Oregano", "Zitrone", "Apfel", "Zimt", "Backpulver", "Vanillezucker", "Reis", "Sojasauce", "Ingwer", "Honig"
]
cursor.executemany("INSERT INTO Ingredient (Name) VALUES (?)", [(i,) for i in ingredients])

print("Generiere Kategorien...")
categories = ["Frühstück", "Mittagessen", "Abendessen", "Snack", "Dessert", "Vorspeise", "Hauptspeise", "Beilage", "Kuchen", "Getränk"]
cursor.executemany("INSERT INTO Category (Name) VALUES (?)", [(c,) for c in categories])

print("Generiere Diäten...")
diets = ["Vegetarisch", "Vegan", "Glutenfrei", "Laktosefrei", "Low-Carb"]
cursor.executemany("INSERT INTO Diet (Name) VALUES (?)", [(d,) for d in diets])

print("Generiere Werkzeuge...")
tools = [
    ("Pfanne", "Groß"), ("Topf", "Mittel"), ("Schneidebrett", "Holz"), ("Messer", "Chef"), ("Backofen", "Standard"),
    ("Mixer", "Hand"), ("Auflaufform", "Glas"), ("Rührschüssel", "Groß"), ("Schneebesen", "Metall"), ("Teigschaber", "Silikon")
]
cursor.executemany("INSERT INTO Tool (Name, Size) VALUES (?, ?)", tools)


# ==========================================
# 2. REZEPTE & DETAILS EINFÜGEN
# ==========================================
print("Generiere Rezepte...")
recipes = [
    # Title, Work, Total, Diff, Date, UserID
    ("Spaghetti Bolognese", 20, 60, "Einfach", "2023-11-01", 1),
    ("Pfannkuchen", 10, 20, "Sehr Einfach", "2023-11-05", 2),
    ("Caesar Salad", 15, 15, "Einfach", "2023-11-10", 3),
    ("Apfelkuchen", 30, 90, "Mittel", "2023-11-15", 4),
    ("Hähnchen Curry", 20, 40, "Mittel", "2023-11-20", 5),
    ("Gemüsesuppe", 15, 45, "Einfach", "2023-11-25", 6),
    ("Lasagne", 40, 120, "Schwer", "2023-12-01", 7),
    ("Kartoffelgratin", 20, 60, "Mittel", "2023-12-05", 8),
    ("Schokobrownies", 15, 45, "Mittel", "2023-12-10", 9),
    ("Tomatensalat", 10, 10, "Sehr Einfach", "2023-12-15", 10)
]
cursor.executemany("INSERT INTO Recipe (Title, Working_time, Total_time, Difficulty, Creation_date, UserID) VALUES (?, ?, ?, ?, ?, ?)", recipes)

print("Generiere Zubereitungsschritte...")
steps = [
    # Spaghetti Bolognese (RecipeID 1)
    (1, "Zwiebeln und Knoblauch hacken und in Öl anbraten.", 1),
    (2, "Hackfleisch hinzugeben und krümelig braten.", 1),
    (3, "Tomaten und Kräuter zufügen und 40 Minuten köcheln lassen.", 1),
    # Pfannkuchen (RecipeID 2)
    (1, "Mehl, Eier und Milch zu einem glatten Teig verrühren.", 2),
    (2, "Butter in der Pfanne erhitzen.", 2),
    (3, "Teig portionsweise goldbraun ausbacken.", 2),
    # Apfelkuchen (RecipeID 4)
    (1, "Äpfel schälen und in Spalten schneiden.", 4),
    (2, "Teig aus Mehl, Butter, Zucker und Eiern kneten.", 4),
    (3, "Teig in die Form geben, Äpfel darauf verteilen und 60 Min backen.", 4)
]
# Füge für den Rest Dummy-Schritte hinzu
for i in [3, 5, 6, 7, 8, 9, 10]:
    steps.append((1, "Zutaten vorbereiten.", i))
    steps.append((2, "Alles vermischen und kochen/backen.", i))
    steps.append((3, "Warm servieren.", i))

cursor.executemany("INSERT INTO Preparationstep (Stepnumber, Instruction_text, RecipeID) VALUES (?, ?, ?)", steps)

print("Generiere Nährwerte...")
nutritions = []
for i in range(1, 11):
    nutritions.append((
        random.uniform(200, 800), # Calories
        random.uniform(5, 50),    # Protein
        random.uniform(10, 80),   # Carbs
        random.uniform(5, 40),    # Fat
        random.uniform(0.5, 3),   # Salt
        random.uniform(1, 20),    # Sugar
        random.uniform(2, 15),    # Fiber
        i                         # RecipeID
    ))
cursor.executemany("INSERT INTO Nutrition (Calories, Protein, Carbohydrates, Fat, Salt, Sugar, Fiber, RecipeID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", nutritions)

print("Generiere Bewertungen...")
reviews = []
for i in range(15):
    reviews.append((
        random.randint(3, 5), # Stars
        "Sehr lecker! Habe es schon oft gekocht.", # Text
        "2024-01-10", # Date
        random.randint(1, 10), # UserID
        random.randint(1, 10)  # RecipeID
    ))
cursor.executemany("INSERT INTO Review (Stars, Text, Date, UserID, RecipeID) VALUES (?, ?, ?, ?, ?)", reviews)

# ==========================================
# 3. ZWISCHENTABELLEN EINFÜGEN (Verknüpfungen)
# ==========================================
print("Generiere Verknüpfungen (Zutaten, Kategorien, etc.)...")

# Recipe_Ingredient (RecipeID, IngredientID, Quantity, Unit)
recipe_ingredients = [
    (1, 11, 500, "g"), (1, 12, 400, "g"), (1, 8, 2, "Stück"), (1, 10, 1, "Dose"), # Bolognese
    (2, 1, 250, "g"), (2, 4, 3, "Stück"), (2, 5, 500, "ml"), # Pfannkuchen
    (4, 23, 4, "Stück"), (4, 1, 300, "g"), (4, 2, 150, "g"), (4, 6, 150, "g") # Apfelkuchen
]
# Fill the rest with random ingredients to have enough data
for r_id in [3, 5, 6, 7, 8, 9, 10]:
    for _ in range(random.randint(3, 6)):
        i_id = random.randint(1, 30)
        # Avoid duplicates for the same recipe
        if (r_id, i_id) not in [(x[0], x[1]) for x in recipe_ingredients]:
            recipe_ingredients.append((r_id, i_id, random.uniform(1, 100), "g/ml/Stk"))

cursor.executemany("INSERT INTO Recipe_Ingredient (RecipeID, IngredientID, Quantity, Unit) VALUES (?, ?, ?, ?)", recipe_ingredients)

# Recipe_Category
recipe_categories = [
    (1, 7), (1, 2), # Bolognese ist Hauptspeise & Mittagessen
    (2, 1), (2, 5), # Pfannkuchen ist Frühstück & Dessert
    (3, 6), (3, 4), # Caesar Salad ist Vorspeise & Snack
    (4, 9), (4, 5)  # Apfelkuchen ist Kuchen & Dessert
]
for r_id in range(5, 11):
    recipe_categories.append((r_id, random.randint(1, 10)))
cursor.executemany("INSERT INTO Recipe_Category (RecipeID, CategoryID) VALUES (?, ?)", list(set(recipe_categories)))

# Recipe_Diet
recipe_diets = [
    (2, 1), # Pfannkuchen ist vegetarisch
    (3, 5), # Salad ist low-carb (ohne Croutons)
    (6, 1), (6, 2) # Gemüsesuppe ist vegetarisch & vegan
]
cursor.executemany("INSERT INTO Recipe_Diet (RecipeID, DietID) VALUES (?, ?)", list(set(recipe_diets)))

# Recipe_Tool
recipe_tools = [
    (1, 2), (1, 3), (1, 4), # Bolognese braucht Topf, Brett, Messer
    (2, 1), (2, 8), (2, 9), # Pfannkuchen braucht Pfanne, Schüssel, Besen
    (4, 5), (4, 7) # Apfelkuchen braucht Ofen, Form
]
cursor.executemany("INSERT INTO Recipe_Tool (RecipeID, ToolID) VALUES (?, ?)", recipe_tools)

connection.commit()
connection.close()

print("Erfolgreich! Die Datenbank wurde mit über 200 Einträgen gefüllt.")

import sqlite3

is_db_open = False 
connection = sqlite3.connect("Recipeportal.db") 
is_db_open = True 

# Enable foreign key support
connection.execute("PRAGMA foreign_keys = ON;")
cursor = connection.cursor() 

# ==========================================
# 1. BASIS-ENTITÄTEN (Die Stammdaten)
# ==========================================

sql_user = """CREATE TABLE IF NOT EXISTS User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name TEXT,
    Last_name TEXT,
    EMail TEXT UNIQUE,
    Password TEXT,
    Birthday DATE,
    Registration_day DATE
)"""
cursor.execute(sql_user)

sql_recipe = """CREATE TABLE IF NOT EXISTS Recipe (
    RecipeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Working_time INTEGER,
    Total_time INTEGER,
    Difficulty TEXT,
    Creation_date DATE,
    UserID INTEGER,
    FOREIGN KEY(UserID) REFERENCES User(UserID)
)"""
cursor.execute(sql_recipe)

sql_prepstep = """CREATE TABLE IF NOT EXISTS Preparationstep (
    PreparationstepID INTEGER PRIMARY KEY AUTOINCREMENT,
    Stepnumber INTEGER,
    Instruction_text TEXT,
    RecipeID INTEGER,
    FOREIGN KEY(RecipeID) REFERENCES Recipe(RecipeID)
)"""
cursor.execute(sql_prepstep)

sql_nutrition = """CREATE TABLE IF NOT EXISTS Nutrition (
    NutritionID INTEGER PRIMARY KEY AUTOINCREMENT,
    Calories REAL,
    Protein REAL,
    Carbohydrates REAL,
    Fat REAL,
    Salt REAL,
    Sugar REAL,
    Fiber REAL,
    RecipeID INTEGER UNIQUE,
    FOREIGN KEY(RecipeID) REFERENCES Recipe(RecipeID)
)"""
cursor.execute(sql_nutrition)

sql_review = """CREATE TABLE IF NOT EXISTS Review (
    ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
    Stars INTEGER,
    Text TEXT,
    Date DATE,
    UserID INTEGER,
    RecipeID INTEGER,
    FOREIGN KEY(UserID) REFERENCES User(UserID),
    FOREIGN KEY(RecipeID) REFERENCES Recipe(RecipeID)
)"""
cursor.execute(sql_review)

sql_ingredient = """CREATE TABLE IF NOT EXISTS Ingredient (
    IngredientID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT
)"""
cursor.execute(sql_ingredient)

sql_category = """CREATE TABLE IF NOT EXISTS Category (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT
)"""
cursor.execute(sql_category)

sql_diet = """CREATE TABLE IF NOT EXISTS Diet (
    DietID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT
)"""
cursor.execute(sql_diet)

sql_tool = """CREATE TABLE IF NOT EXISTS Tool (
    ToolID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Size TEXT
)"""
cursor.execute(sql_tool)

# ==========================================
# 2. ZWISCHENTABELLEN (Auflösung der m:n Beziehungen)
# ==========================================

sql_recipe_ingredient = """CREATE TABLE IF NOT EXISTS Recipe_Ingredient (
    RecipeID INTEGER,
    IngredientID INTEGER,
    Quantity REAL,
    Unit TEXT,
    PRIMARY KEY(RecipeID, IngredientID),
    FOREIGN KEY(RecipeID) REFERENCES Recipe(RecipeID),
    FOREIGN KEY(IngredientID) REFERENCES Ingredient(IngredientID)
)"""
cursor.execute(sql_recipe_ingredient)

sql_recipe_category = """CREATE TABLE IF NOT EXISTS Recipe_Category (
    RecipeID INTEGER,
    CategoryID INTEGER,
    PRIMARY KEY(RecipeID, CategoryID),
    FOREIGN KEY(RecipeID) REFERENCES Recipe(RecipeID),
    FOREIGN KEY(CategoryID) REFERENCES Category(CategoryID)
)"""
cursor.execute(sql_recipe_category)

sql_recipe_diet = """CREATE TABLE IF NOT EXISTS Recipe_Diet (
    RecipeID INTEGER,
    DietID INTEGER,
    PRIMARY KEY(RecipeID, DietID),
    FOREIGN KEY(RecipeID) REFERENCES Recipe(RecipeID),
    FOREIGN KEY(DietID) REFERENCES Diet(DietID)
)"""
cursor.execute(sql_recipe_diet)

sql_recipe_tool = """CREATE TABLE IF NOT EXISTS Recipe_Tool (
    RecipeID INTEGER,
    ToolID INTEGER,
    PRIMARY KEY(RecipeID, ToolID),
    FOREIGN KEY(RecipeID) REFERENCES Recipe(RecipeID),
    FOREIGN KEY(ToolID) REFERENCES Tool(ToolID)
)"""
cursor.execute(sql_recipe_tool)

# Änderungen in der DB speichern und Verbindung schließen
connection.commit()
connection.close()
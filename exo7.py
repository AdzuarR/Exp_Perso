recettes = {'Kouglof' : (20, 20, 'difficile'),'Salade de fruits' : (30, 0, 'facile'),'Mousse au chocolat' : (25, 0, 'facile'),'Gateau au yaourt' : (10, 20, 'facile')}
magasin = {'Au panier Bio' : (False, False),'Au supermarché' : (False, True),'Au commerce du jour' : (True, True)}
contient = {('Kouglof', 'Farine'), ('Kouglof', 'Raisins secs'), ('Kouglof', 'Oeufs'),('Kouglof', 'Lait'), ('Salade de fruits', 'Fraises'),('Salade de fruits', 'Pommes'),  ('Salade de fruits', 'Bananes'),('Salade de fruits', 'Oranges'),  ('Salade de fruits', 'Raisins secs'),('Salade de fruits', 'Noix'),  ('Mousse au chocolat', 'Chocolat'),('Mousse au chocolat', 'Oeufs'),  ('Mousse au chocolat', 'Beurre'),('Gateau au yaourt', 'Farine'), ('Gateau au yaourt', 'Yaourt'),('Gateau au yaourt', 'Oeufs'), ('Gateau au yaourt', 'Lait')}
vend = {('Fraises', 'Au panier Bio'), ('Farine', 'Au panier Bio'),('Raisins secs', 'Au panier Bio'), ('Oeufs', 'Au panier Bio'),('Lait', 'Au panier Bio'), ('Pommes', 'Au panier Bio'),('Fraises', 'Au supermarché'),  ('Lait', 'Au supermarché'),('Bananes', 'Au supermarché'),  ('Oranges', 'Au supermarché'),('Noix', 'Au supermarché'),  ('Chocolat', 'Au supermarché'),('Beurre', 'Au commerce du jour'), ('Yaourt', 'Au commerce du jour'),('Chocolat', 'Au commerce du jour') ,  ('Oeufs', 'Au commerce du jour')}

def dico_recette_ensemble_ingredient(contient):
    """
    """
    dico_sortie = {}
    for (recette, ingredient) in contient:
        if recette not in dico_sortie.keys():
            dico_sortie[recette] = set()
        dico_sortie[recette].add(ingredient)
    
    return dico_sortie

print(dico_recette_ensemble_ingredient(contient))

def ouvert_lundi(magasin):
    """
    """
    ouvert = set()
    for (magasin_name,(dimanche, lundi)) in magasin.items():
        if lundi:
            ouvert.add(magasin_name)
    return ouvert

print(ouvert_lundi(magasin))

def ensemble_ingredient(vend, magasin_interet):
    """
    """
    ingredients = set()
    for (ingredient_vendu,magasin_name) in vend:
        if magasin_name == magasin_interet:
            ingredients.add(ingredient_vendu)
    return ingredients
    
print (ensemble_ingredient(vend, 'Au panier Bio'))

def ingredient_dispo_lundi(magasin, vend):
    """
    """
    magasin_ouvert_lundi = ouvert_lundi(magasin)
    ensemble_dispo_lundi = set()
    for elem in magasin_ouvert_lundi:
        ensemble_dispo_lundi = ensemble_dispo_lundi | ensemble_ingredient(vend, elem)
    
    return ensemble_dispo_lundi

print(ingredient_dispo_lundi(magasin, vend))

def recette_du_lundi(magasin, vend, recettes, contient):
    """
    """
    ensemble_recette_lundi = set()
    
    ingredient_du_lundi  = ingredient_dispo_lundi(magasin, vend)
    
    

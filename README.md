# MoneyMaker

## Repo for my money maker application


### Explications

Dans le fichier de base lors de la génération de la fenêtre :
```html
Principe à demander :
    - Avoir la fenêtre de base qui est générée seule, lorsque que nous
utilisons un bouton, cela change le nom de la fenêtre et en fonction du nom,
On utilise une interface personnalisée pour chaque fenêtre.
Interface Base :
    - fenêtre de base avec un bouton de connexion ou d'inscription
    Ou d'ajout de compte supplémentaire (bonus)
    - Le bouton inscription : fonction Create_User()
    - Le bouton connexion : fonction Test_User() A créer
    - Le bouton Ajout de compte : fonction add_User() A créer
    Interface Inscription :
        - Affichage d'un form pour insérer ses données
        - Bouton Valider qui test si les données du form sont correctes
        - Bouton Valider Ouvre l'interface utilisateur
    Interface Connexion :
        - Affichage d'un form pour insérer le pseudo et le mdp
        - Si correcte, envoie interface utilisateur
        - Si incorrecte, Renvoie sur la fenêtre de base

```
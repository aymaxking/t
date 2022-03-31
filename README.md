# DoChecker

Projet de développement autour de Python/Angular

# Charte graphique 

 - Utilisation des composant angular material
   https://material.angular.io/  
   
 - Sauf pour les tableaux, utilisation de
   https://www.ag-grid.com/angular-data-grid/getting-started/
   
La charte graphique du portail : https://dxcportal.sharepoint.com/:u:/r/sites/DoChecker/Shared%20Documents/General/Charte%20graphique/material-dashboard-angular2-master.zip?csf=1&web=1&e=0yNkfj 

Ce projet a été généré avec [Angular CLI](https://github.com/angular/angular-cli) version 1.0.0 et angular 4.x.

1. Install NodeJs from [NodeJs Official Page](https://nodejs.org/en).
2. Ouvrir un Terminal
3. Aller au projet (au même niveau que package.json)
4. Assurez-vous que vous avez bien installé [Angular CLI](https://github.com/angular/angular-cli). Si ce n'est pas le cas, merci de l'installer
5. Lancez dans un terminal : ```npm install```
6. Lancez`ng serve`. Naviguez à `http://localhost:4200/`. L'application redémarre automatiquement en cas de modification


# Process de gestion des branches

![enter image description here](https://nvie.com/img/git-model@2x.png)

# Process de création de branche

Sur le projet on suit les préconisation de GitFlow en la matière de création de branche. En effet chaque bug/fonctionnalités developpés doit être commité sur une branche, ensuite une PR doit être demandé pour la mergé sur la branche develop (sur le projet elle est nommée dev). 

La création de chacune des ses Features/Bug doit respecter le nommage suivant :


 - Pour une nouvelle fonctionnalité (US)

		feature-DOC-XXX

		XXX: Numéro du ticket JIRA_

 - Pour les Bug :

		Bug-DOC-XXX

		XXX: Numéro du ticket JIRA_

 - Pour les HotFix (anoamlie post Release ou en production)

		HotFix-DOC-XXX

		_XXX: Numéro du ticket JIRA_



# Back-Front


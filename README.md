# gamification_adaptative

###Première partie :
#####Décrivez/commentez deux des matrices de résultats de l’analyse PLS. 
Nous avons choisi de décrire les matrices suivantes: 
- Path coefs de l’élément ludique badge pour le profil Hexad :


![alt text](images/badgepchexad.png)

La matrice présente pour chaque catégorie hexad (Le Socialiser, Le Free Spirit, L’Achiever, Le Philanthropist, Le Disruptor, Le Player) les coefficients de variation de la motivation intrinsèque, la motivation extrinsèque et d'amotivation selon l'élément ludiques (badge dans ce cas).


- P val de l’élément ludique badge pour le profil Hexad :

![alt text](images/badgespvalshexad.png)

On utilise la technique de p value pour valider ou rejeter des coefficients. Pour ce faire, cette matrice est associée à la matrice “path coef”, pour valider ou pas selon la p valeur max choisie (i p<0.05, voir p<0.1 en fonction de la précision souhaitée), le coefficient existant dans les mêmes cordonnées respectives. 
Par exemple, si on choisit p <0.1, on voit bien que la p valeur pour “freeSpirit”,”MEVar” est égale à 0.0510341081952265 qui est bien inférieur à 0.1. Ceci valide le path coef -0.441996464538212 pour “freeSpirit”,”MEVar”. 


#####Recommandations à partir des matrices PLS 
Nous avons créé la classe Student qui décrit l’élève, elle permet de calculer/récupérer ses statistiques à partir du fichier csv userStats.csv. La méthode printStatistics() permet d’afficher pour l’élève en question ses statistiques. 

De multiples méthodes get\[nomDuParamVoulu]() permettent de retourner la valeur du paramètre en question. Par exemple:
- getArchiver() retourne le coefficient de la catégorie Archiver pour cet élève récupéré du csv. 
- getME() récupère les valeur de motivation extrinsèques initiales (meidI; meinI; mereI) les additionne et retourne la valeur de motiviation extrinsèque initiale totale.


La méthode getRandomStudent(), permet de récupérer des données d’un étudiant aléatoirement du csv et de retourner une instance Student à partir de celles-ci.


la méthode pathCoefsValidation() reçoit en paramètre:
- pCoefs : La matrice des path coef d’un élément ludique donnée 
- pValues : La matrice p val équivalente
- validateValue : La p valeur max 
- factor : Le type de profil (hexad ou motivation) pour savoir quel traitement faire selon le profil

Cette méthode permet de vérifier si un coefficient dans la matrice pathCoef est pertinent et donc à garder, selon la valeur p val dans correspondante dans la matrice pval. Les coef qui ont un p val supérieur à validateValue  seront mis à 0 et le nouveau pathcoef sera retourné par cette méthode.


Rappelons les définition suivantes :
- La motivation intrinsèque : l’action est conduite uniquement par l’intérêt et le plaisir que l’individu trouve à l’action, sans attente de récompense externe.

- La motivation extrinsèque : l’action est provoquée par une circonstance extérieure à l’individu (punition, récompense, pression sociale, obtention de l’approbation d’une personne tierce...).

Ces deux types de motivations sont complétés par un troisième état : l’amotivation 
- L’amotivation : l’individu a le sentiment d’être soumis à des facteurs hors de tout contrôle. L’amotivation se distingue de la motivation extrinsèque par l’absence de motivation liée au sentiment de ne plus être capable de prévoir les conséquences de ses actions.


Donc pour calculer le score de motivation il faut additionner les valeurs de motivations intrinsèques et extrinsèque puis en soustraire la valeur de l’amotivation.

######Vecteur d'affinité pour profil Hexad 



######Vecteur d'affinité pour profil motivation 


###Deuxième partie :
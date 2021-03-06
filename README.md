# Django & Buildout

## Intro et vocabulaire

Django est un framework Python pour faire des sites web et/ou des applications web.

Python est un langage de programmation.

Les packages standardisés et distribuables Python se nomme des eggs.

Buildout, à l'aide de son fichier de config, permet de reproduire un environnement spécifique pour des applications Python.

Quelques avantages de Buildout:

* Il nous crée un environnement virtuel pour notre application.
* Il télécharge et installe des eggs multiples provenant de sources diverses. ([pypi](http://pypi.python.org/pypi), repo Git & SVN)
* On peut utilisé des [recipes](http://pypi.python.org/pypi?:action=browse&show=all&c=512) pour ajouter de nouvelles fonctionnalités à l'application qui est construite. Dans le cas de django, on utilise [celui-ci](http://pypi.python.org/pypi/djangorecipe/0.23.1).

## Pourquoi utiliser Buildout pour déployer une application Django ?

### Parce que télécharger des packages et les installer à bras peut être fastidieux dépendamment des fonctionnalités du projet.

La procédure habituelle d'installation d'un egg est la suivante:

    wget https://github.com/jdriscoll/django-imagekit/tarball/develop
    tar -xvf jdriscoll-django-imagekit-4a1d1d9.tar.gz
    cd jdriscoll-django-imagekit-4a1d1d9
    python setup.py install

Imaginez maintenant le faire pour 5, 10, 20 packages et ce, sur 3 ou 4 postes de développement + le serveur de prod...

### Pourquoi un environnement virtuel pour mon application ?

La méthode d'installation précédente a également un autre problème; elle pollue l'installation globale de Python pour tout le système !

Or, peut-être qu'une autre application dépend d'une version antérieur du même package que l'on vient de mettre à jour !!

Bref, nous pouvons isoler l'environnement d'une application. 

Autant le faire pour éviter un casse-tête similaire au DLL Hell.

## Show me some code !

1. Présentation du fichier de config Buildout
2. Faire rouler bootstrap.py

        python bootstrap.py

3. Faire rouler l'executable 
    
        bin/buildout 

4. Faire rouler django

        bin/opencode runserver 0.0.0.0:9696

5. Ajouter un nouveau package (markdown) dans les eggs dans le fichier de config.
6. refaire l'étape 3 pour obtenir le package
7. Activer markdown pour le contenu via un templatetag
8. magie !
# Django & Buildout

## Intro et vocabulaire

Django est un framework Python pour faire des sites web et/ou des applications web.

Les packages Python se nomme des eggs.

Buildout, à l'aide de son fichier de config, permet de reproduire un environnement spécifique pour des applications.

Ses avantages sont les suivants:

* Il nous crée un environnement virtuel pour notre application.
* Il assemble des eggs multiples provenant de sources diverses.
** [pypi](http://pypi.python.org/pypi)
** repo Git
** repo SVN 

## Pourquoi utiliser Buildout pour déployer une application Django ?

### Parce que télécharger des packages et les installer à bras peut être fastidieux dépendamment des fonctionnalités du projet.

La procédure habituelle est la suivante:

    wget https://github.com/jdriscoll/django-imagekit/tarball/develop
    tar -xvf jdriscoll-django-imagekit-4a1d1d9.tar.gz
    cd jdriscoll-django-imagekit-4a1d1d9
    python setup.py install

Imaginez maintenant le faire pour 5, 10, 20 packages...

### Pourquoi un environnement virtuel pour mon application ?

La méthode d'installation précédente a également un autre problème; elle pollue l'installation globale de Python pour tout ton système !

Or, peut-être qu'une autre application dépend d'une version antérieur du même package que tu viens de mettre à jour !!

Bref, nous pouvons isoler l'environnement d'une application. 

Autant le faire pour éviter un casse-tête similaire au DLL Hell.

## Show me some code !

...
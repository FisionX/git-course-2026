# NOTAS DEL CURSO

## GIT STATUS
git status te dice que hace falta actualizar tanto en el servidor 'origin/main' como en el git hub

## GIT ADD
Una vez que se añadio un archivo nuevo para incluirlo en el proyecto hacer git add 'Nombre', se hace para tener los cambios listos para hacer commit

- git add .: Añade todos los archivos al staging hasta los nuevos
- git add u: Añade solo los archivos cambiados al staging

## GIT COMMIT
git commit -m "comentario" guarda los cambios del staging area con un comentario

git commit -am "comentario": Es el equivalente de hacer:

 git add -u + git commit -m

git push lo sube al git hub

## GIT BRANCH

- `git branch:` Enlista las ramas
- `git branch "nombre":` Crea una rama nueva
- `git branch -D "nombre":` Borra ramas

## GIT CHECK OUT

Git checkout sirve para intercambiar ramas o commits

- git switch "nombre de la rama" te mueve a la rama

## GIT PUSH

- git push por default 

por default el server remote principal se le llama *origin*

- git push -u origin <branch>

Subir cambios al remote (server)
- git push <remote> <branch>


**Glosario**

- remote: servers a los cuales subir cambios

- origin: server default para hacer los cambios

Si cambiamos la branch upstream

## que rollo sami 
# Notes

## Git add 

- `git add .` : Anadir todos los archivos cambaindo a stating
, incluso a archivos nuevos
- `git add - u` : Anadir solo los archivos cambiados al area de stating

## Git commit
guarda los cambios del staging area
- `git commit -m "comentarios"` : 

## Git push 
subir cambio al *remote* (server)

`git push` por default sube los cambios de nuestro branch al
*upstream* branch, la cual es la branch default al 
- `git push <remote><branch>` : sirve para subir los cambios a las ramas principales y asi
- `git push -u` : 


## Git branch
`git branch` : Enlistar ramas y crea ramas nuevas en el repositorio
- `git branch` se usa para enlistar
- `git branch <rama>` crea ramas
- `git branch -D <rama>` eliminar ramas

## Git checkout 
`git checkout` : sirve para intercambiar ramas o commits

## Git switch

- `git switch <rama> :` cambiar a la rama

**glosario**

Si cambuiamos la branch upstream, podremos pushear sin especificar los cambios asi como

```
git push -u origin <branch> : 
```
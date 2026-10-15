# Notes

## Git status

## Git add

- `git add .`: Añadir todos los archivos cambiados a staging, incluso archivos nuevos
- `git add -u`: Añadir solo los archivos cambiados al area de staging

## Git commit

Guarda los cambios del staging area

- `git commit -m "Comentario"`: hace un commit con un comentario
- `git commit -am "Comentario`: Es el equivalente de:
  ```bash
  git add -u
  git commit -m "Comentario"
  ```

## Git branch
`git branch` sirve para enlistar o crear nuevas ramas
de nuestro repositorio

- `git branch`: Enlistar ramas
- `git branch <rama>`: Crea una nueva rama
- `git branch -D <rama>`: Elimina una rama

## git checkout

Git checkout sirve para intercambiar ramas o commits

- `git switch <rama>`: chambiar a una rama
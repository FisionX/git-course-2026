# Notes

# Git clone

```bash
git clone <url del repositorio>
```

Crear una carpeta con el nombre del repo y clonar el repositorio ahí

## Git status

## Git add

- `git add .`: Añadir todos los archivos cambiados a staging, incluso archivos nuevos
- `git add -u`: Añadir solo los archivos cambiados al area de staging

## Git push

`git push` por default sube los cambios de nuestro branch al *upstream* branch, la cual es la branch default para sincronizar cambios

por default tenemos a nuestro remote principal llamado *origin*

Subir cambios al *remote* (server)
- `git push <remote> <branch>`: subir cambios de nuestro branch al server remote

**Glosario**

- **remote**: servers a los cuales subir cambios
- **origin**: server default para subir los cambios

Si cambiamos la branch upstream, podremos pushear nuestros cambios sin especificar a que rama todo el tiempo

```
git push -u origin <branch>
```

`-u` es igual que `--set-upstream`

Ahora nuestra rama local va a seguir a otra rama distinta de main en el *remote*

## Git commit

Guarda los cambios del staging area

- `git commit -m "Comentario"`: hace un commit con un comentario
- `git commit -am "Comentario`: Nos ahorra tiempo al ser el equivalente de
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

## git switch

Git checkout sirve para intercambiar ramas o commits

- `git switch <rama>`: chambiar a una rama
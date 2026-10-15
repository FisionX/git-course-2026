## Repositorio de git 15/10/26

- jorge habib hernandez rojas

`codigo ....`


# Notes

## git add:

 `git add .`: añade todos los archivos cambiados al area de staging, incluso archivos nuevos

 `git add -u`: añade solo los archivos cambiados al area de staging

## Git push

 `git push `: por default sube los cambios de nuestro branch al *upstream* branch, la cual es la branch default para sincronizar cambios

por default tenemos a nuestro remote principal llamado *origin* 


subir cambios al *remote* (server)

-  `git push <remote> <branch>`: subir cambios de nuestra  branch al server remote

#### cambiar upstream

si cambiamos la branch upstream podemos pushear nuestros cambios sin especificar a que rama todo el tiempo
    
`git push -u origin <branch> `: la rama usptream ahora es branch


### glosario 
    
    remote: server a los cuales subir cambios 
    origin: sever default para subir cambios 

 ## Git commit
 guarda los cambios del staging area

 `git commit -m  "comentario".`: guarda los cambios del staging area

 `git commit -am "comentario"`: añade solo los archivos cambiados al area de staging



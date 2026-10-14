# Taller de Git desde cero — Día 1

**Duración:** 2 horas · **Nivel:** principiantes · **Requisitos:** computadora con Windows o macOS, conexión a Internet y una cuenta gratuita de [GitHub](https://github.com/).

## Índice

- [¿Qué es Git y de dónde viene?](#qué-es-git-y-de-dónde-viene)
- [Instalación en Windows y macOS](#instalación-en-windows-y-macos)
- [Primeros pasos en la terminal: PowerShell y Bash](#primeros-pasos-en-la-terminal-powershell-y-bash)
- [Configuración inicial de Git](#configuración-inicial-de-git)
- [Glosario esencial](#glosario-esencial)
- [El flujo de trabajo básico](#el-flujo-de-trabajo-básico)
- [Práctica guiada: tu primer fork](#práctica-guiada-tu-primer-fork)
- [Errores frecuentes y comprobación](#errores-frecuentes-y-comprobación)
- [Recursos para seguir aprendiendo](#recursos-para-seguir-aprendiendo)

---

## ¿Qué es Git y de dónde viene?

**Git** es un **sistema de control de versiones distribuido**: registra la evolución de archivos a lo largo del tiempo. Permite recuperar versiones anteriores, comparar cambios y colaborar sin tener que enviar archivos llamados `proyecto_final_v2_ahora_si.txt`.

**Ejemplo:** tú y otra persona modifican un proyecto. En vez de sobrescribir el trabajo de la otra persona, cada una registra sus cambios y Git ayuda a integrarlos.

### Linus Torvalds y el nacimiento de Git

**Linus Torvalds** es un ingeniero de software finlandés, conocido por iniciar el desarrollo del *kernel* de Linux en 1991. En **2005** impulsó la creación de Git para gestionar de manera eficiente las aportaciones de muchas personas al kernel de Linux. El proyecto había usado **BitKeeper**, una herramienta propietaria; cuando cambió la relación con su proveedor y se perdió su disponibilidad gratuita para ese uso, la comunidad necesitó otra solución.

Git se diseñó con objetivos como **rapidez**, **trabajo distribuido**, **integridad del historial** y **manejo eficiente de ramas y proyectos grandes**.

### Git no es lo mismo que GitHub

- **Git:** programa que administra versiones en tu computadora.
- **GitHub:** plataforma web que aloja repositorios Git y facilita la colaboración (forks, pull requests, revisión de cambios).
- **Repositorio:** carpeta de un proyecto administrada por Git y su historial.

Git funciona sin GitHub ni Internet para muchas operaciones, como crear commits y consultar el historial. Necesitas conexión para sincronizar con un servidor remoto.

**Pregunta de discusión:** ¿qué problemas habría si cinco personas editaran el mismo documento y se lo mandaran por correo?

## Instalación en Windows y macOS

### Windows

1. Abre la página oficial: https://git-scm.com/install/windows
2. Descarga **Git for Windows** compatible con tu equipo y ejecuta el instalador.
3. Para este taller puedes conservar las opciones predeterminadas. Asegúrate de que quede instalado **Git Bash**.
4. Busca **Git Bash** en el menú Inicio y ábrelo. También puedes usar **PowerShell**.
5. Comprueba la instalación:

```bash
git --version
```

**Alternativa, si ya tienes `winget`:** en PowerShell puedes ejecutar `winget install --id Git.Git -e --source winget`. Si acabas de instalar Git, cierra y vuelve a abrir la terminal.

### macOS

1. Abre **Terminal** (Aplicaciones → Utilidades → Terminal; también puedes buscarla con Spotlight).
2. Puedes instalar las herramientas de línea de comandos de Apple, que incluyen Git:

```bash
xcode-select --install
```

3. Sigue las instrucciones del sistema. Si ya están instaladas, macOS puede indicártelo.
4. Comprueba la instalación:

```bash
git --version
```

**Alternativa con Homebrew**, si ya lo usas: `brew install git`. Consulta https://git-scm.com/install/mac.

> La versión exacta que aparece con `git --version` puede variar. Lo importante es que el comando funcione.

## Primeros pasos en la terminal: PowerShell y Bash

Una **terminal** es una ventana donde escribimos instrucciones para trabajar con archivos y programas. Una **shell** interpreta esas instrucciones.

- **PowerShell:** shell muy utilizada en Windows; trabaja con comandos y objetos.
- **Bash:** shell frecuente en Linux y disponible en Windows mediante Git Bash; macOS usa **zsh** por defecto, cuya sintaxis para los comandos de este taller es muy similar a Bash.
- **Git Bash:** aplicación incluida con Git for Windows que ofrece una experiencia Bash.

**Para simplificar:** durante la práctica de Git usaremos comandos compatibles con PowerShell, Git Bash y la terminal de macOS, salvo cuando se indique una diferencia.

### Comandos básicos

| Acción | PowerShell (Windows) | Bash / Git Bash / macOS |
| --- | --- | --- |
| ¿Dónde estoy? | `pwd` | `pwd` |
| Ver archivos | `ls` | `ls` |
| Entrar a una carpeta | `cd nombre-carpeta` | `cd nombre-carpeta` |
| Subir una carpeta | `cd ..` | `cd ..` |
| Volver a tu carpeta personal | `cd ~` | `cd ~` |
| Crear una carpeta | `mkdir pruebas-git` | `mkdir pruebas-git` |
| Limpiar la pantalla | `Clear-Host` o `cls` | `clear` |
| Mostrar un archivo Markdown | `Get-Content practica.md` | `cat practica.md` |

**Reglas útiles:** pulsa **Enter** para ejecutar; la tecla **Tab** suele completar rutas; las flechas permiten recuperar comandos anteriores. Si una ruta tiene espacios, escríbela entre comillas, por ejemplo `cd "Mis proyectos"`.

### Mini ejercicio: explorar sin modificar nada importante

```bash
pwd
ls
mkdir pruebas-git
cd pruebas-git
pwd
cd ..
```

Comprueba que puedes identificar en qué carpeta estás y cómo regresar. **No copies el símbolo `$`** de ejemplos que lo muestren como indicativo de terminal: escribe solamente el comando.

## Configuración inicial de Git

Git guarda un **nombre de autor** y un **correo electrónico** en cada commit. Configúralos una vez en tu computadora:

```bash
git config --global user.name "Tu Nombre Apellido"
git config --global user.email "tu-correo@ejemplo.com"
```

**Sustituye** el texto entre comillas por tus datos. Si usas GitHub, puedes elegir el correo asociado a tu cuenta o su dirección privada `noreply` (configurada en los ajustes de GitHub) para proteger tu correo personal.

Para comprobarlo:

```bash
git config --global --get user.name
git config --global --get user.email
```

`--global` significa que los valores se usarán por defecto en los repositorios de este usuario de la computadora. En un proyecto específico se pueden establecer valores distintos sin `--global`.

> **Importante:** `user.name` y `user.email` **no inician sesión en GitHub** ni proporcionan permisos para hacer push. La autenticación es un paso separado (por ejemplo, mediante un navegador/gestor de credenciales o SSH). No escribas tu contraseña de GitHub como si fuera un comando Git.

## Glosario esencial

| Término | Significado explicado desde cero |
| --- | --- |
| **Repository (repositorio)** | Proyecto y su historial de versiones gestionado por Git. |
| **Working directory (directorio de trabajo)** | Archivos tal como están actualmente en tu carpeta local. |
| **Staging area / index** | Lista provisional de cambios que eliges incluir en el próximo commit. |
| **Commit** | Registro de un conjunto de cambios con un identificador, autor y mensaje. |
| **Branch / branching** | Rama o línea de trabajo independiente dentro del historial; permite experimentar sin modificar directamente otra rama. |
| **Merge** | Integración de cambios de una rama en otra. |
| **Remote** | Repositorio vinculado que está en otro lugar, normalmente en un servidor como GitHub. |
| **`origin`** | Nombre convencional del remoto desde el que clonaste; en este taller será **tu fork**. |
| **Fork** | Copia de un repositorio en tu cuenta de GitHub, independiente del original pero conectada a él. |
| **Upstream** | Literalmente, “aguas arriba”. Suele referirse al repositorio original del que salió el fork. También puede indicar la rama remota que sigue una rama local: **son usos relacionados, pero distintos**. |
| **Downstream** | “Aguas abajo”: copia o proyecto que recibe cambios de otro repositorio, como un fork respecto al original. No es un nombre obligatorio de remoto. |
| **Clone** | Descargar un repositorio remoto y su historial a tu computadora. |
| **Push** | Enviar commits locales a un repositorio remoto. |
| **Pull / fetch** | `fetch` obtiene información y commits remotos; `pull` los obtiene y además intenta integrarlos en tu rama. |
| **Pull request (PR) / merge request (MR)** | Solicitud para revisar e integrar cambios. GitHub usa *pull request*; GitLab suele usar *merge request*. Son funciones de las plataformas, no comandos básicos de Git. |

**¡No confundas!** Hacer un *fork* en GitHub, crear una *branch* con Git y hacer un *clone* son tres acciones diferentes.

## El flujo de trabajo básico

### Cuatro momentos

```text
(1) DEVELOPMENT / EDICIÓN      (2) STAGING             (3) COMMIT             (4) PUSH
Archivos en tu carpeta  ──git add──>  Cambios preparados ──git commit──> Historial local ──git push──> GitHub
        │
        └── git status: consulta qué ha cambiado y qué falta preparar
```

**Developing / edición:** creas o modificas archivos de tu proyecto. Todavía no has guardado esos cambios como un commit.

**Staging:** con `git add` decides qué cambios entrarán en el siguiente commit. Es como colocar páginas seleccionadas en una carpeta antes de archivarlas.

**Commit:** con `git commit` registras una versión local, con un mensaje claro. No publica nada por sí solo.

**Pushing:** con `git push` envías tus commits locales a GitHub, siempre que tengas acceso al remoto y puedas autenticarte.

### Comandos que usaremos

```bash
git status                         # Revisa cambios actuales
git add practica.md              # Prepara un archivo
git diff --staged                 # Revisa cambios preparados
git commit -m "Completo mi presentación"  # Crea un commit local
git log --oneline -5             # Muestra los últimos 5 commits
git push                         # Envía los commits al remoto configurado
```

**Importante:** `git add` no guarda un commit y `git commit` no sube archivos a Internet. En un clon con rama remota de seguimiento, `git push` suele bastar; si Git pide configurar la rama remota, sigue la indicación que muestra.

### Ejemplo mental

Piensa en una tarea escrita: **editar** es escribir el borrador; **staging** es seleccionar las páginas; **commit** es entregar una versión cerrada a tu archivo personal; **push** es enviar esa versión al espacio compartido.

## Práctica guiada: tu primer fork

**Archivo de trabajo:** [`practica.md`](practica.md).

**Objetivo:** crear tu copia del repositorio del taller, editar el archivo de práctica, confirmar el cambio y verlo publicado en tu propio GitHub. No hace falta saber programar.

### Preparación

- Inicia sesión en https://github.com/ (crea una cuenta si aún no tienes).
- Abre el repositorio del taller que compartió la persona instructora.
- Comprueba que ya tienes Git instalado y configurado (`git --version` y `git config --global --get user.name`).

### Haz un fork en GitHub

1. En el repositorio original, pulsa el botón **Fork**.
2. Elige tu propia cuenta como destino y confirma.
3. Revisa que estás viendo el repositorio bajo **tu nombre de usuario**.

**Resultado esperado:** tienes una copia en tu cuenta; el repositorio original de la persona instructora no se ha modificado.

### Clona tu fork a tu computadora

1. En **tu fork**, pulsa **Code → HTTPS** y copia la URL.
2. Abre la terminal, ve a una carpeta donde quieras guardar el curso y escribe:

```bash
git clone https://github.com/TU-USUARIO/NOMBRE-DEL-REPO.git
cd NOMBRE-DEL-REPO
```

Sustituye `TU-USUARIO` y `NOMBRE-DEL-REPO` por los valores reales de la URL. El primer comando descarga la copia; el segundo entra a la carpeta.

Comprueba:

```bash
git status
git remote -v
```

En `git remote -v` debe aparecer la URL de **tu fork** con el nombre `origin`.

### Edita `practica.md`

Abre el archivo con un editor de texto (Bloc de notas, VS Code, TextEdit en **texto sin formato**, etc.) y completa las preguntas indicadas. **Guarda el archivo** antes de volver a la terminal.

> Consejo: si tu editor pregunta por el formato, utiliza texto plano `.txt`. No necesitas instalar un editor especial.

### Observa la modificación

```bash
git status
git diff
```

Deberías ver que `practica.md` tiene cambios y que Git puede compararlos con la versión anterior.

### Prepara y registra el cambio

```bash
git add practica.md
git status
git diff --staged
git commit -m "Agrego mi presentacion al taller"
```

Comprueba el historial:

```bash
git log --oneline -3
```

### Publica en tu fork

```bash
git push
```

Si es tu primera vez, Git o el gestor de credenciales puede pedirte **autorizar el acceso a GitHub desde el navegador**. Sigue las instrucciones que aparezcan. GitHub no acepta la contraseña de tu cuenta como contraseña de Git por HTTPS; se utilizan métodos como credenciales administradas o tokens cuando corresponda.

Regresa al navegador, recarga **tu fork** y abre `practica.md`: tus respuestas deberían aparecer ahí.

## Errores frecuentes y comprobación

| Situación | Qué revisar |
| --- | --- |
| `git` no se reconoce como comando | Git no está instalado o hace falta cerrar y reabrir la terminal. |
| `fatal: not a git repository` | Entra a la carpeta descargada con `cd NOMBRE-DEL-REPO`. |
| `nothing to commit, working tree clean` | ¿Guardaste cambios? Si ya hiciste commit, es normal que esté limpio. |
| `Please tell me who you are` | Configura `user.name` y `user.email` como en la sección de configuración inicial. |
| `Permission denied` / error de autenticación al hacer push | Verifica que `origin` apunte a **tu fork** y completa el inicio de sesión/autorización de GitHub. |
| `Everything up-to-date` | No hay nuevos commits locales pendientes de enviar, o ya se enviaron. |



## Recursos para seguir aprendiendo

- [Libro Pro Git (español)](https://git-scm.com/book/es/v2) — Introducción oficial y gratuita.
- [Breve historia de Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Una-breve-historia-de-Git) — Contexto de su creación.
- [Instalación oficial de Git](https://git-scm.com/install/) — Opciones para cada sistema operativo.
- [Guía de forks de GitHub](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) — Más información sobre copias y colaboración.
- [Documentación de Git](https://git-scm.com/docs) — Referencia de comandos.

---

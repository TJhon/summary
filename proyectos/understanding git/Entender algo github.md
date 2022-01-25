Cofigure tooling 

git config --global user.name "Jhon"
git config --global user.email "fr.jhonk@gmail.com"

Branch  (trabajo en equipo)

git branch nombre-incicio Mmaste, ayudantes
git checkout branch o commint
git merge [nombre] combina con el historial (cuando esta bien trabajo en equipo)
gir brach -d [version-eliminar] eliminar una version
git brachh --all #incluido remote 


Crear repositorios

git init # repositorio git
git clone [url] #descarga una version de internet
git remote add nombre url # cuando se quiere subir un repositorio

Utiles 

git status # ver lo que se modifica
git status -s # en donde se hace el cambio
git tag -a - m "commits" v.00 # versiones 

sincronizar cambios

git fetch # descarga el historial de la version en linea
git merge # conbian localmente
git push # sube la version
git pull # conbinacion de git fetch y gir merge 

Hacer cambios

git log # versiones de trabajo
git log --follow [file] # historial 
git diff [version1]...[version2] # ver las diferencias en los dos archivos
git show [commit]  lo que contiene cada comentario
git add [file] #captura de la version en la que se trabaja
git commit -m "un commit"


Rehacer 

git reset [commit] # deshace despues del commit
git reset --hard [commit] #deshace cambios anteiroes a este 

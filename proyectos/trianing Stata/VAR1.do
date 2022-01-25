*Series de tiempo

*// importar la base de datos

use http://www.stata-press.com/data/r13/lutkepohl2, clear

*** declarar que se esta trabajando con una serie de tiempo y declarar cual es la variable temporal

tsset qtr


****** Diccionario de variables ******

* - inv: Inversion
* - consump: Consumo
* - inc: Ingreso
* - ln_*: Logarito de la variable (inversion, consumo o ingreso)
* - dln_*: Primera diferencia (lag) de la variable (inversion, consumo o ingreso)

** 1) Grafico consumo inversion

* - graph twoway: sobrepone los graficos dentro de los parentesis
* - lfit: estima un modelo de regresion lineal y muestra su pendiente
* - scatter: grafico de puntos entre las 2 variables
* - xtitle: nombre de la etiqueta del eje x
* - ytitle: nombre de la etiqueta del eje y
* - title: titulo del grafico

graph twoway (lfit inv consump) (scatter inv consump), xtitle("Consumo") ytitle("Inversion") title("Consumo inversion")
graph twoway (lfit inv consump) (scatter inv consump), xtitle("Consumo") ytitle("Inversion") title("Consumo inversion (Escala logarítmica)")

** 2) Pendiente consumo sobre ingreso

** - reg: si no hay nada adicional, especificaciones despues de la coma, es una regresion lineal


reg consump inc

** # En este caso existe una propencion marginal a consumir es de 0.85, es decir que casi el 85% del ingreso se gasta.
** # Tambien se tiene un consumo autonomo de 21.41

** # Esta regresion puede no ser ya que no se
** # tiene el tratamiento de datos de series de tiempo, ya que hasta este punto no se comprobo la estacionariedad de las variables


** 3) Estacionariedad


*** Funciones
* - display: en este caso para mostrar un comentario en pantalla
* - trend: tendencia
* - las(): Retardos a tomar en la prueba
* - dfuller: test de raiz unitaria Aumentada de Dickey Fuller (ADF)
  * - el punto de corte es |3.481| si cae en la zona de aceptacion, entonces la variable no es estacionaria
  * - Los procedimientos son:
    * - Probar con las variables normales con tendencia
    * - Tomar logaritmos con la esperanza de que sean estacionarias (a veces aun con logaritmos conservan la tendencia por lo que aun se especifica la tendencia)
    * - Tomar diferencia a las variables logaritmicas (en este caso ya no se especifica la tendencia)


display "Variables originales"

* En este caso ninguna de las variables es estacionaria ya que los z(t) son inferiores al punto de corte
* |z(t)|:
  * - consump: 2.334
  * - inv: 3.188
  * - inc: 2.294

dfuller consump, lags(4) trend
dfuller inv, lags(4) trend
dfuller inc, lags(4) trend

display "Variables en logarigmos: consumo (ln_consump),  inversion (ln_inv) e ingresos (ln_inc)"

* En este caso tampoco ninguna de las variables es estacionaria ya que los z(t) son inferiores al punto de corte
* |z(t)|:
  * - consump: 0.75
  * - inv: 3.133
  * - inc: 1.318

dfuller ln_inc, lags(4) trend
dfuller ln_inv, lags(4) trend
dfuller ln_consump, lags(4) trend

display "Variables en primera diferencia logaritmica: consumo (ln_consump),  inversion (ln_inv) e ingresos (ln_inc)"

* En este todas las variables son estacionarias
* |z(t)|:
  * - consump: 8.389
  * - inv: 11.136
  * - inc: 9.75

dfuller dln_inc
dfuller dln_inv
dfuller dln_consump

** 4) estimacion var

** var: estima un modelo var, por default son 2 retardos que calcula en las estimaciones

var dln_inv dln_inc dln_consump


** 5) IRF grafico, consumo

*** - irf: comando de impulso respuesta
***   - irf create: Crea un archivo irf en la memoria fisica (temp)
***   - step: el espacion temporal
***   - set especificamos el archivo temporal
***   - irf graph: especificamos el grafico impulso respeuesta
***   - impulse: variable impulso
***   - response: variable respuesta


irf create irf_mod, step(10) set(irf_mod) replace

** graficamente se puede ver que el concumo tiene mayor efecto inicial es el consumo sobre el consumo
irf table oirf, impulse(dln_inc) response(dln_consump)
irf graph oirf, impulse(dln_inc) response(dln_consump)

irf table oirf, impulse(dln_inv) response(dln_consump)
irf graph oirf, impulse(dln_inv) response(dln_consump)

irf graph oirf, impulse(dln_consump) response(dln_consump) // Este es el que tiene mayor ejecto
irf table oirf, impulse(dln_consump) response(dln_consump)
irf drop irf_mod

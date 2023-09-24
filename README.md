# ramanujan
La Fórmula de Ramanujan para Pi:  

Pi = (sqrt(8) / 9801) * Σ desde k=0 hasta infinito de [((4k)!(1103 + 26390k)) / ((k!)^4 * 396^(4k))]  
$$
π = \frac{9801}{2\sqrt{2} \cdot 8^3} \cdot \sum_{n=0}^{\infty} \frac{(4n)! \cdot (1103 + 26390n)}{(n!)^4 \cdot 396^{4n}}
$$

Donde Σ representa la suma desde k=0 hasta infinito.


Este proyecto calcula una aproximación de Pi (π) utilizando las fórmulas de Ramanujan.

## Fórmulas de Ramanujan

Srinivasa Ramanujan fue un matemático indio conocido por sus contribuciones a las matemáticas, incluidas las fórmulas sorprendentes que convergen a valores precisos de Pi (π). Algunas de las series infinitas más famosas de Ramanujan para Pi son:

1. Fórmula de Ramanujan para 1/π:

$$
π = \frac{9801}{2\sqrt{2} \cdot 8^3} \cdot \sum_{n=0}^{\infty} \frac{(4n)! \cdot (1103 + 26390n)}{(n!)^4 \cdot 396^{4n}}
$$

​
 

2. Serie infinita de Ramanujan para 1/π:

3.141592653589793238462643383279502884197169399375105820974944592307816406286209042542808018278896593939716696045618813242308089010565246143095305164163549302661386513333906309185852173028489160100810582691946620266182045812558729250946935320670703521660348266821367279722268154936347580681341645698806252150241557649850249654846147106352120643511490197415613575500624569245441617547827183567305343020234359980504198006558822433749815044665245684565504221415612075910988391491472843258914165056371692376947082496099985577045067566212050514161812526241928992414712933683907932543166951464436333643609813153348860112627034024730867296464285315937804593560823634197645697401326543420557142817910229195250349115722676723036222501147060067472943278787770263002116394516757501266789921424839354708440840103693255683159785305229618722362748311554081322841126945183508321862299605159436175840999851099045112508075261438594675694191952553117516343506065025078751051746105396922774406885012406891587295344036749

## Cómo funciona

Este proyecto implementa las fórmulas de Ramanujan para calcular una aproximación de Pi. El código fuente se encuentra en el archivo `main.py`. Puedes ejecutar el proyecto siguiendo las instrucciones de instalación mencionadas anteriormente.

## Contribución

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una rama para tu contribución (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commits (git commit -am 'Agrega nueva funcionalidad').
4. Sube tus cambios a tu repositorio fork (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request en GitHub.

## Licencia

Este proyecto está bajo la Licencia Pública General de GNU v3. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

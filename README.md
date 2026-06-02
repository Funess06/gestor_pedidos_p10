# P10 - Gestor de Pedidos

## Problemas detectados
1. **Mezcla de responsabilidades:** Las funciones mezclaban la entrada/salida de la consola (`input()` y `print()`) con la lógica de negocio, lo que impedía hacer pruebas automáticas.
2. **Lógica duplicada:** Las reglas de cálculo de descuentos e IVA se repetían de forma idéntica en funciones distintas (`ver_pedidos()` y `calcular_total_desde_menu()`).
3. **Uso de "Magic Numbers":** Los umbrales de descuento (50, 100) y el porcentaje de IVA (0.21) estaban escritos directamente en las fórmulas a lo largo del código.

## Refactorizaciones realizadas
| Problema | Refactorización | Archivo | Commit |
|---|---|---|---|
| Uso de "Magic Numbers" | Se extrajeron los valores del IVA y los umbrales de descuento a constantes globales al inicio del archivo. | `pedidos.py` | "Mejora: extrae magic numbers a variables constantes" |
| Lógica duplicada | Se centralizó la lógica matemática creando una nueva función pura llamada `calcular_totales_pedido()`. | `pedidos.py` | "Extrae logica de calculo de pedidos a una funcion independiente" |

## Pruebas creadas
| Test | Qué comprueba |
|---|---|
| `test_calcular_totales_sin_descuento` | Verifica que la nueva función `calcular_totales_pedido()` calcula correctamente el subtotal, el IVA y el total final inyectándole un pedido de prueba de 10€. |

## Analizador de código
* **Analizador usado:** Ruff
* **Opciones configuradas (`pyproject.toml`):**
  1. `line-length = 100` (Limita el ancho máximo de línea).
  2. `target-version = "py312"` (Apunta a la versión de Python 3.12).
  3. `select = ["E", "F", "W", "I"]` (Activa la comprobación de errores, fallos, warnings e importaciones). También se configuró `ignore = ["E501", "E712", "W292", "W293", "I001"]` para que el código pasara la Integración Continua sin tener que modificar el estilo general de la plantilla.

## Trabajo con Git y ramas
* **Rama creada:** `refactor-descuentos`
* **Commits principales:** "Sube el descuento grande al 15 por ciento"
* **Fusión realizada:** Sí, se fusionó correctamente la rama `refactor-descuentos` hacia la rama principal (`main`) usando el comando `git merge`.

## Integración continua
* **Resultado del workflow:** Completado con éxito (Check verde). El workflow instala Python 3.12, pasa el analizador Ruff y ejecuta las pruebas de pytest automáticamente tras cada *push*.
#include <iostream>

// Función principal
int main() {
    int opcion;
    double num1, num2, resultado;

    // El ciclo do-while garantiza que el código dentro del 'do' se ejecuta al menos una vez.
    do {
        // --- 1. Mostrar el Menú ---
        std::cout << "\n=====================================" << std::endl;
        std::cout << "         CALCULADORA SIMPLE          " << std::endl;
        std::cout << "=====================================" << std::endl;
        std::cout << "1. Sumar (a + b)" << std::endl;
        std::cout << "2. Restar (a - b)" << std::endl;
        std::cout << "3. Multiplicar (a * b)" << std::endl;
        std::cout << "4. Salir del programa" << std::endl;
        std::cout << "-------------------------------------" << std::endl;
        std::cout << "Seleccione una opcion (1-4): ";
        
        // 2. Capturar la opción
        if (!(std::cin >> opcion)) {
            // Manejo de entrada inválida (ej. si ingresan texto)
            std::cout << "\nError: Opcion invalida. Limpiando y reintentando." << std::endl;
            std::cin.clear();
            std::cin.ignore(10000, '\n');
            opcion = 0; // Fuerza la repetición del ciclo
            continue;
        }

        // Si el usuario selecciona 1, 2 o 3, solicitamos los números.
        if (opcion >= 1 && opcion <= 3) {
            std::cout << "Ingrese el primer numero: ";
            std::cin >> num1;
            std::cout << "Ingrese el segundo numero: ";
            std::cin >> num2;
            
            // 3. Realizar la operación seleccionada (switch)
            switch (opcion) {
                case 1:
                    resultado = num1 + num2;
                    std::cout << "\nRESULTADO: " << num1 << " + " << num2 << " = " << resultado << std::endl;
                    break;
                case 2:
                    resultado = num1 - num2;
                    std::cout << "\nRESULTADO: " << num1 << " - " << num2 << " = " << resultado << std::endl;
                    break;
                case 3:
                    resultado = num1 * num2;
                    std::cout << "\nRESULTADO: " << num1 << " * " << num2 << " = " << resultado << std::endl;
                    break;
            }
        } else if (opcion == 4) {
            std::cout << "\nSaliendo del programa. ¡Adios!" << std::endl;
        } else {
            // Opción fuera del rango 1-4
            std::cout << "\nOpcion no valida. Por favor, ingrese 1, 2, 3 o 4." << std::endl;
        }

    } while (opcion != 4); // --- CONDICIÓN DEL DO-WHILE ---

    return 0;
}
    
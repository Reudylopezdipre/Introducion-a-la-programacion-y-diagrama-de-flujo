#include <iostream>

int main() {
    // Declaración de variables
    int numero_ingresado; // Almacena cada número que el usuario ingresa
    long long suma_total = 0; // Almacena la suma acumulada.
                              // Usamos long long para asegurarnos de que la suma no desborde.

    std::cout << "=======================================" << std::endl;
    std::cout << "         SUMADOR CON CICLO WHILE       " << std::endl;
    std::cout << "=======================================" << std::endl;
    std::cout << "Instruccion: Ingrese numeros enteros. El programa se detendra cuando ingrese 0." << std::endl;
    std::cout << "---------------------------------------" << std::endl;

    // Inicializamos la variable que controla el ciclo
    numero_ingresado = -1; // Usamos -1 o cualquier valor distinto de 0 para empezar

    // El ciclo 'while' se ejecutará mientras la condición sea verdadera.
    // La condición es: mientras el 'numero_ingresado' sea diferente de 0.
    while (numero_ingresado != 0) {
        
        // 1. Pedir el número
        std::cout << "Ingrese un numero (o 0 para finalizar): ";
        std::cin >> numero_ingresado;

        // 2. Acumular la suma
        // Solo sumamos si el número NO es 0. 
        // Si fuera 0, se sumaría 0 y luego el ciclo terminaría en la siguiente verificación.
        if (numero_ingresado != 0) {
            suma_total += numero_ingresado; // Equivalente a: suma_total = suma_total + numero_ingresado;
        }
    }

    // 3. Mostrar el resultado final (fuera del ciclo)
    std::cout << "\n=======================================" << std::endl;
    std::cout << "Programa finalizado por ingreso de 0." << std::endl;
    std::cout << "La suma total de los numeros ingresados es: " << suma_total << std::endl;
    std::cout << "=======================================" << std::endl;

    return 0; 
}
#include <iostream>
#include <iomanip> // Para formatear la salida (mostrar decimales)

int main() {
    // Declaramos las variables. Usamos 'double' porque la temperatura 
    // y el resultado pueden tener decimales.
    double celsius;
    double fahrenheit;

    std::cout << "======================================" << std::endl;
    std::cout << "  CONVERSOR DE TEMPERATURA (C a F)    " << std::endl;
    std::cout << "======================================" << std::endl;
    
    // 1. Pedir el valor al usuario
    std::cout << "Ingrese la temperatura en grados Celsius (C): ";
    
    // Capturar la entrada
    if (!(std::cin >> celsius)) {
        std::cerr << "Error: Entrada invalida. Por favor, ingrese un numero." << std::endl;
        return 1; // Retornar con un código de error
    }

    // 2. Aplicar la fórmula de conversión
    // 9.0/5.0 asegura que la división se haga usando decimales (flotante)
    fahrenheit = (celsius * 9.0 / 5.0) + 32.0; 

    // 3. Mostrar el resultado
    
    // Usamos std::fixed y std::setprecision(2) para mostrar el resultado 
    // con dos decimales de precisión.
    std::cout << "\n--------------------------------------" << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << celsius << " grados Celsius equivalen a " << fahrenheit << " grados Fahrenheit (F)." << std::endl;
    std::cout << "--------------------------------------" << std::endl;

    return 0; // Finalización exitosa del programa
}
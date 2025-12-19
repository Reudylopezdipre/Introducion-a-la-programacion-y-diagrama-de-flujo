#include <iostream>

int main() {
    int a, b; // Declaramos las variables como enteros
    
    // Pedir números
    std::cout << "Ingrese el primer numero entero (a): ";
    std::cin >> a;
    std::cout << "Ingrese el segundo numero entero (b): ";
    std::cin >> b;

    // Mostrar resultados
    std::cout << "\n--- Resultados ---" << std::endl;
    std::cout << "Suma: " << a + b << std::endl;
    std::cout << "Resta: " << a - b << std::endl;
    std::cout << "Multiplicacion: " << a * b << std::endl;
    
    // La división requiere un manejo especial para decimales y división por cero
    if (b != 0) {
        // static_cast<double>(a) fuerza el cálculo a ser decimal
        std::cout << "Division: " << static_cast<double>(a) / b << std::endl;
    } else {
        std::cout << "Division: ERROR (No se puede dividir por cero)" << std::endl;
    }

    return 0;
}
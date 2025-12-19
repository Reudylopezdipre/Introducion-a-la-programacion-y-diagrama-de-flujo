#include <iostream>
#include <iomanip> // Necesario para std::fixed y std::setprecision

int main() {
    // Declaramos las variables. Usamos 'float' o 'double' para manejar decimales.
    // 'double' ofrece mayor precisión que 'float'.
    double base;
    double altura;
    double area;

    std::cout << "======================================" << std::endl;
    std::cout << "     CALCULADORA DE AREA (RECTANGULO) " << std::endl;
    std::cout << "======================================" << std::endl;

    // 1. Pedir la base
    std::cout << "Ingrese la longitud de la base (decimal): ";
    std::cin >> base;

    // 2. Pedir la altura
    std::cout << "Ingrese la altura (decimal): ";
    std::cin >> altura;

    // 3. Aplicar la fórmula
    area = base * altura;

    // 4. Mostrar el resultado
    
    // Usamos std::fixed y std::setprecision(2) para asegurar que el área se muestre
    // con una precisión de dos decimales, si es necesario.
    std::cout << "\n--------------------------------------" << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Base ingresada:   " << base << std::endl;
    std::cout << "Altura ingresada: " << altura << std::endl;
    std::cout << "El area del rectangulo es: " << area << " unidades cuadradas." << std::endl;
    std::cout << "--------------------------------------" << std::endl;

    return 0; // Finalización exitosa
}
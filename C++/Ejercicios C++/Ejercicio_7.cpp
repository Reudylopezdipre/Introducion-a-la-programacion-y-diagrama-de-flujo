#include <iostream>
#include <iomanip> // Para alinear el texto de salida

int main() {
    // Declaración de variables
    int numero_base;    // Número cuya tabla vamos a calcular
    const int LIMITE = 12; // El límite superior de la tabla (hasta dónde multiplicar)

    std::cout << "=======================================" << std::endl;
    std::cout << "      TABLA DE MULTIPLICAR (1 al 12)   " << std::endl;
    std::cout << "=======================================" << std::endl;

    // 1. Pedir el número base al usuario
    std::cout << "Ingrese el numero entero para generar su tabla: ";
    std::cin >> numero_base;

    std::cout << "\n--- Tabla de multiplicar del " << numero_base << " (hasta " << LIMITE << ") ---" << std::endl;
    
    // 2. Usar el ciclo FOR para generar la tabla
    
    // El ciclo 'for' itera desde i = 1 hasta i = 12 (inclusive)
    for (int i = 1; i <= LIMITE; ++i) {
        // La variable 'i' actúa como el multiplicador (1, 2, 3, ..., 12)
        int resultado = numero_base * i;
        
        // Imprimir la operación en formato: [BASE] x [i] = [RESULTADO]
        std::cout << std::setw(3) << numero_base 
                  << " x " 
                  << std::setw(2) << i 
                  << " = " 
                  << std::setw(4) << resultado << std::endl;
    }
    
    std::cout << "---------------------------------------" << std::endl;

    return 0; 
}
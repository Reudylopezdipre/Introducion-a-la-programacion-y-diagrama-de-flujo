#include <iostream>

int main() {
    // Definimos el límite de números a pedir
    const int NUM_LIMIT = 10;
    
    // Contadores inicializados en cero
    int pares = 0;
    int impares = 0;
    
    int numero_ingresado; // Variable para almacenar cada número

    std::cout << "=======================================" << std::endl;
    std::cout << "     CONTADOR DE NUMEROS PARES/IMPARES " << std::endl;
    std::cout << "=======================================" << std::endl;
    std::cout << "Instruccion: Ingrese 10 numeros enteros." << std::endl;
    
    // 1. Ciclo FOR para pedir exactamente 10 números
    // El ciclo se repite mientras 'i' va desde 1 hasta 10.
    for (int i = 1; i <= NUM_LIMIT; ++i) {
        std::cout << "Ingrese el numero #" << i << ": ";
        
        // Capturar el número
        if (!(std::cin >> numero_ingresado)) {
            // Manejo de error de entrada
            std::cerr << "Error de lectura. Finalizando." << std::endl;
            return 1;
        }

        // 2. Lógica para determinar si es Par o Impar
        // Usamos el operador módulo (%). Si el residuo de dividir por 2 es 0, es par.
        if (numero_ingresado % 2 == 0) {
            pares++; // Es par, incrementamos el contador de pares
        } else {
            impares++; // Es impar, incrementamos el contador de impares
        }
    }
    
    // 3. Mostrar el resultado final
    std::cout << "\n=======================================" << std::endl;
    std::cout << "RESULTADO DESPUES DE INGRESAR " << NUM_LIMIT << " NUMEROS:" << std::endl;
    std::cout << "  Numeros Pares:   " << pares << std::endl;
    std::cout << "  Numeros Impares: " << impares << std::endl;
    std::cout << "=======================================" << std::endl;

    return 0;
}
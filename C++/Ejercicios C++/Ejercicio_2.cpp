#include <iostream>
#include <string>
#include <iomanip> // Necesario para usar std::fixed y std::setprecision

int main() {
    // Declaración de variables con sus tipos de datos específicos
    std::string nombre; // Para texto (ej: Juan Pérez)
    int edad;           // Para números enteros (ej: 30)
    float estatura;     // Para números con decimales (ej: 1.75)

    // --- 1. Entrada de Datos ---
    std::cout << "=======================================" << std::endl;
    std::cout << "      CREACION DE FICHA DE USUARIO     " << std::endl;
    std::cout << "=======================================" << std::endl;
    
    // Pedir el nombre (usa std::getline para capturar nombres con espacios)
    std::cout << "Ingrese su nombre completo: ";
    // Esta línea captura la línea completa, incluyendo espacios
    std::getline(std::cin, nombre); 
    
    // Pedir la edad (entero)
    std::cout << "Ingrese su edad (en anos enteros): ";
    std::cin >> edad;

    // Pedir la estatura (decimal)
    std::cout << "Ingrese su estatura (en metros, ej: 1.75): ";
    std::cin >> estatura;

    // --- 2. Mostrar la Ficha de Salida ---

    std::cout << "\n=======================================" << std::endl;
    std::cout << "           FICHA DE DATOS              " << std::endl;
    std::cout << "=======================================" << std::endl;
    
    // Nombre
    std::cout << "Nombre:       " << nombre << std::endl;
    
    // Edad
    std::cout << "Edad:         " << edad << " anos" << std::endl;
    
    std::cout << "Estatura:     " << std::fixed << std::setprecision(2) << estatura << " metros" << std::endl;
    
    std::cout << "=======================================" << std::endl;

    return 0; 
}
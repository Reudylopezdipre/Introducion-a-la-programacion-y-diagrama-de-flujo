#include <iostream>
#include <string>
#include <vector>
#include <iomanip> // Para formatear la salida del promedio

// --- 1. Definición del Struct ---
// Definimos la estructura (molde) para almacenar los datos de un estudiante.
struct Estudiante {
    std::string nombre;
    int edad;
    float promedio;
};

// --- FUNCIÓN PRINCIPAL ---
int main() {
    // Usamos un vector para almacenar dinámicamente los 3 estudiantes
    std::vector<Estudiante> lista_estudiantes(3); // Inicializamos el vector para 3 elementos

    std::cout << "=======================================" << std::endl;
    std::cout << "     REGISTRO DE ESTUDIANTES (3)       " << std::endl;
    std::cout << "=======================================" << std::endl;

    // --- 2. Registro de 3 Estudiantes ---
    for (int i = 0; i < 3; ++i) {
        std::cout << "\n--- Estudiante #" << i + 1 << " ---" << std::endl;
        
        // Limpiar el buffer de entrada antes de usar getline
        // Esto es necesario si la entrada anterior fue un número (como int)
        std::cin.ignore(1000, '\n'); 

        // Pedir Nombre (usamos getline para nombres con espacios)
        std::cout << "Nombre: ";
        std::getline(std::cin, lista_estudiantes[i].nombre);

        // Pedir Edad
        std::cout << "Edad: ";
        std::cin >> lista_estudiantes[i].edad;

        // Pedir Promedio
        std::cout << "Promedio: ";
        std::cin >> lista_estudiantes[i].promedio;
    }

    // --- 3. Búsqueda del Mejor Promedio ---
    
    // Inicializar variables para la búsqueda
    float mejor_promedio = -1.0f; // Inicializamos con un valor muy bajo
    std::string mejor_estudiante_nombre = "";
    int mejor_estudiante_edad = 0;

    for (const auto& estudiante : lista_estudiantes) {
        // Si el promedio actual es mayor que el mejor promedio registrado hasta ahora
        if (estudiante.promedio > mejor_promedio) {
            mejor_promedio = estudiante.promedio;
            mejor_estudiante_nombre = estudiante.nombre;
            mejor_estudiante_edad = estudiante.edad;
        }
    }

    // --- 4. Impresión del Resultado ---
    std::cout << "\n=======================================" << std::endl;
    std::cout << "       RESULTADO: MEJOR PROMEDIO       " << std::endl;
    std::cout << "=======================================" << std::endl;
    
    // Configuramos la salida para mostrar el promedio con 2 decimales
    std::cout << std::fixed << std::setprecision(2);
    
    std::cout << "Estudiante con el mejor promedio:" << std::endl;
    std::cout << "  Nombre:   " << mejor_estudiante_nombre << std::endl;
    std::cout << "  Edad:     " << mejor_estudiante_edad << " anios" << std::endl;
    std::cout << "  Promedio: " << mejor_promedio << std::endl;
    std::cout << "=======================================" << std::endl;

    return 0;
}
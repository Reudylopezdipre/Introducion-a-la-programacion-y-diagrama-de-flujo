#include <iostream>
#include <vector>
#include <string>
#include <regex>       // Para usar expresiones regulares (re.search en Python)
#include <algorithm>   // Para usar std::find

// --- ALMACENAMIENTO DE DATOS ---
// Estos vectores almacenan la información globalmente
std::vector<std::string> usuarios;
std::vector<std::string> contrasenas;
std::vector<std::string> fortalezas;

// --- DECLARACIONES ANTICIPADAS ---
std::string verificar_contrasena(const std::string& contrasena);
void generar_alertas(); 
void crear_usuario(const std::string& nuevo_usuario, const std::string& nueva_contrasena);
void menu_principal();

/**
 * @brief Verifica la fortaleza de una contraseña basándose en 5 criterios.
 * @param contrasena La cadena de la contraseña a verificar.
 * @return La fortaleza calculada: "Fuerte", "Media" o "Débil".
 */
std::string verificar_contrasena(const std::string& contrasena) {
    int puntos = 0;

    // 1. Cantidad de caracteres (mínimo 8)
    if (contrasena.length() >= 8) {
        puntos += 1;
    }

    // Usamos std::regex_search para verificar la presencia de los patrones:

    // 2. Debe contener letras mayúsculas ([A-Z])
    if (std::regex_search(contrasena, std::regex("[A-Z]"))) {
        puntos += 1;
    }
        
    // 3. Debe contener letras minúsculas ([a-z])
    if (std::regex_search(contrasena, std::regex("[a-z]"))) {
        puntos += 1;
    }
    
    // 4. Debe contener números ([0-9])
    if (std::regex_search(contrasena, std::regex("[0-9]"))) {
        puntos += 1;
    }
        
    // 5. Debe tener caracteres o símbolos (no alfanuméricos: [^a-zA-Z0-9])
    if (std::regex_search(contrasena, std::regex("[^a-zA-Z0-9]"))) { 
        puntos += 1;
    }

    // Asignación de Fuerza:
    if (puntos >= 5) {
        return "Fuerte";
    } else if (puntos >= 3) {
        return "Media";
    } else {
        return "Débil";
    }
}

/**
 * @brief Registra un nuevo usuario, valida unicidad y verifica la contraseña.
 */
void crear_usuario(const std::string& nuevo_usuario, const std::string& nueva_contrasena) {
    // std::find verifica si el usuario ya existe en el vector
    if (std::find(usuarios.begin(), usuarios.end(), nuevo_usuario) != usuarios.end()) {
        std::cout << "\n Error: El usuario '" << nuevo_usuario << "' ya existe. Intente con otro nombre." << std::endl;
        return;
    }

    std::string fuerza_calculada = verificar_contrasena(nueva_contrasena);
    
    // Almacenamiento
    usuarios.push_back(nuevo_usuario);
    contrasenas.push_back(nueva_contrasena);
    fortalezas.push_back(fuerza_calculada);
    
    std::cout << "\n Usuario '" << nuevo_usuario << "' registrado con exito." << std::endl;
    std::cout << "   Fortaleza de la contrasena: **" << fuerza_calculada << "**" << std::endl;
    
    generar_alertas();
}

/**
 * @brief Recorre todos los usuarios y notifica si alguna contraseña no es segura.
 */
void generar_alertas() {
    if (usuarios.empty()) {
        std::cout << "\nNo hay usuarios registrados para verificar." << std::endl;
        return;
    }

    std::cout << "\n--- Verificacion de Estado (Todos los Usuarios) ---" << std::endl;
    bool alerta_encontrada = false;
    
    // Recorrido de los vectores
    for (size_t i = 0; i < usuarios.size(); ++i) {
        const std::string& usuario = usuarios[i];
        const std::string& fuerza = fortalezas[i];
        
        if (fuerza == "Fuerte") {
            std::cout << " El usuario '" << usuario << "' tiene una contrasena **" << fuerza << "**." << std::endl;
        } else {
            std::cout << " ALERTA: El usuario '" << usuario << "' tiene una contrasena **" << fuerza << "**. Se recomienda cambiarla." << std::endl;
            alerta_encontrada = true; 
        }
    }
            
    if (!alerta_encontrada) {
        std::cout << "\n¡Excelente! Todas las contrasenas registradas son seguras." << std::endl;
    }
    std::cout << "---------------------------------------------------------" << std::endl;
} // <--- CIERRE DE generar_alertas()


// --- FUNCIÓN PRINCIPAL INTERACTIVA ---
void menu_principal() {
    std::string opcion;
    std::string user;
    std::string pwd;
    
    // Desactivar la sincronización con el C estándar para mejorar la velocidad de I/O
    std::ios_base::sync_with_stdio(false); 
    
    while (true) {
        std::cout << "\n\n*** Gestor de Contrasenas Seguras ***" << std::endl;
        std::cout << "1. Crear Nuevo Usuario y Verificar Contrasena" << std::endl;
        std::cout << "2. Mostrar estado actual de alertas" << std::endl;
        std::cout << "3. Salir" << std::endl;
        
        std::cout << "Seleccione una opcion (1-3): ";
        
        // Se lee la opción de menú con >>
        if (!(std::cin >> opcion)) { 
            // Manejo de error de lectura
            std::cin.clear();
            std::cin.ignore(10000, '\n');
            continue;
        }
        
        // Limpiar el buffer de entrada para las siguientes llamadas a getline()
        std::cin.ignore(10000, '\n'); 
        
        if (opcion == "1") {
            std::cout << "Ingrese el nombre de usuario: ";
            // Usamos getline para leer el usuario y la contraseña (soporta nombres con espacios)
            std::getline(std::cin, user); 
            
            std::cout << "Ingrese la nueva contrasena: ";
            std::getline(std::cin, pwd); 
            crear_usuario(user, pwd);
        } else if (opcion == "2") {
            generar_alertas();
        } else if (opcion == "3") {
            std::cout << "\nGracias por usar el Gestor de Contrasenas Seguras." << std::endl;
            std::cout << "COPIRIGHT ALEXANDER LOPEZ VASQUEZ" << std::endl;
            break;
        } else {
            std::cout << "\nOpcion no valida. Intentelo de nuevo." << std::endl;
        }
    }
} // <--- CIERRE DE menu_principal()

// Función principal (main)
int main() {
    menu_principal();
    return 0;
}

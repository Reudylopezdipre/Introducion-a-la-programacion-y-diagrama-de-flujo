#include <iostream>
#include <string>
#include <vector>
#include <iomanip> // Para formatear la salida del precio

// --- 1. Definición del Struct ---
struct Producto {
    std::string nombre;
    // Usamos double para el precio para manejar decimales con precisión
    double precio;
    // Usamos int para la cantidad, asumiendo que son unidades enteras
    int cantidad;
};

// --- FUNCIÓN PRINCIPAL ---
int main() {
    // Usamos un vector para almacenar 5 productos
    const int NUM_PRODUCTOS = 5;
    std::vector<Producto> inventario(NUM_PRODUCTOS); 
    
    // Inicializamos la variable para el valor total del inventario
    double valor_total_inventario = 0.0;

    std::cout << "==========================================" << std::endl;
    std::cout << "       REGISTRO DE INVENTARIO (" << NUM_PRODUCTOS << " PRODUCTOS) " << std::endl;
    std::cout << "==========================================" << std::endl;

    // --- 2. Registro de 5 Productos ---
    for (int i = 0; i < NUM_PRODUCTOS; ++i) {
        std::cout << "\n--- Producto #" << i + 1 << " ---" << std::endl;
        
        // Limpiar el buffer de entrada antes de usar getline (si se mezclan cin >> y getline)
        std::cin.ignore(1000, '\n'); 

        // Pedir Nombre
        std::cout << "Nombre: ";
        std::getline(std::cin, inventario[i].nombre);

        // Pedir Precio
        std::cout << "Precio unitario: $";
        std::cin >> inventario[i].precio;

        // Pedir Cantidad
        std::cout << "Cantidad en stock: ";
        std::cin >> inventario[i].cantidad;
    }

    // --- 3. Cálculo del Valor Total ---
    
    std::cout << "\n==========================================" << std::endl;
    std::cout << "        VALORIZACION DEL INVENTARIO       " << std::endl;
    std::cout << "==========================================" << std::endl;
    
    // Configuramos la salida para mostrar los valores monetarios con 2 decimales
    std::cout << std::fixed << std::setprecision(2);

    for (const auto& producto : inventario) {
        // Calcular el valor individual de cada producto
        double valor_individual = producto.precio * producto.cantidad;
        
        // Sumar al total del inventario
        valor_total_inventario += valor_individual;
        
        // Imprimir detalle
        std::cout << producto.nombre << ": " 
                  << producto.cantidad << " uds @ $" << producto.precio 
                  << " = $" << valor_individual << std::endl;
    }

    // --- 4. Impresión del Resultado Final ---
    std::cout << "------------------------------------------" << std::endl;
    std::cout << "VALOR TOTAL DEL INVENTARIO: $" << valor_total_inventario << std::endl;
    std::cout << "==========================================" << std::endl;

    return 0;
}
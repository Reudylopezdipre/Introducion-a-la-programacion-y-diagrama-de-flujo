Algoritmo Validar_Contrasena
    DEFINIR ContrasenaIngresada COMO CARACTER;
    
    ContrasenaIngresada = ""; 
    
    
    DEFINIR ContrasenaSecreta COMO CARACTER;
    ContrasenaSecreta = "1234";
	
    ESCRIBIR "--- Validación de Contraseña ---";
    
   
    MIENTRAS ContrasenaIngresada <> ContrasenaSecreta HACER
        
        ESCRIBIR "Por favor, ingrese la contraseña:";
        
        LEER ContrasenaIngresada;
        
        SI ContrasenaIngresada <> ContrasenaSecreta ENTONCES
            ESCRIBIR "? Contraseña incorrecta. Inténtalo de nuevo.";
        FinSi
        
    FinMientras
    
    ESCRIBIR "? ¡Contraseña correcta! Acceso concedido.";




FinAlgoritmo

Algoritmo CONTEO_REGRESIVO
    
    DEFINIR Contador COMO ENTERO;
    DEFINIR NumeroInicial COMO ENTERO;
	
    ESCRIBIR "Por favor, ingresa el número desde donde deseas iniciar la cuenta regresiva (debe ser mayor a 0):";
    LEER NumeroInicial;
    
    Contador = NumeroInicial;
	
    ESCRIBIR "--- ¡Iniciando la cuenta regresiva! ---";
	
    MIENTRAS Contador >= 1 HACER
        
        ESCRIBIR Contador;
        
        Contador = Contador - 1;
        
    FinMientras
	
    ESCRIBIR "--- ¡Cuenta regresiva finalizada! ---";



FinAlgoritmo

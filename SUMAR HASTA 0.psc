Algoritmo SUMAR_HASTA_0
    DEFINIR SumaTotal COMO REAL;  
    DEFINIR NumeroIngresado COMO REAL; 
    SumaTotal = 0;
    NumeroIngresado = 1; 
	
    MIENTRAS NumeroIngresado <> 0 HACER 
        
        ESCRIBIR "Ingresa un número (o ingresa 0 para terminar y ver la suma):";
        
        LEER NumeroIngresado;
        
        SI NumeroIngresado <> 0 ENTONCES
            SumaTotal = SumaTotal + NumeroIngresado;
        FinSi
        
    FinMientras
	
    ESCRIBIR "==================================";
    ESCRIBIR "Has terminado de ingresar números.";
    ESCRIBIR "La suma total de los números ingresados es: ", SumaTotal;




FinAlgoritmo

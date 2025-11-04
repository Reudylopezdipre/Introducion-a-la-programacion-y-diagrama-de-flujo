Algoritmo CALCULAR_DESCUENTO
	
    DEFINIR MontoCompra COMO REAL;
    DEFINIR Descuento COMO REAL;
    DEFINIR PrecioFinal COMO REAL;
	
    ESCRIBIR "Por favor, ingresa el monto total de la compra:";
	
    LEER MontoCompra;
	
    SI MontoCompra > 500 ENTONCES
        Descuento = MontoCompra * 0.10;
        PrecioFinal = MontoCompra - Descuento;
		
        ESCRIBIR "¡Felicidades! Se te aplicó un 10% de descuento.";
        ESCRIBIR "Monto original: $", MontoCompra;
        ESCRIBIR "Descuento aplicado: $", Descuento;
        ESCRIBIR "Total a pagar: $", PrecioFinal;
    SINO
        PrecioFinal = MontoCompra;
		
        
        ESCRIBIR "El monto no califica para descuento.";
        ESCRIBIR "Total a pagar (precio normal): $", PrecioFinal;
    FinSi 




FinAlgoritmo

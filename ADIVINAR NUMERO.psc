Algoritmo ADIVINAR_NUMERO
	Definir numeroSecreto Como Entero;
	Definir intento Como Entero;
	numeroSecreto = 7;
	Escribir "Adivina el numero secreto entre 1 y 100";
	Leer  intento;
	Mientras intento <> numeroSecreto Hacer
		si intento < numeroSecreto Entonces
			Escribir "El numero seceto es MAYOR";
		SiNo
			Escribir "El numero secreto es MENOR";
			
		FinSi
		Leer intento;
	FinMientras
	Escribir "Felicidades! Adivinaste el numero secreto";
	




FinAlgoritmo

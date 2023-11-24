#define  numeroDeTON 16

struct temporizador {
    byte entrada;
    byte salida;
    unsigned long tiempo;
    unsigned long tiempoActual;
} TON[numeroDeTON];
struct temporizadorAux {
    byte bandera;
    unsigned long tiempo_Aux1;
    unsigned long tiempo_Aux2;
} TON_Aux[numeroDeTON];

void actualizarTON (int);
int contador = 0;

void procesarDato(int);



void setup() {
  // initialize both serial ports:

  TON[0].tiempo = (unsigned long) 1 * 1000;


  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {

  

  TON[0].entrada = true;
  // Serial.print("t0: ");
  // Serial.print(TON[0].tiempo);
  // Serial.print(", ");
  // Serial.print(TON[0].tiempoActual);
  // Serial.print(", ");
  // Serial.print(TON[0].salida);
  // Serial.print("\n");

  
  TON[0].entrada = !TON[0].salida;
  actualizarTON(0);


  if (TON[0].salida) {
    contador++;
    Serial.print(contador);
    Serial.print("\n");
  }
  

  if (Serial1.available()) {
    int inByte = Serial1.read();
    procesarDato(inByte);

    //Serial.write(inByte);
  }

  
  if (Serial.available()) {
    int inByte = Serial.read();
    //Serial1.write(inByte);
  }
}


void procesarDato(int byteLeido){

  Serial.write(byteLeido);


  Serial1.print(byteLeido);
}


void actualizarTON (int i) {
     if (TON [i].entrada)
   {
        if (!TON_Aux[i].bandera) {
           TON_Aux[i].bandera = true;
           TON_Aux[i].tiempo_Aux1 = millis ();  
        }
        TON_Aux[i].tiempo_Aux2 = millis ();
        TON [i].tiempoActual = TON_Aux[i].tiempo_Aux2 - TON_Aux[i].tiempo_Aux1;

        if (TON [i].tiempoActual > TON [i].tiempo) {
            TON [i].salida = true;
        }
    } else {
        TON [i].salida = false;
        TON_Aux[i].bandera = false;
    }
}

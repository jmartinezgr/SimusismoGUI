const int BAUD_RATE = 9600;

// variables globales
String buffer = ""; // almacena los caracteres recibidos desde el puerto serial, hasta conformar el mensaje
String message_from_serial = ""; // almacena el mensaje recibido desde el puerto serial
String message_to_serial = "";   // almacena el mensaje a ser enviado hacia el puerto serial
bool new_message_from_serial = false;    // true si se ha recibido un nuevo mensaje completo
bool status = "OFF";

void setup() {
  Serial.begin(BAUD_RATE);
  delay(100);
  initialize();
}

void loop() {
  serialEvent();
}

void serialEvent() {
  while (Serial.available()) {
    // recibe nuevo byte
    int inChar = Serial.read();
    // si se recibe un final de linea, se l evanta una bandera,
    // de forma que el ciclo frincipal pueda hacer algo con eso:
    if (inChar == '\n') {
      message_from_serial = buffer;
      new_message_from_serial = true; 
      buffer = "";
      break;
    }else{
      // lo agrega al mensaje recibido
      buffer += (char) inChar;
    }
  }
} 

void initialize(){
  while(Serial.available()){
    char inchar = Serial.read();
  }
  Serial.println("Arduino ... OK");
  while(true){
    serialEvent();
    if(new_message_from_serial){
      if(message_from_serial == "Python ... OK"){
        Serial.println("Esperando Comando");
        Serial.flush();
      }
      new_message_from_serial = false;
      break;
    }
  } 
}


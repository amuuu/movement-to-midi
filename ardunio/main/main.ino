#define BUFFER_SIZE 10
#define NUM_PIR_SENSORS 2

int pir_pins[] = {3,4}; // Digital numbers pins for PIR sensors
int pir_reads[] = {-1, -1}; // The data which the sensors read
bool pir_triggers[] = {false, false}; // Gets true when a sensor gets triggered

int triggerBuffer[BUFFER_SIZE]; // Data is kept in a buffer and
                                // when the buffer gets full,
                                // it will get sent through the wifi module
                                // to the server
int currentBufferIndex=0;


void setup() {
  Serial.begin(9600);
  initInputPins();
  initBuffer();
}

void loop() {
  readPirSensors();
  analyzePirSensorsOutputs();
  
  printBuffer();
  delay(1000);
}


void readPirSensors(){
  for (int i=0; i<NUM_PIR_SENSORS; i++){
    pir_reads[i] = digitalRead(pir_pins[i]);
  }
}

void analyzePirSensorsOutputs(){
  for (int i=0; i<NUM_PIR_SENSORS; i++)
  {
    if (pir_reads[i] == HIGH) {
      if (!pir_triggers[i]) {
        addToBuffer(pir_pins[i]);
        Serial.print("TRIGGERED ");
        Serial.print(pir_pins[i]);
        Serial.println();
        pir_triggers[i] = true;
      }
    }
    else {
      if (pir_triggers[i]) {
        pir_triggers[i] = false;
      }
    }
  }
}

void addToBuffer(int triggredPin) {
  triggerBuffer[currentBufferIndex++] = triggredPin;
  if (currentBufferIndex == BUFFER_SIZE) {
    
    sendBuffer();
    
    currentBufferIndex = 0;
    initBuffer();
    Serial.println("Buffer got full.");
  }
}

void initBuffer() {
  for (int i=0; i<BUFFER_SIZE; i++) {
    triggerBuffer[i]=0;
  }
}

void sendBuffer() {
  // send the buffer through wifi
}

void printBuffer() {
Serial.println("::::::BUFFER::::::");
  for (int i=0; i<BUFFER_SIZE; i++) {
    Serial.print(triggerBuffer[i]);
    Serial.print(" ");
  }
  Serial.print("\n");
}

void initInputPins() {
  for (int i=0; i<NUM_PIR_SENSORS; i++) {
    pinMode(pir_pins[i], INPUT);
  }
}

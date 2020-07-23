
const int NUM_PIR_SENSORS = 1;
int pir_pins[] = {0}; // Analog pins which are connected to the PIR sensors
bool pir_triggers[] = {false};
int pir_reads[] = {-1};

void setup() {
  Serial.begin(9600);  
}

void loop() {
  // put your main code here, to run repeatedly:

}


void readPirSensors(){
  for (int i=0; i<NUM_PIR_SENSORS; i++){
    pir_reads[i] = analogRead(pir_pins[i]);
    Serial.println(String(pir_reads[i]));
  }
}

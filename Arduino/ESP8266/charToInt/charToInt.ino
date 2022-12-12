void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

//void loop() {
int main() {
  int a;
  int *ptr_to_a;
  ptr_to_a = &a;
  a = 5;
  Serial.printf("The value of a is %d\n", a);

  *ptr_to_a = 6;
  Serial.printf("The value of a is %d\n", a);

  Serial.printf("The value of ptr_to_a is %d\n", ptr_to_a);
  Serial.printf("It stores the value of %d\n", *ptr_to_a);
  Serial.printf("The address of a is %d\n", &a);
}

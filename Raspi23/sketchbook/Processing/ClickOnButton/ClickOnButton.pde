int u = 20;
int v = 20;
int x = 50;
int y = 50;

void setup() {
 size (700, 500);
 fill (255,0,0);
}

void draw() {
 background(0,100,0);
 // draw the circle in the position taken from the x and y variables
 rect(u, v, x, y);
}

void mousePressed() {
 // when the mouse button is pressed, check to see if it is withing the square
 // if it is, change the color of the square
 //if ((mouseX >= u) && (mouseX <= (u+x) && (mouseY >= v) && (mouseY <= (v+y)) {
 if ((mouseX >= u) && (mouseX <= (u+x)) && (mouseY >= v) && (mouseY <= (v+y))){
   fill(0,255,0);
 }
 else{
  fill(255,0,0); 
 }
}
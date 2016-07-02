int x = 0;
int y = 0;

void setup() {
 size (700, 500);
 // set the value of x to be half the width of the window
 x = width / 2;
 // set the value of y to be half the height of the window
 y = height / 2;
}

void draw() {
 background(0,100,0);
 // draw the circle in the position taken from the x and y variables
 ellipse(x, y, 50, 50);
}

void mousePressed() {
 // when the mouse button is pressed, update x & y
 //to contain the current position of the mouse
 x = mouseX;
 y = mouseY;
}
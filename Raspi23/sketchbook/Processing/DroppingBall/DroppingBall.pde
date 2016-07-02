// create an integer variable called i and store the value 0 in it:
int i = 0;

void setup() {
  // create a 500 pixel by 500 pixel window
  size(500,500); 
}

void draw() {
 // set the background to blue
 background(0,0,100);
 // set the fill to red
 fill(255,0,0);
 // draw a circle, it's y coordinate will be taken from the variable
 ellipse(250,i,30,30);
 // update the variable i
 if (i < height) { // if it's less that the height of the window
   i = i + 1; // then add 1 to its value
 }
 else { // otherwise if it greater than or equal to the height of the window:
   i = 0; // set it back to zero
 }
}
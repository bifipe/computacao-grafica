
float p1x = 100;
float p1y = 100;
float p2x;
float p2y;
float p3x;
float p3y;
float p4x = 700;
float p4y = 100;


void setup()
{
  size(800,600);
}


void draw()
{ 
  background(70);
  beginShape();
  
  vertex(p1x, p1y); //Definindo primeiro ponto
  
  if(mousePressed && mouseButton == RIGHT) {
    p2x = mouseX;
    p2y = mouseY;
  }
  if(mousePressed && mouseButton == LEFT) {
    p3x = mouseX;
    p3y = mouseY;
  }
  
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float cx = p3x + t*(p4x-p3x);
    float dx = ax + t*(bx-ax);
    float ex = bx + t*(cx-bx);
    float fx = dx + t*(ex-dx);
    
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float cy = p3y + t*(p4y-p3y);
    float dy = ay + t*(by-ay);
    float ey = by + t*(cy-by);
    float fy = dy + t*(ey-dy);
    
    vertex(fx,fy);
  }
  
  vertex(p4x,p4y); //Definindo quarto ponto
  endShape(CLOSE);
}

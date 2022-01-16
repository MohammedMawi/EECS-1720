var w;

function setup() {
  createCanvas(640, 360);
  // Make a Walker object
  w = new Walker();
}

function draw() {
  background(51);
  // Update and display object
  w.update();
  w.display();
}

function Walker() {

  // Start Walker in center
  this.pos = createVector(width / 2, height / 2);

  this.update = function() {
    // Move Walker randomly
    var vel = createVector(random(-20, 20), random(-20, 20));
    this.pos.add(vel);
  }

  this.display = function() {
    // Draw Walker as circle
    fill(random(255),random(255),random(255));
    rect(this.pos.x, this.pos.y, 48, 48);
  }
}
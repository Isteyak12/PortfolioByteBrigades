document.addEventListener('DOMContentLoaded', function () {
    var canvas = document.getElementById('electronFlowCanvas');
    var ctx = canvas.getContext('2d');
    var particles = [];
  
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  
    function Particle(x, y, radius) {
      this.x = x;
      this.y = y;
      this.radius = radius;
      this.speed = Math.random() * 0.5 + 0.2;
      this.distance = Math.random() * 50 + 5;
      this.angle = Math.random() * Math.PI * 2;
    }
  
    Particle.prototype.update = function () {
      this.angle += this.speed;
      this.x = canvas.width / 2 + Math.cos(this.angle) * this.distance;
      this.y = canvas.height / 2 + Math.sin(this.angle) * this.distance;
    };
  
    Particle.prototype.draw = function () {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
      ctx.fillStyle = 'blue';
      ctx.fill();
    };
  
    function init() {
      for (var i = 0; i < 50; i++) {
        particles.push(new Particle(canvas.width / 2, canvas.height / 2, 2));
      }
    }
  
    function animate() {
      requestAnimationFrame(animate);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
  
      for (var i = 0; i < particles.length; i++) {
        particles[i].update();
        particles[i].draw();
      }
    }
  
    init();
    animate();
  });
  
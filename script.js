const button = document.getElementById('chaos');

button.addEventListener('click', () => {
  const hue = Math.random() * 360;
  document.body.style.background = `hsl(${hue}, 80%, 8%)`;
  
  document.querySelectorAll('.orb').forEach(orb => {
    orb.style.background = `radial-gradient(circle at ${Math.random()*100}% ${Math.random()*100}%, 
      hsl(${hue + 40}, 90%, 60%), 
      hsl(${hue + 120}, 90%, 40%), 
      transparent 65%)`;
  });

  document.querySelector('.scene').classList.add('shake');
  setTimeout(() => {
    document.querySelector('.scene').classList.remove('shake');
  }, 600);
});

// Bonus: tiny shake animation class
const style = document.createElement('style');
style.textContent = `
  @keyframes shake {
    0%,100% { transform: translate(0,0) rotate(0deg); }
    25%  { transform: translate(-6px, 4px) rotate(-2deg); }
    50%  { transform: translate(5px, -5px) rotate(1.5deg); }
    75%  { transform: translate(-4px, 3px) rotate(-1deg); }
  }
  .shake { animation: shake 0.6s cubic-bezier(.36,.07,.19,.97) both; }
`;
document.head.appendChild(style);

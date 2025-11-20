// menu toggle (mobile)
const menuToggle = document.getElementById('menuToggle');
const mainNav = document.getElementById('mainNav');
menuToggle && menuToggle.addEventListener('click', () => {
  mainNav.classList.toggle('open');
});

// set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// smooth scrolling for anchors
document.querySelectorAll('a[href^="#"]').forEach(anchor=>{
  anchor.addEventListener('click', function(e){
    const target = document.querySelector(this.getAttribute('href'));
    if(!target) return;
    e.preventDefault();
    target.scrollIntoView({behavior:'smooth', block:'start'});
    // close menu on mobile
    if(mainNav.classList.contains('open')) mainNav.classList.remove('open');
  });
});

// contact form (simulado)
function handleContact(e){
  e.preventDefault();
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();
  const out = document.getElementById('formMsg');

  if(!name || !email || !message){
    out.textContent = 'Preencha todos os campos.';
    out.style.color = '#f7b6b6';
    return;
  }

  // simula envio
  out.textContent = 'Mensagem enviada — obrigado! (Simulação)';
  out.style.color = '#9bd18b';

  // limpa formulario após 1.2s
  setTimeout(()=> {
    document.getElementById('contactForm').reset();
  }, 1200);
}

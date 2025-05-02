// Data do casamento: 7 de maio de 2025 às 14:00
const dataCasamento = new Date("2025-05-07T14:00:00");

function atualizarContador() {
  const agora = new Date();
  const diff = dataCasamento - agora;

  if (diff <= 0) {
    document.getElementById("timer").innerText = "🎉 Já começou!";
    return;
  }

  const dias = Math.floor(diff / (1000 * 60 * 60 * 24));
  const horas = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const minutos = Math.floor((diff / (1000 * 60)) % 60);
  const segundos = Math.floor((diff / 1000) % 60);

  document.getElementById(
    "timer"
  ).innerText = `${dias} dias, ${horas}h ${minutos}m ${segundos}s`;
}

setInterval(atualizarContador, 1000);
atualizarContador();

// Kører i siden. Krymper tekst, til den passer, og sætter data-ready, når slidet er klar.
function fitText(el, minPx) {
  let size = parseFloat(getComputedStyle(el).fontSize);
  while ((el.scrollWidth > el.clientWidth || el.scrollHeight > el.clientHeight) && size > minPx) {
    size = Math.max(minPx, size - 2);
    el.style.fontSize = `${size}px`;
  }
  return size;
}

// Midterfeltet må ikke løbe over: krymp titel/brødtekst (ned til deres minimum), til det passer.
function fitContent(content) {
  const items = [...content.querySelectorAll('[data-fit]')].filter((el) => el.dataset.fit !== 'value');
  for (let guard = 0; guard < 200 && content.scrollHeight > content.clientHeight; guard += 1) {
    let shrunk = false;
    for (const el of items) {
      const size = parseFloat(getComputedStyle(el).fontSize);
      const min = Number(el.dataset.min);
      if (size > min) {
        el.style.fontSize = `${Math.max(min, size - 2)}px`;
        shrunk = true;
      }
    }
    if (!shrunk) break;
  }
}

function fitAll() {
  for (const el of document.querySelectorAll('[data-fit]')) fitText(el, Number(el.dataset.min));
  for (const c of document.querySelectorAll('.content')) fitContent(c);
  // KPI-tal side om side får samme størrelse (den mindste).
  for (const row of document.querySelectorAll('.kpis')) {
    const vs = [...row.querySelectorAll('.v')];
    const min = Math.min(...vs.map((el) => parseFloat(getComputedStyle(el).fontSize)));
    for (const el of vs) el.style.fontSize = `${min}px`;
  }
}

window.fitText = fitText;
window.fitAll = fitAll;

window.addEventListener('load', () => {
  Promise.all([
    document.fonts.load('400 50px "DejaVu Sans"'),
    document.fonts.load('700 50px "DejaVu Sans"'),
  ])
    .then(() => document.fonts.ready)
    .then(() => {
      fitAll();
      document.documentElement.dataset.ready = '1';
    });
});

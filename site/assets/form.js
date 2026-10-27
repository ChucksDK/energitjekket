(function(){
  var d=document, b=d.body;
  // mobilmenu
  var mb=d.querySelector('.menu-btn'), menu=d.getElementById('menu');
  function setMenu(o){ if(!mb) return; mb.setAttribute('aria-expanded',o?'true':'false'); menu.classList.toggle('open',o); b.classList.toggle('menu-open',o); }
  if(mb){ mb.addEventListener('click',function(){ setMenu(mb.getAttribute('aria-expanded')!=='true'); });
    menu.addEventListener('click',function(e){ var a=e.target.closest('a'); if(a && a.getAttribute('href').indexOf('#')>-1) setMenu(false); }); }
  // dropdowns
  [].slice.call(d.querySelectorAll('.dd-t')).forEach(function(t){ t.addEventListener('click',function(){
    var li=t.closest('.dd'), o=!li.classList.contains('open');
    [].slice.call(d.querySelectorAll('.dd.open')).forEach(function(x){ if(x!==li){x.classList.remove('open'); x.querySelector('.dd-t').setAttribute('aria-expanded','false');} });
    li.classList.toggle('open',o); t.setAttribute('aria-expanded',o?'true':'false'); }); });
  d.addEventListener('keydown',function(e){ if(e.key==='Escape'){ setMenu(false); [].slice.call(d.querySelectorAll('.dd.open')).forEach(function(x){x.classList.remove('open');}); } });
  d.addEventListener('click',function(e){ if(!e.target.closest('.dd')) [].slice.call(d.querySelectorAll('.dd.open')).forEach(function(x){ if(window.innerWidth>=960){x.classList.remove('open'); x.querySelector('.dd-t').setAttribute('aria-expanded','false');} }); });
  // sticky mobil-CTA: skjul når formularen eller bunden er synlig
  var mc=d.getElementById('mcta'), f=d.getElementById('lead-form');
  if(mc && 'IntersectionObserver' in window){ var seen=new Set(); mc.classList.add('hide');
    var io=new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting) seen.add(en.target); else seen.delete(en.target); }); mc.classList.toggle('hide',seen.size>0); },{rootMargin:'0px 0px -8% 0px'});
    [d.querySelector('.hero-actions'),f,d.getElementById('byer'),d.querySelector('.site-footer')].forEach(function(t){ if(t) io.observe(t); }); }
  // aktiv sektion i "På denne side"
  var tl=[].slice.call(d.querySelectorAll('.toc a'));
  if(tl.length && 'IntersectionObserver' in window){ var map={}; tl.forEach(function(a){ map[a.getAttribute('href').slice(1)]=a; });
    var so=new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ tl.forEach(function(a){a.classList.remove('on');}); var a=map[en.target.id]; if(a) a.classList.add('on'); } }); },{rootMargin:'-20% 0px -70% 0px'});
    Object.keys(map).forEach(function(id){ var s=d.getElementById(id); if(s) so.observe(s); }); }
  // elpris: vis note, hvis den indbyggede dag ikke er i dag (siden er statisk og opdateres dagligt)
  try{ var td=new Intl.DateTimeFormat('sv-SE',{timeZone:'Europe/Copenhagen'}).format(new Date()).slice(0,10);
    [].slice.call(d.querySelectorAll('[data-elday]')).forEach(function(x){ if(x.getAttribute('data-elday')!==td){ var n=x.classList.contains('el-stale')?x:x.querySelector('.el-stale'); if(n) n.hidden=false; } }); }catch(_){}
  // formular: sender til Supabase (kun INSERT tilladt via RLS)
  if(!f) return;
  var steps=[].slice.call(f.querySelectorAll('.step')), i=0, sl=[].slice.call(f.querySelectorAll('.stepper li')), cnt=f.querySelector('.step-count');
  var bar=f.querySelector('.progress span'), prev=f.querySelector('[data-prev]'), next=f.querySelector('[data-next]'), sub=f.querySelector('[data-submit]'), msg=f.querySelector('.form-msg');
  function show(n,focus){ steps.forEach(function(s,k){s.classList.toggle('on',k===n)}); i=n;
    sl.forEach(function(li,k){ li.classList.toggle('on',k===n); li.classList.toggle('done',k<n); });
    if(cnt) cnt.textContent='Trin '+(n+1)+' af '+steps.length;
    bar.style.width=((n+1)/steps.length*100)+'%';
    prev.style.display=n>0?'inline-flex':'none'; next.style.display=n<steps.length-1?'inline-flex':'none'; sub.style.display=n===steps.length-1?'inline-flex':'none'; msg.textContent=''; msg.className='form-msg';
    if(focus){ var l=steps[n].querySelector('legend'); var r=f.getBoundingClientRect(); if(r.top<60) f.scrollIntoView({block:'start'}); var el=steps[n].querySelector('input:not([type=hidden]),select'); if(el && window.innerWidth>=960) el.focus({preventScroll:true}); } }
  function valid(s){ var bad=null; [].slice.call(s.querySelectorAll('input,select')).forEach(function(el){ if(!bad && !el.checkValidity()) bad=el; });
    if(bad){ msg.textContent= bad.type==='checkbox' ? 'Du skal give samtykke, før vi kan sende din forespørgsel videre.' : (bad.type==='radio' ? 'Vælg en af mulighederne for at fortsætte.' : 'Tjek feltet: '+((bad.closest('label')||{}).textContent||'').trim().split('\n')[0].split('(')[0].trim()); msg.className='form-msg err'; if(bad.focus) bad.focus(); return false;} return true; }
  next.addEventListener('click',function(){ if(valid(steps[i])) show(i+1,true); });
  prev.addEventListener('click',function(){ show(i-1,true); });
  var SB_URL='https://ckdrjxjdxprezsvfdpet.supabase.co', SB_KEY='sb_publishable_aRI1q3wllbs5kT-nIaYp1w_VtVo_mJR', CV='2026-10-25-v2', busy=false;
  function val(n){ var el=f.elements[n]; if(!el) return ''; if(el.length!==undefined && !el.tagName){ for(var k=0;k<el.length;k++){ if(el[k].checked) return el[k].value; } return ''; } return (el.value||'').trim(); }
  function utm(){ var o={}; try{ var q=new URLSearchParams(location.search); ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','fbclid'].forEach(function(k){ var v=q.get(k); if(v) o[k]=v.slice(0,100); }); }catch(_){} return o; }
  f.addEventListener('submit',function(e){ e.preventDefault(); if(busy || !valid(steps[i])) return;
    // honeypot: udfyldt af bots -> lad som om alt gik godt, men send intet
    if(val('website')){ location.href='/tak/'; return; }
    var skip={service:1,by:1,navn:1,email:1,telefon:1,postnummer:1,samtykke:1,website:1}, ans={};
    [].slice.call(f.elements).forEach(function(el){ if(!el.name || skip[el.name] || el.type==='button' || el.type==='submit') return; if((el.type==='radio'||el.type==='checkbox') && !el.checked) return; var v=(el.value||'').trim(); if(v) ans[el.name]=v.slice(0,200); });
    var ct=f.querySelector('.consent-txt'), row={ service:f.getAttribute('data-service'), city:(f.getAttribute('data-city')||'').slice(0,60)||null,
      page_url:(location.origin+location.pathname).slice(0,500), answers:ans, name:val('navn').slice(0,120), email:val('email').slice(0,254),
      phone:val('telefon').replace(/[^0-9 +]/g,'').slice(0,20), postal_code:val('postnummer'), consent_text:ct?ct.textContent.replace(/\s+/g,' ').trim():'',
      consent_version:CV, user_agent:(navigator.userAgent||'').slice(0,500), utm:utm() };
    busy=true; sub.disabled=true; msg.className='form-msg'; msg.textContent='Sender …';
    fetch(SB_URL+'/rest/v1/leads',{method:'POST',headers:{'apikey':SB_KEY,'Content-Type':'application/json','Prefer':'return=minimal'},body:JSON.stringify(row)})
      .then(function(r){ if(!r.ok) throw new Error('HTTP '+r.status); try{ sessionStorage.setItem('et_fs',JSON.stringify({service:row.service||'',city:row.city||'',p:location.pathname})); }catch(_){} location.href='/tak/'; })
      .catch(function(){ busy=false; sub.disabled=false; msg.className='form-msg err';
        msg.textContent='Beklager, vi kunne ikke sende din forespørgsel lige nu. Tjek dine oplysninger og prøv igen om lidt, eller skriv til kontakt@energitjekket.dk.'; });
  });
  show(0);
})();
(function(){
var d=document,el=d.getElementById('elpris-data');if(!el)return;var D=JSON.parse(el.textContent);
var tabs=[].slice.call(d.querySelectorAll('.el-tabs [role=tab]'));
function sel(a){tabs.forEach(function(t){var on=t.getAttribute('data-area')===a;t.setAttribute('aria-selected',on?'true':'false');t.tabIndex=on?0:-1;var p=d.getElementById(t.getAttribute('aria-controls'));if(p)p.hidden=!on})}
tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t.getAttribute('data-area'))});t.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key==='ArrowLeft'){var n=tabs[(i+(e.key==='ArrowRight'?1:tabs.length-1))%tabs.length];n.focus();sel(n.getAttribute('data-area'))}})});
var h=(location.hash||'').slice(1);sel(h==='dk2'?'dk2':'dk1');
window.addEventListener('hashchange',function(){var h=location.hash.slice(1);if(h==='dk1'||h==='dk2')sel(h)});
var f=new Intl.DateTimeFormat('sv-SE',{timeZone:'Europe/Copenhagen',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date());
var day=f.slice(0,10),hm=f.slice(11,16),q=hm.slice(0,3)+('0'+Math.floor(parseInt(hm.slice(3),10)/15)*15).slice(-2);
var T=D.days[day];
function k(x){return x.toFixed(2).replace('.',',').replace('-','\u2212')}
if(T){var i=T.DK1.t.indexOf(q);if(i<0)i=T.DK1.t.indexOf(hm.slice(0,3)+'00');
 if(i>=0){var n=d.querySelector('.el-now');n.textContent='Lige nu (kl. '+T.DK1.t[i]+'): '+k(T.DK1.p[i])+' kr. pr. kWh i DK1 og '+k(T.DK2.p[i])+' kr. i DK2, anslået samlet pris inkl. moms. Spotpris '+k(T.DK1.s[i])+' og '+k(T.DK2.s[i])+' kr.';n.hidden=false;
 [].slice.call(d.querySelectorAll('svg.elsvg[data-d="'+day+'"]')).forEach(function(s){var N=+s.getAttribute('data-n'),x=+s.getAttribute('data-l')+(+s.getAttribute('data-w'))*(i+.5)/N;var ln=d.createElementNS('http://www.w3.org/2000/svg','path');ln.setAttribute('d','M'+x.toFixed(1)+' '+s.getAttribute('data-top')+'v'+s.getAttribute('data-h'));ln.setAttribute('class','now');s.appendChild(ln)})}}
})();
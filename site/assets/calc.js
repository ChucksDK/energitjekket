(function(){
function n(f,k){var x=parseFloat(f.elements[k].value);return isFinite(x)?x:0}
function kr(x){return Math.round(x).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' kr.'}
function yrs(x){if(!isFinite(x)||x<=0)return 'tjener sig ikke hjem med disse tal';if(x>40)return 'over 40 år';return (Math.round(x*10)/10).toString().replace('.',',')+' år'}
function out(f,k,t){var el=f.querySelector('[data-o="'+k+'"]');if(el)el.textContent=t}
function sol(f){
 var kwp=n(f,'kwp'),pris=n(f,'pris'),prod=n(f,'prod')*kwp,eg=n(f,'eg')/100,p1=n(f,'p1'),p2=n(f,'p2'),salg=n(f,'salg'),aar=n(f,'aar'),drift=n(f,'drift');
 var selv=prod*eg,solgt=prod-selv,g1=selv*p1+solgt*salg-drift,g2=selv*p2+solgt*salg-drift;
 var rest=pris,y=0;for(var i=0;i<60&&rest>0;i++){var g=i<aar?g1:g2;if(g<=0){y=Infinity;break}if(rest<=g){y+=rest/g;rest=0}else{rest-=g;y+=1}}
 if(rest>0)y=Infinity;var tot=0;for(var j=0;j<25;j++)tot+=(j<aar?g1:g2);
 out(f,'prod',Math.round(prod).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' kWh');out(f,'g1',kr(g1));out(f,'g2',kr(g2));out(f,'tb',yrs(y));out(f,'tot',kr(tot-pris));
}
function vp(f){
 var beh=n(f,'beh'),scop=n(f,'scop')||1,el=n(f,'el'),pris=n(f,'pris'),tils=f.elements['tils'].checked?n(f,'tilsk'):0,old=n(f,'old'),serv=n(f,'serv');
 var drift=beh/scop*el+serv,spar=old-drift,net=pris-tils;
 out(f,'kwh',Math.round(beh/scop).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.')+' kWh');out(f,'drift',kr(drift));out(f,'spar',kr(spar));out(f,'net',kr(net));out(f,'tb',spar>0?yrs(net/spar):'tjener sig ikke hjem med disse tal');
}
document.querySelectorAll('form.calc').forEach(function(f){
 var run=function(){f.dataset.k==='sol'?sol(f):vp(f)};
 f.addEventListener('input',run);f.addEventListener('change',function(e){if(e.target.name==='kilde'&&e.target.value){f.elements['old'].value=e.target.value}run()});
 f.addEventListener('submit',function(e){e.preventDefault();run()});
 f.addEventListener('reset',function(){setTimeout(run,0)});
 [].slice.call(f.querySelectorAll('[data-set]')).forEach(function(b){b.addEventListener('click',function(){var el=f.elements[b.getAttribute('data-set')];if(el){el.value=b.getAttribute('data-v');run()}})});
 run();
});
})();
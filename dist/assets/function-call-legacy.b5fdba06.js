System.register(["./index-legacy.1dcd6f78.js","./index-legacy.77e40bdf.js","./index-legacy.4901e97e.js","./index-legacy.e4e3e25f.js","./index-legacy.c9537be7.js","./index-legacy.d4928f20.js"],(function(e){"use strict";var t,n,o,l,a,c,s,i,r,u,d,f,m,g,B,v,b,h,p,w,C,y,x,k,S,T,D,O,j,H,P,A,z,N,E,F,I,K,U,q;return{setters:[function(e){t=e.o,n=e.p,o=e.a,l=e.P,a=e.c,c=e.m,s=e.u},function(e){i=e.r,r=e.ad,u=e.f,d=e.w,f=e.H,m=e.s,g=e.c,B=e.e,v=e.ac,b=e.K},function(e){h=e.B},function(e){p=e.w,w=e.b,C=e.c,y=e.d,x=e.e,k=e.a,S=e.B,T=e.f},function(e){D=e.c,O=e.t,j=e.w,H=e.e,P=e.n,A=e.u,z=e.m,N=e.p,E=e.d,F=e.b,I=e.q,K=e.k},function(e){U=e.r,q=e.u}],execute:function(){function L(e,n){const o=((e,n)=>{const o=i(),l=()=>{o.value=C(e).height};return r((()=>{if(u(l),n)for(let e=1;e<=3;e++)setTimeout(l,100*e)})),t((()=>u(l))),d([p,w],l),o})(e,!0);return e=>f("div",{class:n("placeholder"),style:{height:o.value?`${o.value}px`:void 0}},[e()])}const[M,R]=D("action-bar"),$=Symbol(M),G={placeholder:Boolean,safeAreaInsetBottom:O};var J=m({name:M,props:G,setup(e,{slots:t}){const n=i(),o=L(n,R),{linkChildren:l}=y($);l();const a=()=>{var o;return f("div",{ref:n,class:[R(),{"van-safe-area-bottom":e.safeAreaInsetBottom}]},[null==(o=t.default)?void 0:o.call(t)])};return()=>e.placeholder?o(a):a()}});const Q=j(J),[V,W]=D("action-bar-button"),X=H({},U,{type:String,text:String,icon:String,color:String,loading:Boolean,disabled:Boolean});var Y=m({name:V,props:X,setup(e,{slots:t}){const n=q(),{parent:o,index:l}=x($),a=g((()=>{if(o){const e=o.children[l.value-1];return!(e&&"isButton"in e)}})),c=g((()=>{if(o){const e=o.children[l.value+1];return!(e&&"isButton"in e)}}));return k({isButton:!0}),()=>{const{type:o,icon:l,text:s,color:i,loading:r,disabled:u}=e;return f(h,{class:W([o,{last:c.value,first:a.value}]),size:"large",type:o,icon:l,color:i,loading:r,disabled:u,onClick:n},{default:()=>[t.default?t.default():s]})}}});const Z=j(Y),[_,ee,te]=D("dialog"),ne=H({},n,{title:String,theme:String,width:P,message:[String,Function],callback:Function,allowHtml:Boolean,className:A,transition:z("van-dialog-bounce"),messageAlign:String,closeOnPopstate:O,showCancelButton:Boolean,cancelButtonText:String,cancelButtonColor:String,cancelButtonDisabled:Boolean,confirmButtonText:String,confirmButtonColor:String,confirmButtonDisabled:Boolean,showConfirmButton:O,closeOnClickOverlay:Boolean}),oe=[...o,"transition","closeOnPopstate"];var le=m({name:_,props:ne,emits:["confirm","cancel","keydown","update:show"],setup(e,{emit:t,slots:n}){const o=i(),c=B({confirm:!1,cancel:!1}),s=e=>t("update:show",e),r=t=>{var n;s(!1),null==(n=e.callback)||n.call(e,t)},u=n=>()=>{e.show&&(t(n),e.beforeClose?(c[n]=!0,a(e.beforeClose,{args:[n],done(){r(n),c[n]=!1},canceled(){c[n]=!1}})):r(n))},d=u("cancel"),m=u("confirm"),g=b((n=>{var l,a;n.target===(null==(a=null==(l=o.value)?void 0:l.popupRef)?void 0:a.value)&&({Enter:e.showConfirmButton?m:F,Escape:e.showCancelButton?d:F}[n.key](),t("keydown",n))}),["enter","esc"]),p=()=>{const t=n.title?n.title():e.title;if(t)return f("div",{class:ee("header",{isolated:!e.message&&!n.default})},[t])},w=t=>{const{message:n,allowHtml:o,messageAlign:l}=e,a=ee("message",{"has-title":t,[l]:l}),c=I(n)?n():n;return o&&"string"==typeof c?f("div",{class:a,innerHTML:c},null):f("div",{class:a},[c])},C=()=>{if(n.default)return f("div",{class:ee("content")},[n.default()]);const{title:t,message:o,allowHtml:l}=e;if(o){const e=!(!t&&!n.title);return f("div",{key:l?1:0,class:ee("content",{isolated:!e})},[w(e)])}},y=()=>n.footer?n.footer():"round-button"===e.theme?f(Q,{class:ee("footer")},{default:()=>[e.showCancelButton&&f(Z,{type:"warning",text:e.cancelButtonText||te("cancel"),class:ee("cancel"),color:e.cancelButtonColor,loading:c.cancel,disabled:e.cancelButtonDisabled,onClick:d},null),e.showConfirmButton&&f(Z,{type:"danger",text:e.confirmButtonText||te("confirm"),class:ee("confirm"),color:e.confirmButtonColor,loading:c.confirm,disabled:e.confirmButtonDisabled,onClick:m},null)]}):f("div",{class:[T,ee("footer")]},[e.showCancelButton&&f(h,{size:"large",text:e.cancelButtonText||te("cancel"),class:ee("cancel"),style:{color:e.cancelButtonColor},loading:c.cancel,disabled:e.cancelButtonDisabled,onClick:d},null),e.showConfirmButton&&f(h,{size:"large",text:e.confirmButtonText||te("confirm"),class:[ee("confirm"),{[S]:e.showCancelButton}],style:{color:e.confirmButtonColor},loading:c.confirm,disabled:e.confirmButtonDisabled,onClick:m},null)]);return()=>{const{width:t,title:n,theme:a,message:c,className:i}=e;return f(l,v({ref:o,role:"dialog",class:[ee([a]),i],style:{width:E(t)},tabindex:0,"aria-labelledby":n||c,onKeydown:g,"onUpdate:show":s},N(e,oe)),{default:()=>[p(),C(),y()]})}}});let ae,ce=H({},{title:"",width:"",theme:null,message:"",overlay:!0,callback:null,teleport:"body",className:"",allowHtml:!1,lockScroll:!0,transition:void 0,beforeClose:null,overlayClass:"",overlayStyle:void 0,messageAlign:"",cancelButtonText:"",cancelButtonColor:null,cancelButtonDisabled:!1,confirmButtonText:"",confirmButtonColor:null,confirmButtonDisabled:!1,showConfirmButton:!0,showCancelButton:!1,closeOnPopstate:!0,closeOnClickOverlay:!1});function se(e){return K?new Promise(((t,n)=>{ae||function(){const e={setup(){const{state:e,toggle:t}=s();return()=>f(le,v(e,{"onUpdate:show":t}),null)}};({instance:ae}=c(e))}(),ae.open(H({},ce,e,{callback:e=>{("confirm"===e?t:n)(e)}}))})):Promise.resolve()}e("s",(e=>se(H({showCancelButton:!0},e))))}}}));
import{o as z,p as M,a as W,P as q,c as V,m as Y,u as j}from"./index.d6bd2086.js";import{r as S,ad as G,f as D,w as J,H as s,s as T,c as A,e as Q,ac as R,K as X}from"./index.8c5864de.js";import{B as P}from"./index.3e2c8ef6.js";import{w as Z,b as ee,c as te,d as ne,e as oe,a as ae,B as le,f as se}from"./index.6925981e.js";import{c as O,t as k,w as I,e as h,n as re,u as ce,m as ie,p as ue,d as de,b as _,q as fe,k as me}from"./index.72a4dedb.js";import{r as Be,u as ge}from"./index.8ebbac1f.js";const he=(e,a)=>{const n=S(),o=()=>{n.value=te(e).height};return G(()=>{if(D(o),a)for(let l=1;l<=3;l++)setTimeout(o,100*l)}),z(()=>D(o)),J([Z,ee],o),n};function we(e,a){const n=he(e,!0);return o=>s("div",{class:a("placeholder"),style:{height:n.value?`${n.value}px`:void 0}},[o()])}const[N,E]=O("action-bar"),F=Symbol(N),ve={placeholder:Boolean,safeAreaInsetBottom:k};var Ce=T({name:N,props:ve,setup(e,{slots:a}){const n=S(),o=we(n,E),{linkChildren:l}=ne(F);l();const f=()=>{var m;return s("div",{ref:n,class:[E(),{"van-safe-area-bottom":e.safeAreaInsetBottom}]},[(m=a.default)==null?void 0:m.call(a)])};return()=>e.placeholder?o(f):f()}});const be=I(Ce),[ye,pe]=O("action-bar-button"),Pe=h({},Be,{type:String,text:String,icon:String,color:String,loading:Boolean,disabled:Boolean});var ke=T({name:ye,props:Pe,setup(e,{slots:a}){const n=ge(),{parent:o,index:l}=oe(F),f=A(()=>{if(o){const c=o.children[l.value-1];return!(c&&"isButton"in c)}}),m=A(()=>{if(o){const c=o.children[l.value+1];return!(c&&"isButton"in c)}});return ae({isButton:!0}),()=>{const{type:c,icon:B,text:g,color:C,loading:b,disabled:y}=e;return s(P,{class:pe([c,{last:m.value,first:f.value}]),size:"large",type:c,icon:B,color:C,loading:b,disabled:y,onClick:n},{default:()=>[a.default?a.default():g]})}}});const H=I(ke),[xe,i,v]=O("dialog"),Se=h({},M,{title:String,theme:String,width:re,message:[String,Function],callback:Function,allowHtml:Boolean,className:ce,transition:ie("van-dialog-bounce"),messageAlign:String,closeOnPopstate:k,showCancelButton:Boolean,cancelButtonText:String,cancelButtonColor:String,cancelButtonDisabled:Boolean,confirmButtonText:String,confirmButtonColor:String,confirmButtonDisabled:Boolean,showConfirmButton:k,closeOnClickOverlay:Boolean}),Te=[...W,"transition","closeOnPopstate"];var Oe=T({name:xe,props:Se,emits:["confirm","cancel","keydown","update:show"],setup(e,{emit:a,slots:n}){const o=S(),l=Q({confirm:!1,cancel:!1}),f=t=>a("update:show",t),m=t=>{var r;f(!1),(r=e.callback)==null||r.call(e,t)},c=t=>()=>{!e.show||(a(t),e.beforeClose?(l[t]=!0,V(e.beforeClose,{args:[t],done(){m(t),l[t]=!1},canceled(){l[t]=!1}})):m(t))},B=c("cancel"),g=c("confirm"),C=X(t=>{var r,u;if(t.target!==((u=(r=o.value)==null?void 0:r.popupRef)==null?void 0:u.value))return;({Enter:e.showConfirmButton?g:_,Escape:e.showCancelButton?B:_})[t.key](),a("keydown",t)},["enter","esc"]),b=()=>{const t=n.title?n.title():e.title;if(t)return s("div",{class:i("header",{isolated:!e.message&&!n.default})},[t])},y=t=>{const{message:r,allowHtml:u,messageAlign:d}=e,w=i("message",{"has-title":t,[d]:d}),p=fe(r)?r():r;return u&&typeof p=="string"?s("div",{class:w,innerHTML:p},null):s("div",{class:w},[p])},K=()=>{if(n.default)return s("div",{class:i("content")},[n.default()]);const{title:t,message:r,allowHtml:u}=e;if(r){const d=!!(t||n.title);return s("div",{key:u?1:0,class:i("content",{isolated:!d})},[y(d)])}},$=()=>s("div",{class:[se,i("footer")]},[e.showCancelButton&&s(P,{size:"large",text:e.cancelButtonText||v("cancel"),class:i("cancel"),style:{color:e.cancelButtonColor},loading:l.cancel,disabled:e.cancelButtonDisabled,onClick:B},null),e.showConfirmButton&&s(P,{size:"large",text:e.confirmButtonText||v("confirm"),class:[i("confirm"),{[le]:e.showCancelButton}],style:{color:e.confirmButtonColor},loading:l.confirm,disabled:e.confirmButtonDisabled,onClick:g},null)]),L=()=>s(be,{class:i("footer")},{default:()=>[e.showCancelButton&&s(H,{type:"warning",text:e.cancelButtonText||v("cancel"),class:i("cancel"),color:e.cancelButtonColor,loading:l.cancel,disabled:e.cancelButtonDisabled,onClick:B},null),e.showConfirmButton&&s(H,{type:"danger",text:e.confirmButtonText||v("confirm"),class:i("confirm"),color:e.confirmButtonColor,loading:l.confirm,disabled:e.confirmButtonDisabled,onClick:g},null)]}),U=()=>n.footer?n.footer():e.theme==="round-button"?L():$();return()=>{const{width:t,title:r,theme:u,message:d,className:w}=e;return s(q,R({ref:o,role:"dialog",class:[i([u]),w],style:{width:de(t)},tabindex:0,"aria-labelledby":r||d,onKeydown:C,"onUpdate:show":f},ue(e,Te)),{default:()=>[b(),K(),U()]})}}});let x;const De={title:"",width:"",theme:null,message:"",overlay:!0,callback:null,teleport:"body",className:"",allowHtml:!1,lockScroll:!0,transition:void 0,beforeClose:null,overlayClass:"",overlayStyle:void 0,messageAlign:"",cancelButtonText:"",cancelButtonColor:null,cancelButtonDisabled:!1,confirmButtonText:"",confirmButtonColor:null,confirmButtonDisabled:!1,showConfirmButton:!0,showCancelButton:!1,closeOnPopstate:!0,closeOnClickOverlay:!1};let Ae=h({},De);function _e(){({instance:x}=Y({setup(){const{state:a,toggle:n}=j();return()=>s(Oe,R(a,{"onUpdate:show":n}),null)}}))}function Ee(e){return me?new Promise((a,n)=>{x||_e(),x.open(h({},Ae,e,{callback:o=>{(o==="confirm"?a:n)(o)}}))}):Promise.resolve()}const $e=e=>Ee(h({showCancelButton:!0},e));export{$e as s};
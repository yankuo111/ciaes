import{ab as R,ag as b,c as D,r as p,e as T,a8 as _,J as B,w as C,ad as S,B as v,L as E,aa as N,f as P,a7 as L,ai as I}from"./index.8c5864de.js";import{o as M,e as H}from"./index.72a4dedb.js";var g=typeof window!="undefined",A=e=>e===window,O=(e,n)=>({top:0,left:0,right:e,bottom:n,width:e,height:n}),Z=e=>{const n=v(e);if(A(n)){const t=n.innerWidth,o=n.innerHeight;return O(t,o)}return n!=null&&n.getBoundingClientRect?n.getBoundingClientRect():O(0,0)};function nn(e){const n=R(e,null);if(n){const t=E(),{link:o,unlink:i,internalChildren:s}=n;o(t),b(()=>i(t));const r=D(()=>s.indexOf(t));return{parent:n,index:r}}return{parent:null,index:p(-1)}}function W(e){const n=[],t=o=>{Array.isArray(o)&&o.forEach(i=>{var s;I(i)&&(n.push(i),(s=i.component)!=null&&s.subTree&&(n.push(i.component.subTree),t(i.component.subTree.children)),i.children&&t(i.children))})};return t(e),n}var x=(e,n)=>{const t=e.indexOf(n);return t===-1?e.findIndex(o=>n.key!==void 0&&n.key!==null&&o.type===n.type&&o.key===n.key):t};function Y(e,n,t){const o=W(e.subTree.children);t.sort((s,r)=>x(o,s.vnode)-x(o,r.vnode));const i=t.map(s=>s.proxy);n.sort((s,r)=>{const c=i.indexOf(s),a=i.indexOf(r);return c-a})}function en(e){const n=T([]),t=T([]),o=E();return{children:n,linkChildren:s=>{N(e,Object.assign({link:a=>{a.proxy&&(t.push(a),n.push(a.proxy),Y(o,n,t))},unlink:a=>{const l=t.indexOf(a);n.splice(l,1),t.splice(l,1)},children:n,internalChildren:t},s))}}}function F(e){let n;S(()=>{e(),P(()=>{n=!0})}),L(()=>{n&&e()})}function tn(e,n,t={}){if(!g)return;const{target:o=window,passive:i=!1,capture:s=!1}=t;let r=!1,c;const a=d=>{if(r)return;const u=v(d);u&&!c&&(u.addEventListener(e,n,{capture:s,passive:i}),c=!0)},l=d=>{if(r)return;const u=v(d);u&&c&&(u.removeEventListener(e,n,s),c=!1)};b(()=>l(o)),_(()=>l(o)),F(()=>a(o));let h;return B(o)&&(h=C(o,(d,u)=>{l(u),a(d)})),()=>{h==null||h(),l(o),r=!0}}var f,m;function V(){if(!f&&(f=p(0),m=p(0),g)){const e=()=>{f.value=window.innerWidth,m.value=window.innerHeight};e(),window.addEventListener("resize",e,{passive:!0}),window.addEventListener("orientationchange",e,{passive:!0})}return{width:f,height:m}}var $=/scroll|auto|overlay/i,k=g?window:void 0;function U(e){return e.tagName!=="HTML"&&e.tagName!=="BODY"&&e.nodeType===1}function j(e,n=k){let t=e;for(;t&&t!==n&&U(t);){const{overflowY:o}=window.getComputedStyle(t);if($.test(o))return t;t=t.parentNode}return n}function on(e,n=k){const t=p();return S(()=>{e.value&&(t.value=j(e.value,n))}),t}var K=Symbol("van-field");function sn(e){const n=R(K,null);n&&!n.customValue.value&&(n.customValue.value=e,C(e,()=>{n.resetValidation(),n.validateWithTrigger("onChange")}))}function y(e,n){"scrollTop"in e?e.scrollTop=n:e.scrollTo(e.scrollX,n)}function z(){return window.pageYOffset||document.documentElement.scrollTop||document.body.scrollTop||0}function J(e){y(window,e),y(document.body,e)}const X=M();function rn(){X&&J(z())}const q=e=>e.stopPropagation();function an(e,n){(typeof e.cancelable!="boolean"||e.cancelable)&&e.preventDefault(),n&&q(e)}function cn(e){const n=v(e);if(!n)return!1;const t=window.getComputedStyle(n),o=t.display==="none",i=n.offsetParent===null&&t.position!=="fixed";return o||i}const{width:ln,height:un}=V(),w="van-hairline",dn=`${w}--top`,fn=`${w}--left`,pn=`${w}--surround`,vn=`${w}--top-bottom`,wn="van-haptics-feedback",hn=Symbol("van-form");function mn(e){const n=E();n&&H(n.proxy,e)}export{fn as B,K as C,hn as F,wn as H,mn as a,un as b,Z as c,en as d,nn as e,dn as f,j as g,on as h,cn as i,pn as j,z as k,vn as l,sn as m,F as o,an as p,rn as r,J as s,tn as u,ln as w};

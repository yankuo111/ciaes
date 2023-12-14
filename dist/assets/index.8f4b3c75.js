import{h as w,a as E,u as L,c as x,i as B}from"./index.6925981e.js";import{ab as C,s as R,r as h,w as T,aj as _,ad as N,H as r,f as j}from"./index.8c5864de.js";import{L as y}from"./index.d6bd2086.js";import{c as A,r as H,m as U,t as F,w as I}from"./index.72a4dedb.js";const K=Symbol(),M=()=>C(K,null),[V,o,Y]=A("list"),q={error:Boolean,offset:H(300),loading:Boolean,disabled:Boolean,finished:Boolean,errorText:String,direction:U("down"),loadingText:String,finishedText:String,immediateCheck:F};var z=R({name:V,props:q,emits:["load","update:error","update:loading"],setup(e,{emit:c,slots:a}){const d=h(e.loading),f=h(),g=h(),s=M(),m=w(f),n=()=>{j(()=>{if(d.value||e.finished||e.disabled||e.error||(s==null?void 0:s.value)===!1)return;const{direction:t}=e,l=+e.offset,i=x(m);if(!i.height||B(f))return;let u=!1;const v=x(g);t==="up"?u=i.top-v.top<=l:u=v.bottom-i.bottom<=l,u&&(d.value=!0,c("update:loading",!0),c("load"))})},b=()=>{if(e.finished){const t=a.finished?a.finished():e.finishedText;if(t)return r("div",{class:o("finished-text")},[t])}},S=()=>{c("update:error",!1),n()},k=()=>{if(e.error){const t=a.error?a.error():e.errorText;if(t)return r("div",{role:"button",class:o("error-text"),tabindex:0,onClick:S},[t])}},P=()=>{if(d.value&&!e.finished&&!e.disabled)return r("div",{class:o("loading")},[a.loading?a.loading():r(y,{class:o("loading-icon")},{default:()=>[e.loadingText||Y("loading")]})])};return T(()=>[e.loading,e.finished,e.error],n),s&&T(s,t=>{t&&n()}),_(()=>{d.value=e.loading}),N(()=>{e.immediateCheck&&n()}),E({check:n}),L("scroll",n,{target:m,passive:!0}),()=>{var t;const l=(t=a.default)==null?void 0:t.call(a),i=r("div",{ref:g,class:o("placeholder")},null);return r("div",{ref:f,role:"feed",class:o(),"aria-busy":d.value},[e.direction==="down"?l:i,P(),b(),k(),e.direction==="up"?l:i])}}});const Q=I(z);export{Q as L};

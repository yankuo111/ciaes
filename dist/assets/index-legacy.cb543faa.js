System.register(["./index-legacy.77e40bdf.js","./index-legacy.c9537be7.js","./index-legacy.e4e3e25f.js"],(function(o){"use strict";var e,l,n,t,r,s,a,c,i;return{setters:[function(o){e=o.s,l=o.H,n=o.ae},function(o){t=o.c,r=o.t,s=o.m,a=o.I,c=o.w},function(o){i=o.H}],execute:function(){const[u,d]=t("tag"),p={size:String,mark:Boolean,show:r,type:s("default"),color:String,plain:Boolean,round:Boolean,textColor:String,closeable:Boolean};var f=e({name:u,props:p,emits:["close"],setup(o,{slots:e,emit:t}){const r=o=>{o.stopPropagation(),t("close",o)},s=()=>{var n;const{type:t,mark:s,plain:c,round:u,size:p,closeable:f}=o,g={mark:s,plain:c,round:u};p&&(g[p]=p);const m=f&&l(a,{name:"cross",class:[d("close"),i],onClick:r},null);return l("span",{style:o.plain?{color:o.textColor||o.color,borderColor:o.color}:{color:o.textColor,background:o.color},class:d([g,t])},[null==(n=e.default)?void 0:n.call(e),m])};return()=>l(n,{name:o.closeable?"van-fade":void 0},{default:()=>[o.show?s():null]})}});o("T",c(f))}}}));
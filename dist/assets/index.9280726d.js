import{_ as v,s as f,P as k,Q as w,R as I,r as y,z as C,e as L,S as b,o as a,l as o,F as N,E as S,C as $,B as p,q as s,H as l,G as B,x as R,N as V,p as E,m as M,v as O}from"./index.8c5864de.js";const h=n=>(E("data-v-685467db"),n=n(),M(),n),P={class:"left"},z=["onClick"],A={class:"content flex flex_center"},F=h(()=>s("div",{class:"circle-top"},null,-1)),j=h(()=>s("div",{class:"circle-bottom"},null,-1)),q=f({__name:"LeftMenu",setup(n){var i,u;const c=k(),r=w(),_=((u=(i=I.children)==null?void 0:i.filter(e=>e.name==="V2Knowledge")[0])==null?void 0:u.children)||[],m=y(_.filter(e=>C.state.user.knowledgeAuthList.includes(e.name)));let d=L({activeIndex:"",activeOpends:[]});const x=e=>{d.activeIndex=e.fullPath.split("?")[0],d.activeOpends.push(e.matched[0].path)};return b(()=>{x(c)}),(e,J)=>{const g=V;return a(),o("div",P,[(a(!0),o(N,null,S(m.value,t=>(a(),o("div",{key:t.name},[t.meta.breadcrumb!==!1?(a(),o("div",{key:0,class:$(["route-item flex flex_center flex_just",{selected:p(c).fullPath.indexOf(t.path)!==-1}]),onClick:T=>p(r).push({path:t.path})},[s("div",A,[l(g,{"icon-class":t.meta.icon,className:"icon-route"},null,8,["icon-class"]),s("p",null,B(t.meta.title),1)]),F,j],10,z)):R("",!0)]))),128))])}}});var D=v(q,[["__scopeId","data-v-685467db"]]);const G={class:"knowledge flex"},H={class:"knowledge-left"},K={class:"knowledge-right flex_1"},Q=f({__name:"index",setup(n){return(c,r)=>{const _=O("router-view");return a(),o("div",G,[s("div",H,[l(D)]),s("div",K,[l(_)])])}}});var W=v(Q,[["__scopeId","data-v-15433f20"]]);export{W as default};

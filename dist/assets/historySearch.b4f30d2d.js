import{_ as V,s as b,e as H,r as T,o as n,l as r,q as o,H as c,T as f,y as $,A as v,I as C,F as d,E as g,G as q,x as z,D as J,Q as O,L as G,p as M,m as P}from"./index.8c5864de.js";import{I as Q}from"./index.72a4dedb.js";import{s as R}from"./index.d6bd2086.js";import"./index.6925981e.js";import{B as U}from"./index.3e2c8ef6.js";import{S as j,E as K}from"./index.dac30710.js";import{C as W}from"./index.8ebbac1f.js";import{s as X}from"./function-call.ed32c8d0.js";import"./index.5ec7378f.js";const x=i=>(M("data-v-68210cf1"),i=i(),P(),i),Y={class:"nav"},Z=x(()=>o("div",{style:{height:"54px"}},null,-1)),ee={class:"history-search"},te={class:"history-title flex flex_center flex_between"},se=x(()=>o("span",null,"\u5386\u53F2\u641C\u7D22",-1)),oe={class:"history-item"},ae=["onClick"],ne={class:"list-contaner"},re={key:0,class:"chat-empty"},ie=b({__name:"historySearch",setup(i){let _=O();const{appContext:k}=G(),p=k.config.globalProperties,e=H({search:"",historyList:[],historySearch:[],isShowHistoy:!0}),w=T("");let m=localStorage.getItem("historySearch");m&&(e.historySearch=JSON.parse(m));const h=()=>{!e.search||(e.historySearch.unshift(e.search),e.historySearch=[...new Set(e.historySearch)],localStorage.setItem("historySearch",JSON.stringify(e.historySearch)),p.axios.post(p.$api.searchSession,{query:e.search}).then(t=>{const{data:a,code:l,msg:u}=t.data;l==0?e.historyList=a||[]:R(u)}).finally(()=>{e.isShowHistoy=!1}))},y=()=>{e.isShowHistoy=!0,e.historyList=[]},B=t=>{t||y()},I=t=>{e.search=t,h()},D=t=>{X({title:"\u6E29\u99A8\u63D0\u793A",confirmButtonColor:"#22ad72",message:"\u786E\u8BA4\u5220\u9664\u641C\u7D22\u8BB0\u5F55\u4E48\uFF1F"}).then(()=>{e.historySearch=[],localStorage.removeItem("historySearch")}).catch(()=>{})},F=t=>{t?_.push({path:"/h5/v2/index",query:{sessionId:t}}):_.push("/h5/v2/index")};return(t,a)=>{const l=U,u=j,E=Q,A=K,L=W;return n(),r(d,null,[o("div",Y,[c(u,{modelValue:e.search,"onUpdate:modelValue":[a[0]||(a[0]=s=>e.search=s),B],onSearch:h,"show-action":"",shape:"round",onClear:y,placeholder:"\u641C\u7D22\u804A\u5929\u8BB0\u5F55",ref_key:"vanSearchComponent",ref:w},{action:f(()=>[c(l,{class:"search-btn",disabled:!e.search,loading:!1,onClick:h,round:"",type:"success",size:"small","loading-text":"\u641C\u7D22"},{default:f(()=>[$("\u641C\u7D22")]),_:1},8,["disabled"])]),_:1},8,["modelValue"])]),Z,v(o("div",ee,[o("div",te,[se,c(E,{name:"delete-o",color:"#a9a6a6",class:"search-icon",onClick:a[1]||(a[1]=s=>D(t.index))})]),o("div",oe,[(n(!0),r(d,null,g(e.historySearch,(s,S)=>(n(),r("span",{class:"tag",key:S,onClick:N=>I(s)},q(s),9,ae))),128))])],512),[[C,e.isShowHistoy]]),v(o("div",ne,[e.historyList.length===0?(n(),r("div",re,[c(A,{"image-size":"150",description:"\u6CA1\u6709\u627E\u5230\u76F8\u5173\u7684\u804A\u5929\u8BB0\u5F55"})])):z("",!0),(n(!0),r(d,null,g(e.historyList,(s,S)=>(n(),J(L,{key:s.saveTime,title:s.sessionName,onClick:N=>F(s.sessionId),icon:"chat-o","is-link":""},null,8,["title","onClick"]))),128))],512),[[C,!e.isShowHistoy]])],64)}}});var Se=V(ie,[["__scopeId","data-v-68210cf1"]]);export{Se as default};

import{_ as x,s as E,e as F,o,l as f,q as u,H as L,D as l,T as d,F as B,E as P,G as b,y as k,x as v,Q as I,L as S,p as V,m as N}from"./index.8c5864de.js";import{s as T}from"./index.d6bd2086.js";/* empty css              */import"./index.72a4dedb.js";/* empty css               */import"./index.6925981e.js";import{S as D,E as q}from"./index.dac30710.js";import{T as A}from"./index.21153b50.js";import{C as G}from"./index.8ebbac1f.js";import{L as $}from"./index.8f4b3c75.js";import"./index.5ec7378f.js";const K=r=>(V("data-v-7d959048"),r=r(),N(),r),U={class:"nav"},z=K(()=>u("div",{style:{height:"54px"}},null,-1)),H={class:"list-contaner"},Q={style:{"margin-right":"5px"}},R=E({__name:"knowledge",setup(r){let m=I();const{appContext:C}=S(),c=C.config.globalProperties,e=F({search:"",loading:!1,finished:!1,knowledgeList:[],totalCount:1,currentPage:1}),w=()=>{m.push("/h5/v2/knowledge/search")},h=()=>{e.loading=!0;let s={page:e.currentPage};return new Promise((a,p)=>{c.axios.post(c.$api.listKnowledgeTable,s).then(i=>{const{data:n,code:_,msg:g}=i.data;_==0?(n.currentPage===n.totalPage?e.finished=!0:e.currentPage++,e.knowledgeList=e.knowledgeList.concat(n.data),e.totalCount=n.totalCount,a(!0)):(e.totalCount=0,T(g),m.replace("/v2/login"),p())}).finally(()=>{e.loading=!1})})};h();const y=s=>{c.$router.push({path:"/h5/v2/knowledge/details",query:{id:s.uniqueId,name:s.knowledgeName}})};return(s,a)=>{const p=D,i=A,n=G,_=$,g=q;return o(),f("div",null,[u("div",U,[L(p,{modelValue:e.search,"onUpdate:modelValue":a[0]||(a[0]=t=>e.search=t),disabled:"",onClick:w,shape:"round",placeholder:"\u641C\u7D22\u77E5\u8BC6\u5E93"},null,8,["modelValue"])]),z,u("div",H,[e.knowledgeList.length!==0?(o(),l(_,{key:0,loading:e.loading,"onUpdate:loading":a[1]||(a[1]=t=>e.loading=t),finished:e.finished,"finished-text":"\u6CA1\u6709\u66F4\u591A\u4E86",onLoad:h},{default:d(()=>[(o(!0),f(B,null,P(e.knowledgeList,(t,j)=>(o(),l(n,{key:t.uniqueId,label:t.desc,onClick:J=>y(t),icon:"label-o","is-link":""},{title:d(()=>[u("span",Q,b(t.knowledgeName),1),t.type==="public"?(o(),l(i,{key:0,color:"#ffe1e1","text-color":"#ad0000",round:""},{default:d(()=>[k("\u516C\u5F00")]),_:1})):v("",!0),t.type==="private"?(o(),l(i,{key:1,type:"success",round:""},{default:d(()=>[k("\u79C1\u6709")]),_:1})):v("",!0)]),_:2},1032,["label","onClick"]))),128))]),_:1},8,["loading","finished"])):(o(),l(g,{key:1,"image-size":"150",description:"\u6682\u65E0\u77E5\u8BC6\u5E93\uFF0C\u8BF7\u8F6C\u79FB\u81F3PC\u7AEF\u521B\u5EFA\u3002"}))])])}}});var se=x(R,[["__scopeId","data-v-7d959048"]]);export{se as default};

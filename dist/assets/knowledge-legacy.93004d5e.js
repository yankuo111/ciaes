!function(){var e=document.createElement("style");e.innerHTML='@charset "UTF-8";.nav[data-v-7d959048]{position:fixed;top:0;left:0;width:100%;z-index:10;background-color:#fff}.nav[data-v-7d959048] .van-search__action{line-height:normal}.list-contaner[data-v-7d959048]{margin-top:10px}.list-contaner .search-icon[data-v-7d959048]{font-size:16px;line-height:inherit}.page_bottom[data-v-7d959048]{position:fixed;bottom:0;left:0;width:100%;height:50px;background:#22ad72;color:#fff;font-size:18px;border-top-left-radius:4px;border-top-right-radius:4px;padding-bottom:constant(safe-area-inset-bottom);padding-bottom:env(safe-area-inset-bottom)}.page_bottom span[data-v-7d959048]{margin-left:10px}[data-v-7d959048] .van-list{padding-bottom:70px}\n',document.head.appendChild(e),System.register(["./index-legacy.77e40bdf.js","./index-legacy.1dcd6f78.js","./index-legacy.f25f109a.js","./index-legacy.c9537be7.js","./index-legacy.f25f109a2.js","./index-legacy.e4e3e25f.js","./index-legacy.65023b5e.js","./index-legacy.cb543faa.js","./index-legacy.d4928f20.js","./index-legacy.2077b455.js","./index-legacy.3f603159.js"],(function(e){"use strict";var n,t,a,o,i,d,l,s,c,r,g,u,f,p,h,x,m,y,v,b,k,w,_,j;return{setters:[function(e){n=e._,t=e.s,a=e.e,o=e.o,i=e.l,d=e.q,l=e.H,s=e.D,c=e.T,r=e.F,g=e.E,u=e.G,f=e.y,p=e.x,h=e.Q,x=e.L,m=e.p,y=e.m},function(e){v=e.s},function(){},function(){},function(){},function(){},function(e){b=e.S,k=e.E},function(e){w=e.T},function(e){_=e.C},function(e){j=e.L},function(){}],execute:function(){const C={class:"nav"},L=(e=>(m("data-v-7d959048"),e=e(),y(),e))((()=>d("div",{style:{height:"54px"}},null,-1))),P={class:"list-contaner"},T={style:{"margin-right":"5px"}};e("default",n(t({__name:"knowledge",setup(e){let n=h();const{appContext:t}=x(),m=t.config.globalProperties,y=a({search:"",loading:!1,finished:!1,knowledgeList:[],totalCount:1,currentPage:1}),q=()=>{n.push("/h5/v2/knowledge/search")},z=()=>{y.loading=!0;let e={page:y.currentPage};return new Promise(((t,a)=>{m.axios.post(m.$api.listKnowledgeTable,e).then((e=>{const{data:o,code:i,msg:d}=e.data;0==i?(o.currentPage===o.totalPage?y.finished=!0:y.currentPage++,y.knowledgeList=y.knowledgeList.concat(o.data),y.totalCount=o.totalCount,t(!0)):(y.totalCount=0,v(d),n.replace("/v2/login"),a())})).finally((()=>{y.loading=!1}))}))};z();return(e,n)=>{const t=b,a=w,h=_,x=j,v=k;return o(),i("div",null,[d("div",C,[l(t,{modelValue:y.search,"onUpdate:modelValue":n[0]||(n[0]=e=>y.search=e),disabled:"",onClick:q,shape:"round",placeholder:"搜索知识库"},null,8,["modelValue"])]),L,d("div",P,[0!==y.knowledgeList.length?(o(),s(x,{key:0,loading:y.loading,"onUpdate:loading":n[1]||(n[1]=e=>y.loading=e),finished:y.finished,"finished-text":"没有更多了",onLoad:z},{default:c((()=>[(o(!0),i(r,null,g(y.knowledgeList,((e,n)=>(o(),s(h,{key:e.uniqueId,label:e.desc,onClick:n=>(e=>{m.$router.push({path:"/h5/v2/knowledge/details",query:{id:e.uniqueId,name:e.knowledgeName}})})(e),icon:"label-o","is-link":""},{title:c((()=>[d("span",T,u(e.knowledgeName),1),"public"===e.type?(o(),s(a,{key:0,color:"#ffe1e1","text-color":"#ad0000",round:""},{default:c((()=>[f("公开")])),_:1})):p("",!0),"private"===e.type?(o(),s(a,{key:1,type:"success",round:""},{default:c((()=>[f("私有")])),_:1})):p("",!0)])),_:2},1032,["label","onClick"])))),128))])),_:1},8,["loading","finished"])):(o(),s(v,{key:1,"image-size":"150",description:"暂无知识库，请转移至PC端创建。"}))])])}}}),[["__scopeId","data-v-7d959048"]]))}}}))}();

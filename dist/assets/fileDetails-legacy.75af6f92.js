!function(){var e=document.createElement("style");e.innerHTML=".knowledge[data-v-ebf6f03e]{background-color:#fff}.knowledge .search-input[data-v-ebf6f03e]{width:300px;margin-right:20px}.knowledge .header[data-v-ebf6f03e]{margin-bottom:10px;padding:25px 0 5px;position:relative;text-align:center;border-bottom:1px solid #f0f0f0}.knowledge .header .time[data-v-ebf6f03e]{color:#ccc;font-size:13px;margin-top:10px}.knowledge .header .tools[data-v-ebf6f03e]{position:absolute;right:0;top:10px}.knowledge .header .back[data-v-ebf6f03e]{position:absolute;left:0;top:30px;cursor:pointer}\n",document.head.appendChild(e),System.register(["./index-legacy.77e40bdf.js"],(function(e){"use strict";var t,o,n,a,d,l,i,r,c,s,u,f,m,p,g,v;return{setters:[function(e){t=e._,o=e.s,n=e.r,a=e.o,d=e.l,l=e.q,i=e.H,r=e.T,c=e.y,s=e.G,u=e.B,f=e.L,m=e.v,p=e.p,g=e.m,v=e.f}],execute:function(){const h=e=>(p("data-v-ebf6f03e"),e=e(),g(),e),x={class:"knowledge"},b={class:"header"},w={class:"time"},k=h((()=>l("div",{class:"tools"},null,-1))),y={class:"content"},I=h((()=>l("div",null,null,-1)));e("default",t(o({__name:"fileDetails",setup(e){const{appContext:t}=f(),o=t.config.globalProperties,p=n(),g=n(),h=o.$common.DateFormat;document.title=o.$route.query.name;const _=()=>{document.getElementById("iframeBox").height=document.documentElement.clientHeight-100+"px"};return new Promise(((e,t)=>{o.axios.post(o.$api.getKnowledgeFile,{knowledgeId:o.$route.query.knowledgeId,fileId:o.$route.query.fileId}).then((e=>{const{data:t,code:n,msg:a}=e.data;var d;0==n?(p.value=t.policyName,g.value=t.createTime,d=t.source_html,v((()=>{const e=document.getElementById("iframeBox");(e.contentDocument||e.contentWindow.document).write(d)}))):o.$message.error(a)})).finally((()=>{}))})),(e,t)=>{const o=m("H3");return a(),d("div",x,[l("div",b,[i(o,null,{default:r((()=>[c(s(p.value),1)])),_:1}),l("p",w,"上传时间："+s(u(h)("YYYY-mm-dd HH:MM:SS",g.value)),1),k]),l("div",y,[l("iframe",{id:"iframeBox",width:"100%",height:"100%",scrolling:"auto",onLoad:_,frameborder:"0"},null,32)]),I])}}}),[["__scopeId","data-v-ebf6f03e"]]))}}}))}();
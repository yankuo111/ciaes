!function(){function e(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);a&&(l=l.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,l)}return t}function a(e,a,t){return(a=function(e){var a=function(e,a){if("object"!=typeof e||null===e)return e;var t=e[Symbol.toPrimitive];if(void 0!==t){var l=t.call(e,a||"default");if("object"!=typeof l)return l;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===a?String:Number)(e)}(e,"string");return"symbol"==typeof a?a:String(a)}(a))in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function t(e,a,t,l,n,o,r){try{var i=e[o](r),d=i.value}catch(u){return void t(u)}i.done?a(d):Promise.resolve(d).then(l,n)}var l=document.createElement("style");l.innerHTML=".knowledge .search-input[data-v-4b7e04c0]{width:300px;margin-right:20px}.knowledge .header[data-v-4b7e04c0]{margin-bottom:10px;padding:10px 0 20px;border-bottom:1px solid #f0f0f0}.knowledge .content[data-v-4b7e04c0]{text-align:center}.knowledge .content .tips[data-v-4b7e04c0]{font-size:12px;color:#ea5e37;margin:10px 0 5px}.knowledge .content .table[data-v-4b7e04c0]{border-top:1px solid #f0f0f0;border-left:1px solid #f0f0f0;border-right:1px solid #f0f0f0}.knowledge .content[data-v-4b7e04c0] .el-table__row{cursor:pointer}.knowledge .content .pagination[data-v-4b7e04c0]{margin-top:40px;transform:translate(-80px)}.knowledge .form-content[data-v-4b7e04c0]{padding:10px 50px 30px 0}.knowledge .default-primary[data-v-4b7e04c0]{background:#12aa7e;border:none}.knowledge .default-primary-plain[data-v-4b7e04c0]{border:solid 1px #f1f5f4}.knowledge .default-primary-plain[data-v-4b7e04c0]:hover{background:#f1f5f4;color:#12aa7e}.knowledge[data-v-4b7e04c0] .el-input__wrapper.is-focus,.knowledge[data-v-4b7e04c0] .el-textarea__inner:hover{box-shadow:0 0 0 1px #12aa7e inset!important}\n",document.head.appendChild(l),System.register(["./index-legacy.77e40bdf.js"],(function(l){"use strict";var n,o,r,i,d,u,c,s,p,f,m,g,v,b,y,w,x,h,k,_,O,P,j,C;return{setters:[function(e){n=e._,o=e.s,r=e.r,i=e.e,d=e.o,u=e.l,c=e.q,s=e.H,p=e.T,f=e.B,m=e.U,g=e.y,v=e.V,b=e.W,y=e.X,w=e.$,x=e.G,h=e.a0,k=e.a1,_=e.a2,O=e.L,P=e.Q,j=e.v,C=e.a3}],execute:function(){const V={class:"knowledge"},$={class:"header flex flex_between"},T={style:{"padding-top":"20px"}},q={class:"content"},S={class:"tips flex flex_center"},I=o({__name:"manage",setup(l){const n=r(""),o=r(!1),I=r(),D=r(),{appContext:U}=O(),E=U.config.globalProperties,H=P(),K=r(1),N=r([]),Y=E.$common.DateFormat,z=r(0),B=r(!1),M=r(!1),R=i({name:"",desc:"",knowledgeId:""}),F=i({name:[{required:!0,message:"知识库名称不能为空",trigger:"blur"},{min:2,message:"知识库名称最少为两个字符",trigger:"blur"}],desc:[{required:!0,message:"知识库描述不能为空",trigger:"blur"},{min:2,message:"知识库描述最少为两个字符",trigger:"blur"}]}),L=()=>(B.value=!0,M.value=!1,new Promise(((e,a)=>{E.axios.post(E.$api.listKnowledgeTable,{page:K.value}).then((e=>{const{data:a,code:t,msg:l}=e.data;0==t&&a.data.length>0?(N.value=a.data,z.value=a.totalCount):E.$message.error(l)})).finally((()=>{B.value=!1}))})));L();const A=()=>(B.value=!0,new Promise(((e,a)=>{E.axios.post(E.$api.searchKnowledgeTable,{page:K.value,query:n.value}).then((e=>{const{data:a,code:t,msg:l}=e.data;0==t?(N.value=a.data,z.value=a.totalCount):E.$message.error(l)})).finally((()=>{B.value=!1}))}))),G=()=>{n.value&&(N.value=[],z.value=0,K.value=1,M.value=!0,A())},Q=e=>{K.value=e,W()},W=()=>{M.value?A():L()},X=function(){var e,a=(e=function*(){D.value&&(yield D.value.validate(((e,a)=>{e&&ee()})))},function(){var a=this,l=arguments;return new Promise((function(n,o){var r=e.apply(a,l);function i(e){t(r,n,o,i,d,"next",e)}function d(e){t(r,n,o,i,d,"throw",e)}i(void 0)}))});return function(){return a.apply(this,arguments)}}(),J=e=>e+1+10*(K.value-1),Z=e=>{console.log(e),H.push({path:"/v2/knowledge/upload",query:{id:e.uniqueId,name:e.knowledgeName,type:e.type}})},ee=()=>(B.value=!0,new Promise(((t,l)=>{E.axios.post(E.$api.updateKnowledge,function(t){for(var l=1;l<arguments.length;l++){var n=null!=arguments[l]?arguments[l]:{};l%2?e(Object(n),!0).forEach((function(e){a(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):e(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}({},R)).then((e=>{const{data:a,code:t,msg:l}=e.data;0==t?(W(),o.value=!1,E.$message.success("修改成功")):E.$message.error(l)})).finally((()=>{B.value=!1}))}))),ae=(e,a)=>{"edit"===e?(o.value=!0,R.name=a.knowledgeName,R.desc=a.desc,R.knowledgeId=a.uniqueId):"delete"===e&&C.confirm("您将删除此知识库，是否继续?","温馨提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((()=>{var e;e=a.uniqueId,B.value=!0,new Promise(((a,t)=>{E.axios.post(E.$api.deleteKnowledge,{knowledgeId:e}).then((e=>{const{data:a,code:t,msg:l}=e.data;0==t?(W(),E.$message.success("删除成功")):E.$message.error(l)})).finally((()=>{B.value=!1}))}))}))};return(e,a)=>{const t=j("el-icon"),l=j("el-input"),r=j("el-button"),i=j("el-form-item"),O=j("el-form"),P=j("el-dialog"),C=j("el-table-column"),U=j("el-table"),E=j("el-pagination");return d(),u("div",V,[c("div",$,[c("div",null,[s(l,{modelValue:n.value,"onUpdate:modelValue":a[0]||(a[0]=e=>n.value=e),class:"search-input",placeholder:"知识库搜索"},{prefix:p((()=>[s(t,{class:"el-input__icon"},{default:p((()=>[s(f(m))])),_:1})])),_:1},8,["modelValue"]),s(r,{class:"default-primary",type:"primary",icon:f(v),onClick:G},{default:p((()=>[g(" 搜索")])),_:1},8,["icon"]),s(r,{class:"default-primary-plain",icon:f(b),onClick:L},{default:p((()=>[g("重制")])),_:1},8,["icon"])]),c("div",null,[s(r,{class:"default-primary",type:"primary",onClick:a[1]||(a[1]=e=>f(H).push({path:"/v2/knowledge/new"})),icon:f(y)},{default:p((()=>[g("新建")])),_:1},8,["icon"])])]),s(P,{modelValue:o.value,"onUpdate:modelValue":a[6]||(a[6]=e=>o.value=e),title:"编辑知识库"},{default:p((()=>[s(O,{model:R,ref_key:"ruleFormRef",ref:D,"status-icon":"",rules:F,"label-width":"120px",class:"form-content"},{default:p((()=>[s(i,{label:"名称：",prop:"name"},{default:p((()=>[s(l,{modelValue:R.name,"onUpdate:modelValue":a[2]||(a[2]=e=>R.name=e)},null,8,["modelValue"])])),_:1}),s(i,{label:"描述：",prop:"desc"},{default:p((()=>[s(l,{modelValue:R.desc,"onUpdate:modelValue":a[3]||(a[3]=e=>R.desc=e),type:"textarea"},null,8,["modelValue"])])),_:1}),s(i,null,{default:p((()=>[c("div",T,[s(r,{class:"default-primary",type:"primary",onClick:a[4]||(a[4]=e=>X())},{default:p((()=>[g("确定")])),_:1}),s(r,{class:"default-primary-plain",onClick:a[5]||(a[5]=e=>{o.value=!1})},{default:p((()=>[g("取消")])),_:1})])])),_:1})])),_:1},8,["model","rules"])])),_:1},8,["modelValue"]),c("div",q,[c("p",S,[s(t,null,{default:p((()=>[s(f(w))])),_:1}),g("公开类型的知识库，仅支持查看，不支持下载，编辑，删除和上传等。")]),s(U,{ref_key:"multipleTableRef",ref:I,"cell-style":{textAlign:"center"},stripe:"",class:"table","header-cell-style":{"text-align":"center"},data:N.value,onRowClick:Z},{default:p((()=>[s(C,{type:"index",index:J,width:"100"}),s(C,{property:"knowledgeName",label:"名称"}),s(C,{property:"type",label:"类型"},{default:p((e=>[g(x("public"===e.row.type?"公开":"私有"),1)])),_:1}),s(C,{property:"desc",label:"描述"}),s(C,{label:"时间"},{default:p((e=>[g(x(f(Y)("YYYY-mm-dd HH:MM:SS",e.row.createTime)),1)])),_:1}),s(C,{label:"操作",width:"200"},{default:p((e=>[s(r,{class:"default-primary",type:"primary",size:"small",icon:f(h),disabled:"public"===e.row.type,onClick:k((a=>ae("edit",e.row)),["stop"])},{default:p((()=>[g("编辑")])),_:2},1032,["icon","disabled","onClick"]),s(r,{type:"danger",size:"small",icon:f(_),disabled:"public"===e.row.type,onClick:k((a=>ae("delete",e.row)),["stop"])},{default:p((()=>[g("删除")])),_:2},1032,["icon","disabled","onClick"])])),_:1})])),_:1},8,["data"]),s(E,{class:"pagination flex_just",background:"",layout:"total,prev, pager, next",onCurrentChange:Q,"hide-on-single-page":"",total:z.value},null,8,["total"])])])}}});l("default",n(I,[["__scopeId","data-v-4b7e04c0"]]))}}}))}();

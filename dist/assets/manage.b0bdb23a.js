import{_ as W,s as X,r as p,e as $,o as J,l as O,q as v,H as e,T as t,B as m,U as Z,y as d,V as ee,W as le,X as ae,$ as ue,G as T,a0 as te,a1 as K,a2 as ne,L as oe,Q as se,v as f,a3 as re}from"./index.8c5864de.js";const de={class:"knowledge"},ie={class:"header flex flex_between"},ce={style:{"padding-top":"20px"}},pe={class:"content"},me={class:"tips flex flex_center"},fe=X({__name:"manage",setup(_e){const E=p(""),F=p(!1),q=p(),w=p(),{appContext:I}=oe(),n=I.config.globalProperties,D=se(),C=p(1),y=p([]),P=n.$common.DateFormat,b=p(0),_=p(!1),B=p(!1),i=$({name:"",desc:"",knowledgeId:""}),R=$({name:[{required:!0,message:"\u77E5\u8BC6\u5E93\u540D\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{min:2,message:"\u77E5\u8BC6\u5E93\u540D\u79F0\u6700\u5C11\u4E3A\u4E24\u4E2A\u5B57\u7B26",trigger:"blur"}],desc:[{required:!0,message:"\u77E5\u8BC6\u5E93\u63CF\u8FF0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{min:2,message:"\u77E5\u8BC6\u5E93\u63CF\u8FF0\u6700\u5C11\u4E3A\u4E24\u4E2A\u5B57\u7B26",trigger:"blur"}]}),x=()=>(_.value=!0,B.value=!1,new Promise((a,l)=>{n.axios.post(n.$api.listKnowledgeTable,{page:C.value}).then(c=>{const{data:s,code:o,msg:r}=c.data;o==0&&s.data.length>0?(y.value=s.data,b.value=s.totalCount):n.$message.error(r)}).finally(()=>{_.value=!1})}));x();const A=()=>(_.value=!0,new Promise((a,l)=>{n.axios.post(n.$api.searchKnowledgeTable,{page:C.value,query:E.value}).then(c=>{const{data:s,code:o,msg:r}=c.data;o==0?(y.value=s.data,b.value=s.totalCount):n.$message.error(r)}).finally(()=>{_.value=!1})})),N=()=>{!E.value||(y.value=[],b.value=0,C.value=1,B.value=!0,A())},j=a=>{C.value=a,h()},h=()=>{B.value?A():x()},M=async()=>{!w.value||await w.value.validate((a,l)=>{a&&Y()})},S=a=>a+1+(C.value-1)*10,U=a=>{console.log(a),D.push({path:"/v2/knowledge/upload",query:{id:a.uniqueId,name:a.knowledgeName,type:a.type}})},L=a=>(_.value=!0,new Promise((l,c)=>{n.axios.post(n.$api.deleteKnowledge,{knowledgeId:a}).then(s=>{const{data:o,code:r,msg:k}=s.data;r==0?(h(),n.$message.success("\u5220\u9664\u6210\u529F")):n.$message.error(k)}).finally(()=>{_.value=!1})})),Y=()=>(_.value=!0,new Promise((a,l)=>{n.axios.post(n.$api.updateKnowledge,{...i}).then(c=>{const{data:s,code:o,msg:r}=c.data;o==0?(h(),F.value=!1,n.$message.success("\u4FEE\u6539\u6210\u529F")):n.$message.error(r)}).finally(()=>{_.value=!1})})),V=(a,l)=>{a==="edit"?(F.value=!0,i.name=l.knowledgeName,i.desc=l.desc,i.knowledgeId=l.uniqueId):a==="delete"&&re.confirm("\u60A8\u5C06\u5220\u9664\u6B64\u77E5\u8BC6\u5E93\uFF0C\u662F\u5426\u7EE7\u7EED?","\u6E29\u99A8\u63D0\u793A",{confirmButtonText:"\u786E\u5B9A",cancelButtonText:"\u53D6\u6D88",type:"warning"}).then(()=>{L(l.uniqueId)})};return(a,l)=>{const c=f("el-icon"),s=f("el-input"),o=f("el-button"),r=f("el-form-item"),k=f("el-form"),H=f("el-dialog"),g=f("el-table-column"),z=f("el-table"),G=f("el-pagination");return J(),O("div",de,[v("div",ie,[v("div",null,[e(s,{modelValue:E.value,"onUpdate:modelValue":l[0]||(l[0]=u=>E.value=u),class:"search-input",placeholder:"\u77E5\u8BC6\u5E93\u641C\u7D22"},{prefix:t(()=>[e(c,{class:"el-input__icon"},{default:t(()=>[e(m(Z))]),_:1})]),_:1},8,["modelValue"]),e(o,{class:"default-primary",type:"primary",icon:m(ee),onClick:N},{default:t(()=>[d(" \u641C\u7D22")]),_:1},8,["icon"]),e(o,{class:"default-primary-plain",icon:m(le),onClick:x},{default:t(()=>[d("\u91CD\u5236")]),_:1},8,["icon"])]),v("div",null,[e(o,{class:"default-primary",type:"primary",onClick:l[1]||(l[1]=u=>m(D).push({path:"/v2/knowledge/new"})),icon:m(ae)},{default:t(()=>[d("\u65B0\u5EFA")]),_:1},8,["icon"])])]),e(H,{modelValue:F.value,"onUpdate:modelValue":l[6]||(l[6]=u=>F.value=u),title:"\u7F16\u8F91\u77E5\u8BC6\u5E93"},{default:t(()=>[e(k,{model:i,ref_key:"ruleFormRef",ref:w,"status-icon":"",rules:R,"label-width":"120px",class:"form-content"},{default:t(()=>[e(r,{label:"\u540D\u79F0\uFF1A",prop:"name"},{default:t(()=>[e(s,{modelValue:i.name,"onUpdate:modelValue":l[2]||(l[2]=u=>i.name=u)},null,8,["modelValue"])]),_:1}),e(r,{label:"\u63CF\u8FF0\uFF1A",prop:"desc"},{default:t(()=>[e(s,{modelValue:i.desc,"onUpdate:modelValue":l[3]||(l[3]=u=>i.desc=u),type:"textarea"},null,8,["modelValue"])]),_:1}),e(r,null,{default:t(()=>[v("div",ce,[e(o,{class:"default-primary",type:"primary",onClick:l[4]||(l[4]=u=>M())},{default:t(()=>[d("\u786E\u5B9A")]),_:1}),e(o,{class:"default-primary-plain",onClick:l[5]||(l[5]=u=>{F.value=!1})},{default:t(()=>[d("\u53D6\u6D88")]),_:1})])]),_:1})]),_:1},8,["model","rules"])]),_:1},8,["modelValue"]),v("div",pe,[v("p",me,[e(c,null,{default:t(()=>[e(m(ue))]),_:1}),d("\u516C\u5F00\u7C7B\u578B\u7684\u77E5\u8BC6\u5E93\uFF0C\u4EC5\u652F\u6301\u67E5\u770B\uFF0C\u4E0D\u652F\u6301\u4E0B\u8F7D\uFF0C\u7F16\u8F91\uFF0C\u5220\u9664\u548C\u4E0A\u4F20\u7B49\u3002")]),e(z,{ref_key:"multipleTableRef",ref:q,"cell-style":{textAlign:"center"},stripe:"",class:"table","header-cell-style":{"text-align":"center"},data:y.value,onRowClick:U},{default:t(()=>[e(g,{type:"index",index:S,width:"100"}),e(g,{property:"knowledgeName",label:"\u540D\u79F0"}),e(g,{property:"type",label:"\u7C7B\u578B"},{default:t(u=>[d(T(u.row.type==="public"?"\u516C\u5F00":"\u79C1\u6709"),1)]),_:1}),e(g,{property:"desc",label:"\u63CF\u8FF0"}),e(g,{label:"\u65F6\u95F4"},{default:t(u=>[d(T(m(P)("YYYY-mm-dd HH:MM:SS",u.row.createTime)),1)]),_:1}),e(g,{label:"\u64CD\u4F5C",width:"200"},{default:t(u=>[e(o,{class:"default-primary",type:"primary",size:"small",icon:m(te),disabled:u.row.type==="public",onClick:K(Q=>V("edit",u.row),["stop"])},{default:t(()=>[d("\u7F16\u8F91")]),_:2},1032,["icon","disabled","onClick"]),e(o,{type:"danger",size:"small",icon:m(ne),disabled:u.row.type==="public",onClick:K(Q=>V("delete",u.row),["stop"])},{default:t(()=>[d("\u5220\u9664")]),_:2},1032,["icon","disabled","onClick"])]),_:1})]),_:1},8,["data"]),e(G,{class:"pagination flex_just",background:"",layout:"total,prev, pager, next",onCurrentChange:j,"hide-on-single-page":"",total:b.value},null,8,["total"])])])}}});var ve=W(fe,[["__scopeId","data-v-4b7e04c0"]]);export{ve as default};

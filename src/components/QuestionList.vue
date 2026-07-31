<template>

<div class="page">


<div class="header">


<div class="title">

📋 在线问答

<span>
{{questions.length}}
</span>

</div>



<button
class="ask-btn"
@click="emit('add')"
>

＋ 我要提问

</button>


</div>




<div class="table-box">


<div class="table-header">

<div>序号</div>

<div>问题</div>

<div>回答次数</div>

<div>最后修改</div>

<div>操作</div>


</div>





<div

class="row"

v-for="(q,index) in questions"

:key="q.id"

>


<div>
{{index+1}}
</div>



<div

class="question-title"

@click="emit('detail',q.id)"

>

{{q.title}}

</div>



<div>

<span class="count">

{{q.answer_count}}

</span>

</div>




<div>

{{q.update_time || '-'}}

</div>




<div>


<button

class="detail"

@click="emit('detail',q.id)"

>

查看

</button>



<button

class="edit"

@click="emit('edit',q)"

>

✏ 修改

</button>



<button

class="delete"

@click="emit('delete',q)"

>

🗑 删除

</button>



</div>


</div>


</div>


</div>


</template>



<script setup>


defineProps({

questions:{
    type:Array,
    default:()=>[]
}

})



const emit = defineEmits([

"add",

"detail",

"edit",

"delete"

])


</script>




<style scoped>


.page{

width:1200px;

margin:auto;

}



.header{

display:flex;

justify-content:space-between;

align-items:center;

margin-bottom:30px;

}



.title{

font-size:32px;

font-weight:bold;

}



.title span{

background:#e8f0ff;

padding:5px 15px;

border-radius:20px;

font-size:18px;

}



.table-box{

background:white;

border-radius:20px;

overflow:hidden;

}



.table-header,
.row{

display:grid;

grid-template-columns:

80px 1fr 150px 150px 250px;


align-items:center;

}



.table-header{

background:#f5f7fb;

padding:20px;

}



.row{

padding:20px;

border-bottom:1px solid #eee;

}



.question-title{

cursor:pointer;

}



.count{

background:#edf3ff;

color:#3971ff;

padding:8px 15px;

border-radius:20px;

}



button{

padding:8px 18px;

border:none;

border-radius:20px;

cursor:pointer;

margin-right:8px;

}



.detail{

background:#e8f3ff;

}



.edit{

background:#fff4d6;

}



.delete{

background:#ffe8e8;

}

</style>
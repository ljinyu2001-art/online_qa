<script setup>

import {
    ref,
    watch
} from "vue"


import {
    post
} from "../api/request"


const props = defineProps({

    visible:Boolean,

    question:Object

})


const emit = defineEmits([
    "close"
])


const answer=ref("")



async function submitAnswer(){


    if(!answer.value){

        alert("请输入回答")

        return

    }



    await post(
        "/answers/"+props.question.id,
        {
            content:answer.value
        }
    )



    answer.value=""



    alert("回答成功")


    emit("close")


}



</script>





<template>


<div
v-if="visible"
class="mask"
>


<div class="dialog">


<h2>
问题详情
</h2>



<h3>

{{question.title}}

</h3>



<p>

{{question.description}}

</p>





<hr>




<h3>
回答列表
</h3>




<div

v-if="
question.answers &&
question.answers.length
"

>


<div

class="answer"

v-for="a in question.answers"

:key="a.id"

>


{{a.content}}


</div>



</div>


<div v-else>

暂无回答

</div>





<hr>



<h3>
添加回答
</h3>



<textarea

v-model="answer"

placeholder="请输入回答"

></textarea>




<div>


<button
@click="submitAnswer"
>

提交回答

</button>



<button
@click="emit('close')"
>

关闭

</button>


</div>



</div>


</div>


</template>






<style scoped>


.mask{

position:fixed;

left:0;

top:0;

width:100%;

height:100%;

background:rgba(0,0,0,.4);

display:flex;

justify-content:center;

align-items:center;


}



.dialog{

width:600px;

background:white;

padding:30px;

border-radius:15px;


}



.answer{

background:#f5f7fa;

padding:15px;

margin:10px 0;

border-radius:8px;


}



textarea{

width:100%;

height:100px;

margin:15px 0;

padding:10px;


}



button{

padding:10px 20px;

margin-right:15px;

border:none;

border-radius:8px;

background:#409eff;

color:white;


}



</style>
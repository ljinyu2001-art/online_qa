<script setup>

import {ref} from "vue"

import {
    addQuestion
} from "../api/question"



defineProps({

    visible:Boolean

})


const emit=defineEmits([

    "close",

    "submit"

])



const title=ref("")

const description=ref("")



async function save(){


    if(!title.value){

        alert("请输入问题标题")

        return

    }



    await addQuestion({

        title:title.value,

        description:description.value

    })



    emit("submit")



    title.value=""

    description.value=""


}


</script>



<template>


<div
v-if="visible"
class="mask"
>


<div class="dialog">


<h2>
发布问题
</h2>



<input

v-model="title"

placeholder="问题标题"

/>



<textarea

v-model="description"

placeholder="问题描述"

/>




<div class="buttons">


<button
class="ok"
@click="save"
>
提交
</button>



<button
class="cancel"
@click="emit('close')"
>
取消
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

right:0;

bottom:0;


background:rgba(0,0,0,.45);


display:flex;

justify-content:center;

align-items:center;


}



.dialog{


width:450px;


background:white;


padding:30px;


border-radius:15px;


}



input,
textarea{


width:100%;


padding:12px;


margin:10px 0;


border:1px solid #ddd;


border-radius:8px;


}



textarea{


height:120px;


}



button{


padding:10px 25px;


border:none;


border-radius:20px;


cursor:pointer;


margin-right:15px;


}



.ok{


background:#409eff;

color:white;


}



.cancel{


background:#eee;


}


</style>
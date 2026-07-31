<script setup>


import {
    ref,
    watch
} from "vue"



import {
    updateQuestion
} from "../api/question"



const props=defineProps({

    visible:Boolean,

    question:Object

})



const emit=defineEmits([

"close",

"submit"

])



const title=ref("")

const description=ref("")



watch(

()=>props.question,

(q)=>{


    if(q){

        title.value=q.title

        description.value=q.description

    }


},

{
    immediate:true
}

)



async function save(){


    emit(

        "submit",

        {

            title:title.value,

            description:description.value

        }

    )


}



</script>



<template>


<div
v-if="visible"
class="mask"
>


<div class="dialog">


<h2>
修改问题
</h2>


<input
v-model="title"
/>



<textarea
v-model="description"
/>



<button
class="ok"
@click="save"
>
保存
</button>



<button
@click="emit('close')"
>
取消
</button>



</div>


</div>


</template>



<style scoped>


.mask{


position:fixed;

inset:0;

background:rgba(0,0,0,.45);


display:flex;

justify-content:center;

align-items:center;


}



.dialog{


background:white;

width:450px;

padding:30px;

border-radius:15px;


}



input,
textarea{

width:100%;

padding:12px;

margin:10px 0;

}



textarea{

height:120px;

}


.ok{

background:#409eff;

color:white;

}



button{

padding:10px 25px;

border:0;

border-radius:20px;

margin-right:15px;

}



</style>
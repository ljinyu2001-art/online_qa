<script setup>


const props=defineProps({

visible:Boolean,

question:Object

})



const emit=defineEmits([

"close",

"confirm"

])



function remove(){


emit("confirm")


}


</script>




<template>


<div

v-if="visible"

class="mask"

>


<div class="dialog">


<h2>
确认删除？
</h2>



<p>

{{question?.title}}

</p>



<button

class="danger"

@click="remove"

>

删除

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

z-index:9999;

}



.dialog{

background:white;

padding:30px;

border-radius:15px;

}



button{

padding:10px 25px;

margin:10px;

border-radius:20px;

border:0;

cursor:pointer;

}



.danger{

background:#f56c6c;

color:white;

}


</style>
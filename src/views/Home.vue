<template>


<h1>
在线问答系统
</h1>


<QuestionList

:questions="questions"

@add="showAdd=true"

@detail="detail"

@delete="remove"

/>



<AddQuestion

:visible="showAdd"

@close="showAdd=false"

@submit="save"

/>



<DetailDialog

:visible="showDetail"

:question="current"

@close="showDetail=false"

/>


</template>



<script setup>

import {
ref,
onMounted
} from "vue"


import QuestionList from "../components/QuestionList.vue"

import AddQuestion from "../components/AddQuestion.vue"

import DetailDialog from "../components/DetailDialog.vue"



import {
getQuestions,
getQuestion,
addQuestion,
deleteQuestion
}
from "../api/question"



const questions=ref([])


const showAdd=ref(false)

const showDetail=ref(false)


const current=ref({})



function load(){

getQuestions()
.then(res=>{

questions.value=res

})

}



onMounted(load)



function save(data){

addQuestion(data)
.then(()=>{

showAdd.value=false

load()

})

}



function detail(id){

getQuestion(id)
.then(res=>{

current.value=res

showDetail.value=true

})

}



function remove(id){

deleteQuestion(id)
.then(()=>{

load()

})

}


</script>
<script setup>


import {
ref,
onMounted
} from "vue"



import QuestionList from "../components/QuestionList.vue"


import AddQuestion from "../components/AddQuestion.vue"

import EditQuestion from "../components/EditQuestion.vue"

import DeleteDialog from "../components/DeleteDialog.vue"

import DetailDialog from "../components/DetailDialog.vue"



import {

getQuestions,

getQuestion,

addQuestion,

deleteQuestion,

updateQuestion

}

from "../api/question"




const questions=ref([])



const showAdd=ref(false)

const showEdit=ref(false)

const showDelete=ref(false)

const showDetail=ref(false)



const current=ref({})





async function load(){

    questions.value =
        await getQuestions()

}




async function save(data){

    await addQuestion(data)

    showAdd.value=false

    load()

}





async function detail(id){

    current.value =
        await getQuestion(id)

    showDetail.value=true

}





function edit(q){

    current.value=q

    showEdit.value=true

}





async function update(data){

    await updateQuestion(
        current.value.id,
        data
    )


    showEdit.value=false

    load()

}





function remove(q){

    console.log(
        "父组件收到删除:",
        q
    )


    current.value=q


    showDelete.value=true

}





async function confirmDelete(){


    await deleteQuestion(
        current.value.id
    )


    showDelete.value=false


    load()


}




onMounted(()=>{

    load()

})


</script>



<template>


<h1>
在线问答系统
</h1>



<QuestionList

:questions="questions"

@add="showAdd=true"

@detail="detail"

@edit="edit"

@delete="remove"

/>




<AddQuestion

:visible="showAdd"

@close="showAdd=false"

@submit="save"

/>




<EditQuestion

:visible="showEdit"

:question="current"

@close="showEdit=false"

@submit="update"

/>





<DeleteDialog

:visible="showDelete"

:question="current"

@close="showDelete=false"

@confirm="confirmDelete"

/>





<DetailDialog

:visible="showDetail"

:question="current"

@close="showDetail=false"

/>


</template>
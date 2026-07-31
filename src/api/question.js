import {
    get,
    post,
    put,
    del
} from "./request"



// 查询全部问题

export function getQuestions(){

    return get("/questions")

}



// 查询详情

export function getQuestion(id){

    return get(
        "/questions/"+id
    )

}



// 添加问题

export function addQuestion(data){

    return post(
        "/questions",
        data
    )

}



// 修改问题

export function updateQuestion(id,data){

    return put(
        "/questions/"+id,
        data
    )

}



// 删除问题

export function deleteQuestion(id){

    return del(
        "/questions/"+id
    )

}
const BASE_URL = "http://127.0.0.1:8000";


export async function get(url){

    const res = await fetch(
        BASE_URL + url
    );

    return await res.json();
}



export async function post(url,data){

    const res = await fetch(
        BASE_URL + url,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(data)
        }
    );


    return await res.json();

}



export async function put(url,data){

    const res = await fetch(
        BASE_URL + url,
        {
            method:"PUT",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(data)
        }
    );


    return await res.json();

}



export async function del(url){

    const res = await fetch(
        BASE_URL + url,
        {
            method:"DELETE"
        }
    );

    return await res.json();
}
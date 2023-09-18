import { useEffect } from "react";

export function TaskList(){
    useEffect(()=>{
        console.log("pagina creada")
    },[])
    return(
        <div>TaskList</div>
    )
}
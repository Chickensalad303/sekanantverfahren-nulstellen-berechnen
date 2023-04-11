
// var temp1 = 14
// var temp2 = 42
// var tempform = "12**i/51*1"


export function send_calc(ws, XminusOne, Xn, formula, until) {
    const message = {
        XminusOne: XminusOne,
        Xn: Xn,
        formula: formula,
        duration: until
    }
    
    ws.send(JSON.stringify(message))
    
}
export function wserror(ws){
    ws.addEventListener("error", (err) => {
        console.log(err)
    })

}
export function wsopen(ws){
    ws.addEventListener("open", () => {
        console.log("Websocket is open")

    })
    return true
}
export function wsclosed(ws){
    ws.addEventListener("close", () => {
        console.log("websocket is closed")
    })
}














export function removeElements(){
     //remove previous rows of calculation. if none then rows is empty and nothing happens

    var rows = document.querySelectorAll(".grid_item")
    for (var q = 0; q < rows.length; q++){
        rows[q].remove() 
    }
    var messages_to_remove = document.querySelectorAll("#user_message")
    for (var t = 0; t < messages_to_remove.length; t++){
        messages_to_remove[t].remove()
    }
}


function callZeroDivisonError(final_result, div_to_go_into){


    var msg_paragraph = document.createElement("p")
    var msg = document.createTextNode(`Ein präziseres Folgenglied ist nicht zu errechnen. Die Nulstelle ist: ${final_result}`)
    msg_paragraph.appendChild(msg)
    msg_paragraph.setAttribute("id", "user_message")
    div_to_go_into.appendChild(msg_paragraph)
    document.getElementById("messages").appendChild(div_to_go_into)
            
}

export function recieve_calc(ws){
    ws.addEventListener("message", (data) => {
        var event = JSON.parse(data.data)


        var values = event.result
          

        console.log(values)
        
        var iterations = 0
        var insert = document.createDocumentFragment()
        for (var i of values){
            iterations++
            var div = document.createElement("div")
            var paragraph1 = document.createElement("p")
            var paragraph2 = document.createElement("p")
            var paragraph3 = document.createElement("p")
            var text1 = document.createTextNode(`Xn+${iterations.toString()}`)
            var text2 = document.createTextNode("=")
            var text3 = document.createTextNode(i)
            
            
            paragraph1.appendChild(text1)
            paragraph2.appendChild(text2)
            paragraph3.appendChild(text3)
            
            div.setAttribute("class", "grid_item")
            div.appendChild(paragraph1);
            div.appendChild(paragraph2);
            div.appendChild(paragraph3);
            
            
            insert.appendChild(div)
            document.getElementById("grid_box").appendChild(insert)
            
        }

        if (event.error == 2){
            // console.log(event.current_value.toString())
            callZeroDivisonError(event.current_value.toString(), insert)
            return
            
        }
        
        
    })
}
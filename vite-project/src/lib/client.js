
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
}
export function wsclosed(ws){
    ws.addEventListener("close", () => {
        console.log("websocket is closed")
    })
}

export function recieve_calc(ws){
    ws.addEventListener("message", (data) => {
        var event = JSON.parse(data.data)
        var values = event.result
        console.log(values)



        var iterations = 0
        for (var i of values){
            iterations++
            var insert = document.createDocumentFragment()
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

        // for (var i of values){
        //     var div = document.createElement("div")
        //     div.setAttribute("class", "grid_item")
        //     div.appendChild(document.createTextNode("test"))
        // }
    })
}
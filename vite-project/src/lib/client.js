
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
        
        console.log(event.result)
    })
}
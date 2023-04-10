
var temp1 = 14
var temp2 = 42
var tempform = "12**i/51*1"

export function send_calc(ws, XminusOne, Xn, formula, until) {
    console.log(ws)
    const message = {
        XminusOne: XminusOne,
        Xn: Xn,
        formula: formula,
        duration: until
    }
    
    ws.send(JSON.stringify(message))
    

    


}


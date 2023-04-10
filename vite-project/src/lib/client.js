import WebSocket from "ws";

var temp1 = 14
var temp2 = 42
var tempform = "12**i/51*1"

function wsclient(XminusOne, Xn, form) {
    const ws = new WebSocket("ws://localhost:8001/");
    

    var message = {
        XminusOne: temp1,
        Xn: temp2,
        formula: tempform
    }

    ws.send(JSON.stringify(message))
    

}
wsclient()


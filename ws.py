import asyncio
import websockets



# asdg = "1/6 *i **3 - 1/2 * i **2 - 1/3"
# iterations = []
# def parse_formula(formula):
#     print(float(formula))

# def test(howLong, Xminusone, Xn):
#     iterations.append(Xminusone)
#     iterations.append(Xn)


#     for p in range(howLong):
#         try:
#             iterationsvorschrift = 

async def handler(ws):
    while True:
        try:
            message = await ws.recv()
            
        except websockets.ConnectionClosedOK:
            break
        print(message)


async def startServer():
    async with websockets.serve(handler, "", 8001): # inits server on port 8001. Everything recieved goes into the handler func
        await asyncio.Future() # makes it run forever, cuz server needs to be running, not stopping

if __name__ == "__main__":
    asyncio.run(startServer())



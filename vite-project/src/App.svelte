<script>

  import { send_calc, wserror, wsclosed, wsopen, recieve_calc, removeElements} from "./lib/client.js"
  //user input stored in these 
  var value = ""
  var x_minus_one = ""
  var x_n = ""
  var folgengl = ""
  
  //when hosting from rpi its not localhost but the rpi's ip adress 
  // var ws = new WebSocket("ws://localhost:8001/")

  var ws = new WebSocket("ws://192.168.178.40:8001")
  //init EventListeners
  wserror(ws)
    // wsclosed(ws)
    // wsopen(ws)
  recieve_calc(ws)

  function reconnect() {
    ws.close()
    ws = new WebSocket("ws://192.168.178.40:8001")
    setTimeout(() => {
      //idk why. Just dont change it
        if (wsopen(ws) == true){
          ws = new WebSocket("ws://192.168.178.40:8001")
          console.log("test")
          //for some reason have to do this because it stops listening for messages
          recieve_calc(ws)
          return
        }

      reconnect()
    }, 5000)
    
  }

  ws.addEventListener("close", () => {
    if (ws.readyState != ws.OPEN){
      reconnect()

    }
  })
  


  

  var folgengliede = (e) =>{
  folgengl = e.target.value
  }
  var inputformula = (e) =>{
    value = e.target.value
  }
  var minusOne = (e) => {
    x_minus_one = e.target.value
  }
  var n = (e) => {
    x_n = e.target.value
  }
    
    
  var parsedValue

    var calculate = () => {
      value = value.toLowerCase()
      if (value != "" && x_minus_one != "" && x_n != "" && folgengl != ""){
        if (value.includes("^") || value.includes("x")){
          parsedValue = value.replaceAll("^", "**")
          parsedValue = parsedValue.replaceAll("x", "i")
          
        }
        // console.log(parsedValue)
        
        removeElements()
        send_calc(ws, x_minus_one, x_n, parsedValue, folgengl)
      }else{
        console.log("its empty")
        return
      }
      

    }




    //need to create a div with class grid_item and, 3* <p> inside. all inside grid_box div
</script>

<main>

  <div class="header">
    <p>Note: for x to the power of y use: x^y <br>
    use x as the variable</p>
    
  </div>



  <div class="inputform">
    <div>
      <h1>anzahl folgenglieder</h1>
      <input type="text" id="folgen" on:input={folgengliede}>
    </div>
  </div>
  <div class="inputform">
    <div>
      <h1>X-1</h1>
      <input type="text" id="x_minus" on:input={minusOne}>
    </div>
    <div>
      <h1>Xn</h1>
      <input type="text" id="x_minus" on:input={n}>
    </div>
    <div>
      <h1>formula</h1>
      <input type="text" id="formula" on:input={inputformula}>
    </div>
  </div>

  
  <div class="calculateButton"><input type="button" value="calculate" on:click={calculate}></div>



  <div class="grid_box" id="grid_box">

  </div>
  <div class="user_messages" id="messages">

  </div>


</main>

<style>


</style>












<!-- <script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div>
    <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
      <img src={viteLogo} class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank" rel="noreferrer">SvelteKit</a>, the official Svelte app framework powered by Vite!
  </p>

  <p class="read-the-docs">
    Click on the Vite and Svelte logos to learn more
  </p>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style> -->

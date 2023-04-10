<script>
  //user input stored in these 
  var value = ""
  var x_minus_one
  var x_n
  var folgengl

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
      if (value != ""){
        if (value.includes("^")){
          parsedValue = value.replaceAll("^", "**")

        }
        if(value.includes("x")){
          parsedValue = value.replaceAll("x", "i")
        }
        console.log(parsedValue)

      }
    }


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

<script>
  import Canvas from './lib/Canvas.svelte'
  import AI from './lib/AI.svelte'
  
  const background = '#fff'
  const color = '#000'
</script>

<main class="background">
  <div>
  <h1> Digit Recognition </h1>
    <AI/>
    <Canvas/>
  </div>
</main>

<style>
  main {
    background-color: white;
  }
</style>

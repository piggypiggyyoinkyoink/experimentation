<script>
    import Header from "$lib/components/Header.svelte"; //convention is upper case
    let name = $state("Jamie"); //sveltelicious way of setting default value to a prop
    let fullName = $derived(name + " " + "Smith") //fullName is derived from name, i.e. updates whenever the value of name changes

    let status = $state("OPEN");

    function toggleStatus(){
        status = status === "OPEN"? "CLOSED" : "OPEN"; //toggles status between open and closed
    }
</script>

<Header {name}/>
<h2>{fullName}</h2>

<input type = "text" bind:value={name} /> <!-- variable name is auto updated to take the current value of the text field - awesome :) Can also bind variables to html elements -->
<p>The store is now {status}</p>
<button onclick={toggleStatus}>Toggle Status</button>
<!--

Alternative: 
<button {onclick}>Toggle Status</button>
Note: requires function in <script> to be called onclick() -> probably not ideal if you want multiple onclicks, but makes sense for small, simple modular components

Alternative 2: 
<button onclick = {()=>{
    status = status === "OPEN"? "CLOSED" : "OPEN";  //same as above, but with arrow function
}}>Toggle Status</button
>

-->
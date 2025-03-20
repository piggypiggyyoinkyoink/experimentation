<script>
    import {createState, ExampleState} from "$lib/modules/state.svelte"
    let {name} = $props();

    const myState = createState(); //implemented using a function (defined in state.svelte.js)
    const myState2 = new ExampleState(); //implemented using a class (eek), also defined in state.svelte.js



</script>

<div>
    
    <h1>{#if name}{name}{:else}User{/if}'s Form</h1>
    <button onclick = {myState.up}>{myState.value}</button>
    <button onclick = {() => myState2.up()}>{myState2.value}</button> <!-- Have to use a function () => when calling a method of a class used to define a state
    Also note myState.up when using the function; mystate.up() when using the class.-->
</div>
<style>
    div{
        background:coral;
    }
</style>
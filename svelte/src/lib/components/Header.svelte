<script>
    import {createState} from "$lib/modules/state.svelte"
    let {name} = $props();

    const myState = createState();


</script>

<div>
    
    <h1>{#if name}{name}{:else}User{/if}'s Form</h1>
    <button onclick = {myState.up}>{myState.value}</button>
</div>
<style>
    div{
        background:coral;
    }
</style>
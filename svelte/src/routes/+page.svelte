<script>
    import Header from "$lib/components/Header.svelte"; //convention is upper case
    
    let formState = $state({
        name: "",
        birthday:"",
        step:0,
        error:""
    });
</script>

<Header name = {formState.name} />
<main>
    <p> Step {formState.step + 1}</p>
    

    {#if formState.step === 0}
        <div>
            <label for = "name">Your name</label>
            <input type = "text" id = "name" bind:value={formState.name}>
        </div>
        <button onclick ={()=>{
            if(formState.name !== ""){
                formState.step += 1;
                formState.error = "";
            }else{
                formState.error = "Please write your name."
            }
        }}>Next</button>
    {:else if formState.step ===1}
    <div>
        <label for = "bday">Your birthday</label>
        <input type = "date" id = "bday" bind:value={formState.birthday}>
    </div>
    <button onclick ={()=>{
        if(formState.birthday !== ""){
            formState.step += 1;
            formState.error = "";
        }else{
            formState.error = "Please enter your birthday."
        }
    }}>Next</button>
    {/if}
    {#if formState.error !==""}
        <p class="error">{formState.error}</p>

    {/if}
</main>

<style> /*Note: the scope of these CSS styles is restricted to this component, not other components e.g. Header that are imported by it. Likewise, the scope is restricted to this component when other components import this one.*/
    div{
        background:aliceblue;
    }
    .error{
        color:red;
    }
    :global(div){ /*This is a CSS style with global scope, not always recommended*/
        color:rgb(51, 80, 55);
    }
</style>
<script>
    import Header from "$lib/components/Header.svelte"; //convention is upper case
    
    let formState = $state({
        answers:{},
        step:0,
        error:""
    });

    const questions = [
        {
            question: "What is your name?",
            id: "name",
            type: "text"
        },
        {
            question: "What's your birthday?",
            id: "birthday",
            type: "date"
        },
        {
            question: "What's your favorite colour?",
            id: "colour",
            type: "color"
        }
    ]

    function nextStep(id){
        if (formState.answers[id]){
            formState.step +=1;
            formState.error="";
        }else{
            formState.error = "Please fill out the form ";
        }
    }
</script>

<Header name = {formState.answers.name}/>
<main>
    {#if formState.step >= questions.length}
    <p>Thank you</p>
    {:else}
    <p> Step {formState.step + 1}</p>
    {/if}
    {#each questions as question, index (question.id)} <!-- question.id is a 'key' here. It is not needed for everything, but recommended when whatever is beig iterated through is dynamic. Index refers to the index of the loop, can be called anything, e.g. i-->
        {#if formState.step === index}
            {@render formStep(question)}
        {/if}
    {/each}

    <!-- Alternative:

    {#each questions as {id, question, type} (id)}
        {@render formStep({question, id, type})}
    {/each}

    -->
    {#if formState.error !==""}
        <p class="error">{formState.error}</p>

    {/if}
</main>


{#snippet formStep({question,id,type})}
<article>
    <div>
        <label for = {id}>{question}</label>
        <input {type} id = {id} bind:value={formState.answers[id]}/> <!--This creates a dictionary with key being the id for each field, and the value being the user inputted value-->
    </div>
    <button onclick={()=>nextStep(id)}>Next</button> <!--Next button calls nextStep function with current question id-->
</article>
{/snippet}
<!--{JSON.stringify(formState)} <!--To visualise what the above block is doing-->

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
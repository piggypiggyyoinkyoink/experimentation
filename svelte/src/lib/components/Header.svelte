<script>
    let {name} = $props();
</script>

<div>
    
    <h1>{#if name}{name}{:else}User{/if}'s Form</h1>
</div>
<style>
    div{
        background:coral;
    }
</style>
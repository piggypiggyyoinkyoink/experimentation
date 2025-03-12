<script>
    let {name, fakeName=null} = $props(); //fakeName has a default value null, so is an optional parameter
</script>

<div>
    
    <h1>{#if name}{name}{:else}User{/if}'s Form'</h1>
    
</div>
<!--
<h2>{name.replaceAll("a", "o") }</h2>

<p>{fakeName}</p>
-->
<style>
    div{
        background:coral;
    }
</style>
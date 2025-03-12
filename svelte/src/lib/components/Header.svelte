<script>
    let {name, children, secondChild} = $props(); //any children passed into this component are assigned to "children" by default, unles they are named snippets, e.g. secondChild
</script>

<div>
    
    <h1>{#if name}{name}{:else}User{/if}'s Form'</h1>
    {@render children()} <!-- rendering children passed to component -->
    <h3>{@render secondChild("Jonathan")}</h3><!-- rendering named second child-->
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
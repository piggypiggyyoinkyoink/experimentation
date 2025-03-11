<script>
    let {name, fakeName=null} = $props(); //fakeName has a default value null, so is an optional parameter
</script>

<h1>Hello {name}</h1>
<h2>{name.replaceAll("a", "o") }</h2>
<p>{fakeName}</p>
<style>

</style>
<script>
    let num = $state(0);
    let values = $derived.by(()=>{
        return{
            even: (['0', "2", "4", "6", "8"].includes(num.toString()[num.toString().length -1]) && (num % 1 == 0)),
            odd: (["1", "3", "5", "7", "9"].includes(num.toString()[num.toString().length -1])&& (num % 1 == 0)),
            multipleOf10: (num.toString()[num.toString().length -1] == 0 && (num % 1 == 0)),
            doubleVal: num * 2
        }
    })

    $effect(()=>{
        console.log(num.toString()[num.toString().length -1])
    })
</script>

<div>
    <label for = "num">Current Number:</label>
    <input type = "text" id = "num" bind:value={num}>
    <div>
        <h2>Even: { values.even }</h2>
        <h2>Odd: { values.odd }</h2>
        <h2>Multiple of 10: { values.multipleOf10 }</h2>
        <h2>Double Value: { values.doubleVal }</h2>
    </div>
</div>
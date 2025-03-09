<script>
    let count = $state({
        value: 0,
        note: "single digits",
    });
    setInterval(()=>{
        count.value++;
        if (count.value > 9){
            count.note = `${count.value.toString().length} digits`;
        }
    }, 1000);
</script>

<p>Count: {count.value} ({count.note})</p>
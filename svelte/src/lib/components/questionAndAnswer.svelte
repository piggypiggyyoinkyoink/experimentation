<script>
    function getRandomAnswer(){
        answers = ["Absolutely!", "Definitely", "Perhaps", "Let's see", "Not a chance", "Nope"]
        return answers[Math.floor(Math.random()*answers.length)]
    }
    let answers = ["Absolutely!", "Definitely", "Perhaps", "Let's see", "Not a chance", "Nope"]
    
    let { question = "is Jack gay?", answer=getRandomAnswer()} = $props();
    
</script>

<p> The answer to the question "{question}" is "{answer}".</p>
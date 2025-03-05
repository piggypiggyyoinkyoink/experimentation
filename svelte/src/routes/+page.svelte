<script>
    import Hello from "$lib/components/hello.svelte"
    import QuestionAndAnswer from "$lib/components/questionAndAnswer.svelte";
    function getAnswer(){
        let list = ["Yes", "Definitely", "Absolutely", "100%"]
        return list[Math.floor(Math.random()*list.length)]
    }
    let qa = {
        question: "Is Jack gay?",
        answer: getAnswer()
    };
</script>

<Hello />
<QuestionAndAnswer {...qa}/>
<QuestionAndAnswer/>

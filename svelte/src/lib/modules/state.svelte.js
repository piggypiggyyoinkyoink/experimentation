export class ExampleState{
    value = $state(0);

    up(){
        this.value ++;
    }
}

export function createState(){
    let value = $state(0);
    function up(){
        value ++;
    }
    return {
        //this returns getter and setter methods, as well as any other functions (i.e. up) corresponding to the reactive variable value(), which can then be accessed by any components importing this module.
        // If you dont want the value to be modified by external code directly, you can omit the set() function.

        //(this can be seen as being too much effort for what its worth)
        get value(){ 
            return value;
        },
        set value(newValue){
            value = newValue;
        },
        up
    };
}
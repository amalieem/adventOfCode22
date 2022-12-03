const fs = require("fs");
const priority = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ");

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;
    let lines = data.toString().split("\n");
    let items = [];
    for (const i of lines) {
        const len = i.length;
        let comp1 = i.substring(0, len/2);
        let comp2 = i.substring(len/2);
        for (const j of comp1) {
            let done = false;
            if (comp2.includes(j)) {
                items.push(j);
                done = true;
                break;
            }
            if (done) break;
        }
    }
    let sum = 0;
    for (const i of items) {
        sum += priority.indexOf(i) + 1;
    }
    console.log(sum);
});





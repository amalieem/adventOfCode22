const fs = require("fs");
const priority = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ");

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;
    let lines = data.toString().split("\n");
    let badges = []
  
    let group = [];
    for (const i of lines) {
        group.push(i);
        if (group.length == 3) {
            for (let c of group[0]) {
                if (group[1].includes(c) && group[2].includes(c)) {
                    badges.push(c);
                    break;
                }
            }
            group = [];
        }
    }
    
    let sum = 0;
    for (const i of badges) {
        sum += priority.indexOf(i) + 1;
    }
    console.log(sum);
});




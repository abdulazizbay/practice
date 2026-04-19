// B-TASK (Nodejs)

// Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda
//  qatnashgan raqamlarni sonini bizga return qilsin.

// MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.

// Yechim
function countDigits(a) {
  let counter = 0;
  for (let char of a) {
    if (char >= "0" && char <= "9") {
      counter++;
    }
  }
  return counter;
}

const result = countDigits("ad2a54y79wet0sfgb9");
console.log(result);


// ===========================================================================================================

/*  A-TASK (NodeJS)
        Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
        MASALAN countLetter("e", "engineer") 3ni return qiladi. 
*/

// function countLetter(letter, word) {
//   let counter = 0;
//   for (let a of word) {
//     if (a === letter) {
//       counter++;
//     }
//   }
//   return counter;
// }

// const result = countLetter("e", "engineer");
// console.log(result);

// function countLetter(letter, word) {
//   let counter = 0;
//   let list = [];
//   for (let l of word) {
//     list.push(l);
//   }
//   list.map((a) => {
//     if (letter === a) {
//       counter++;
//     }
//   });
//   return counter;
// }

// const result = countLetter("e", "engineer");
// console.log(result);

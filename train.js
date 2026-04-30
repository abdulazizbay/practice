
// F-TASK (NodeJS)

// Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir
//  hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
// MASALAN: getReverse("hello") return true return qilad

// function findDoublers(str) {
  
//   const letters_obj = {};
//   for (let i = 0; i < str.length; i++) {
   
    
//     if (letters_obj[str[i]]) {
//       return true
//     } else {
//       letters_obj[str[i]] = 1;
//     }
//   }
//   return false
// }

// console.log(findDoublers("hello"));

// E-TASK (NodeJS)

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function getReverse(str){
//   return str.split("").reverse().join("")
// }

// console.log(getReverse("hello"))

// D-TASK (NodeJS)

// Shunday function tuzingki unga integerlardan iborat array pass bolsin va
//  function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
// MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.

// function getHighestIndex(arr){
//   const sortedArray = [...arr].sort((a,b)=> b - a)
//   const biggest = sortedArray[0]

//   return arr.indexOf(biggest)

// }

// const result = getHighestIndex([5, 21, 12, 21, 8])
// console.log(result );

// // C-TASK (NodeJS)

// // Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
// // MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;

// function checkContent(a, b) {
//   if (a.length !== b.length) {
//     return false
//   }

//   const sortedA = a.split("").sort().join("");
//   const sortedB = b.split("").sort().join("");

//   return sortedA === sortedB;
// }

// const result = checkContent("mitgroup", "gmtiprou");
// console.log(result);
// ===========================================================================================================
// B-TASK (Nodejs)

// Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda
//  qatnashgan raqamlarni sonini bizga return qilsin.

// MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.

// Yechim
// function countDigits(a) {
//   let counter = 0;
//   for (let char of a) {
//     if (char >= "0" && char <= "9") {
//       counter++;
//     }
//   }
//   return counter;
// }

// const result = countDigits("ad2a54y79wet0sfgb9");
// console.log(result);

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

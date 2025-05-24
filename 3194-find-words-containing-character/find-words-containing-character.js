/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function(words, x) {
    let final = [];
    for (let i = 0; i < words.length; i++){
        if (words[i].includes(x)){
            final.push(i);
        }
    }
    return final;
    
};
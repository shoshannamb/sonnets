function getBigrams(arr) {
  var wordMap = new Object();
  for (i = 0; i< arr.length; i++) {
    for (n = 0; n < arr[i].length-1; n++) {
      var bigram = arr[i].slice(n,n+2);
      if (wordMap.hasOwnProperty(bigram[0])) { //If the first word in the bigram is already in WordMap
        if(bigram[1] in wordMap[bigram[0]]) { //If the second word is already registered as a bigram
          wordMap[bigram[0]][bigram[1]]++;
        }
        else {
          wordMap[bigram[0]][bigram[1]] = 1;
        }
      }
      else {
        wordMap[bigram[0]] = new Object();
        wordMap[bigram[0]][bigram[1]] = 1;
      }
    }
  }
  for (key in wordMap) {
    var maxCount = 0;
    var maxKey = [];
    for (var word in wordMap[key]) {
      if (wordMap[key][word] > maxCount) {
        maxCount = wordMap[key][word];
      }
    }
    for (word in wordMap[key]) {
      if (wordMap[key][word] >= maxCount) {
        maxKey.push(word);
      }
    }
    wordMap[key] = maxKey;
  }
  return wordMap;
}

var comBigrams = getBigrams(comLines);
var tragBigrams = getBigrams(tragLines);

function writeLine(startingWord) {
  
}

var sonnetCounter = 154;

document.getElementById("scramblerButton").addEventListener("click", function() {
  document.getElementById("sonnetBody").innerHTML = writeSonnet();
  document.getElementById("buttonText").innerHTML = "Write Another Sonnet";
  sonnetCounter++;
  document.getElementById("sonnetNumber").innerHTML = "Sonnet " + sonnetCounter;
});

function writeSonnet() {
  var sonnet = "";
  var sonnetRhymes = [];
  var sonnetSources = [];
  //Select random couplets for the sonnet
  for (var i = 0; i < 7; i++) {
    var n = Math.floor(Math.random()*rhymeCouplets.length);
    sonnetRhymes.push(rhymeCouplets[n]);
    sonnetSources.push(Math.floor(n/7));
  }
  //Construct a string "sonnet" comprised of the sonnet in the correct format
  for (var i = 0; i < 5; i = i+2) {
    sonnet += sonnetRhymes[i][0] + "<br>" + sonnetRhymes[i+1][0] + "<br>" +
    sonnetRhymes[i][1] + "<br>" + sonnetRhymes[i+1][1]+ "<br>";
  }
  sonnet += "&nbsp;&nbsp;&nbsp;" + sonnetRhymes[6][0] + "<br>" + "&nbsp;&nbsp;&nbsp;" + sonnetRhymes[6][1];
  sonnetSources = sonnetSources.filter(function(elem, index, self) {
    return index == self.indexOf(elem);
  })
  //Add a sentence to "sonnet" listing the original source sonnets
  var sources = "<p class=\"sources\">Sonnet lines from";
  for (i = 0; i < sonnetSources.length; i++) {
    if (i < sonnetSources.length - 1) {
      sources += " " + sonnetSources[i] + ",";
    }
    else {
      sources += " & " + sonnetSources[i] + ".";
    }
  }
  return sonnet + sources;
}

function countAgainst(inStr, compStr) {
  result = 0;

  for (i=0; i<inStr.length; i++) {
    if (compStr.includes(inStr[i])) {
      result++
    }
  }

  return result;
}

function countVowels(str) {
  return countAgainst(str, 'aeiou');
}

function countConstanants(str) {
  return countAgainst(str, 'bcdfghjklmnpqrstvwxy');
}

function getSolutions() {
  var input = document.getElementById('lettersInput').value;
  input = input.toLowerCase();

  vowels = countVowels(input);
  consts = countConstanants(input);

  if (consts < 4) {
    document.getElementById('errorMsg').innerHTML = 'ERROR: There are less than 4 consonants. Countdown rules enforce that the letters must have at least 3 vowels and 4 consonants';
  } else if (vowels < 3) {
    document.getElementById('errorMsg').innerHTML = 'ERROR: There are less than 3 vowels. Countdown rules enforce that the letters must have at least 3 vowels and 4 consonants';
  } else {
    document.getElementById('errorMsg').innerHTML = '';

    const Http = new XMLHttpRequest();
    const url='http://localhost:5000/letters?input='+input;
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange=(e)=>{
      if (Http.readyState==4 && Http.status==200) {
        response = JSON.parse(Http.responseText);

        solutions = response['data']['solutions'];

        document.getElementById('resultLabel').innerHTML = 'The highest words for ' + input + ' are:'

        resultsString = '';
        for (i=0; i<solutions.length; i++) {
          resultsString += '<li>'+solutions[i]+' ('+solutions[i].length+')'+'</li>';
        }
        document.getElementById('resultList').innerHTML = resultsString;
      }
    }
  }
}


// Listen for enter key
var textbox = document.getElementById('lettersInput');
textbox.addEventListener("keyup", function(event) {
  event.preventDefault();
  if (event.keyCode == 13) {
    document.getElementById("btnSolve").click();
  }
});

function getSolution() {
  var num1 = document.getElementById('num1').value;
  var num2 = document.getElementById('num2').value;
  var num3 = document.getElementById('num3').value;
  var num4 = document.getElementById('num4').value;
  var num5 = document.getElementById('num5').value;
  var num6 = document.getElementById('num6').value;

  var target = document.getElementById('target').value;

  if (num1=="" ||
      num2=="" ||
      num3=="" ||
      num4=="" ||
      num5=="" ||
      num6=="" ||
      target=="") {
    document.getElementById('errorMsg').innerHTML = 'ERROR: Please enter all numbers';
  } else {
    document.getElementById('errorMsg').innerHTML = '';

    startingNumbers = [num1,num2,num3,num4,num5,num6]

    const Http = new XMLHttpRequest();
    const url='http://localhost:5000/numbers?numbers='+startingNumbers+'&target='+target;
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange=(e)=>{
      if (Http.readyState==4 && Http.status==200) {
        response = JSON.parse(Http.responseText);

        path = response['data']['solutionPath'];
        console.log(path);

        pathString = '<tr><th>Operation</th><th>Creates</th>';
        for (i=0; i<path.length; i++) {
          pathString += '<tr><td>' + path[i][0] + '</td><td>' + path[i][1] + '</td></tr>'
        }

        document.getElementById('pathTable').innerHTML = pathString;
      }
    }
  }
}

var a = prompt(); // input number
var sum = 0; // variable to hold sum of factors
var temp = Math.floor(Math.sqrt(a)); // square root floored 
for (var i = 2 ; i <= temp ; i++) { // loop to go through every element till the square root
	if (a % i == 0) { 
		sum = sum + i + a/i; // adding i and a/i since both are factors
	}
}
if(a > 1) {	//if greater than 1 then 1 is also a factor
	sum++;
}
if(a == temp * temp) { //if a perfect square then square root is counted twice
	sum -= temp;
}
if (sum == a) {	//if sum=a then it is perfect
	document.write('YES');
}
else {
	document.write('NO'); // else it is not perfect
}
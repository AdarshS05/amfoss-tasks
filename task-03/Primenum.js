const readline = require('readline');
const prime= readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
prime.question('n=', (n) => {
	n = parseInt(n);
	for (let  a= 2; a<n-1; a++) {
		let k = 0;
		for (let i = 2; i <=a / 2; i++) {
			if (a%i === 0){
				k++;
			}
		}	
		if (k<= 0) {
			console.log(a);
		}
	}
	
	prime.close();
});


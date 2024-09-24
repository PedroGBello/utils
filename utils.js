const { BsCloudFog } = require("react-icons/bs");

function capitalize(text) {
	return text
		.split(" ")
		.map((word) => {
			return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
		})
		.join(" ");
}

function arraySwap(array) {
	const firstValue = array[0];
	const lastValue = array[array.length - 1];
	array[0] = lastValue;
	array[array.length - 1] = firstValue;
	return array;
}

function addNum(array, num = 1) {
	const result = [];
	for (let i = 0; i < array.length; i++) {
		result.push(array[i] + num);
	}
	return result;
}

function addArrays(array1, array2) {
	const result = [];
	for (let i = 0; i < array1.length; i++) {
		result.push(array1[i] + array2[i]);
	}
	return result;
}

function wordsCount(words) {
	const result = {};
	for (let i = 0; i < words.length; i++) {
		const word = words[i];
		if (!result[word]) {
			result[word] = 1;
		} else {
			result[word] += 1;
		}
	}
	return result;
}

/*
	// const previousWhole = Math.floor(sqrt);
	// range of whole nums from 0 to previous:
	// const range = [...Array(previousWhole + 1).keys()];
	// range of prime nums from 2 to previous:
	// const primes = filterPrimes(range);
*/

function isPrime(param) {
	// Numbers less or equal to 1 are not prime:
	if (param <= 1) return false;
	const sqrt = param ** 0.5;
	for (let i = 2; i <= sqrt; i++) {
		if (param % i === 0) {
			return false;
		}
	}
	return true;
}

function filterPrimes(param) {
	return param.filter(isPrime);
}

function getFactors(param) {
	const factors = [];
	for (let i = 2; i <= param; i++) {
		// If i is a factor of num:
		while (param % i === 0) {
			isPrime(i) && factors.push(i);
			// Divide by i to check further factors:
			param /= i;
		}
	}
	return factors;
}
console.log(getFactors(360));
console.log(isPrime(31));

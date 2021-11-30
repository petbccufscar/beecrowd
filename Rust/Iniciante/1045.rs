use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let tokens = buffer.split_whitespace();

	let mut numbers: Vec<f64> = tokens.map(|v| v.parse().unwrap()).collect();
	numbers.sort_by(|a, b| b.partial_cmp(a).unwrap());

	let a: f64 = numbers[0];
	let b: f64 = numbers[1];
	let c: f64 = numbers[2];

	if a >= (b + c) {
		println!("NAO FORMA TRIANGULO");
	} else if a.powf(2.0) == (b.powf(2.0) + c.powf(2.0)) {
		println!("TRIANGULO RETANGULO");
	} else if a.powf(2.0) > (b.powf(2.0) + c.powf(2.0)) {
		println!("TRIANGULO OBTUSANGULO");

		if (a == b && a != c) || (a == c && a != b) || (b == c && b != a) {
			println!("TRIANGULO ISOSCELES");
		}
	} else if a.powf(2.0) < (b.powf(2.0) + c.powf(2.0)) {
		println!("TRIANGULO ACUTANGULO");

		if a == b && a != c || a == c && a != b || b == c && b != c {
			println!("TRIANGULO ISOSCELES");
		}

		if a == b && b == c {
			println!("TRIANGULO EQUILATERO");
		}
	}

	Ok(())
}
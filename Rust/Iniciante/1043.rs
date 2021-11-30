use std::io;
use std::error::Error;

fn eh_triangulo(a: &f64, b: &f64, c: &f64) -> bool {
	(*a + *b) > *c && (*a + *c) > *b && (*b + *c) > *a
}

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let a: f64 = tokens.next().unwrap().parse()?;
	let b: f64 = tokens.next().unwrap().parse()?;
	let c: f64 = tokens.next().unwrap().parse()?;

	if eh_triangulo(&a, &b, &c) {
		let perimetro: f64 = a + b + c;
		println!("Perimetro = {:.1}", perimetro);
	} else {
		let area: f64 = (a + b) / 2.0 * c;
		println!("Area = {:.1}", area);
	}

	Ok(())
}
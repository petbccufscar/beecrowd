use std::io;
use std::error::Error;

const PI: f64 = 3.14159;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let mut tokens = buffer.split_whitespace();

	let a: f64 = tokens.next().unwrap().parse()?;
	let b: f64 = tokens.next().unwrap().parse()?;
	let c: f64 = tokens.next().unwrap().parse()?;

	let triangulo: f64 = a * c / 2.0;
	let circulo: f64 = PI * c.powf(2.0);
	let trapezio: f64 = (a + b) / 2.0 * c;
	let quadrado: f64 = b.powf(2.0);
	let retangulo: f64 = a * b;

	println!("TRIANGULO: {:.3}", triangulo);
	println!("CIRCULO: {:.3}", circulo);
	println!("TRAPEZIO: {:.3}", trapezio);
	println!("QUADRADO: {:.3}", quadrado);
	println!("RETANGULO: {:.3}", retangulo);

	Ok(())
}
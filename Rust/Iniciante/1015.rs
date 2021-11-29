use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let x1: f64 = tokens.next().unwrap().parse()?;
	let y1: f64 = tokens.next().unwrap().parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let x2: f64 = tokens.next().unwrap().parse()?;
	let y2: f64 = tokens.next().unwrap().parse()?;

	let distancia: f64  = ((x2 - x1).powf(2.0) + (y2 - y1).powf(2.0)).sqrt();

	println!("{:.4}", distancia);

	Ok(())
}
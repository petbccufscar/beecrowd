use std::io;
use std::error::Error;

const PI: f64 = 3.14159;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();
	
	stdin.read_line(&mut buffer)?;
	let r: f64 = buffer.trim().parse()?;

	let a: f64 = r * r * PI;

	println!("A={:.4}", a);

	Ok(())
}
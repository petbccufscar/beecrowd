use std::io;
use std::error::Error;

const PI: f64 = 3.14159;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let r: i64 = buffer.trim().parse()?;

	let volume: f64 = 4.0/3.0 * PI * r.pow(3) as f64;

	println!("VOLUME = {:.3}", volume);

	Ok(())
}
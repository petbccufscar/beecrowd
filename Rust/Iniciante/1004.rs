use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let a: i64 = buffer.trim().parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let b: i64 = buffer.trim().parse()?;

	let prod: i64 = a * b;

	println!("PROD = {}", prod);

	Ok(())
}
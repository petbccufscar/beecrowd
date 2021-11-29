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

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let c: i64 = buffer.trim().parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let d: i64 = buffer.trim().parse()?;

	let diferenca: i64 = a * b - c * d;

	println!("DIFERENCA = {}", diferenca);

	Ok(())
}
use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let salary: f64 = buffer.trim().parse()?;
	
	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let bonus: f64 = buffer.trim().parse()?;

	let total: f64 = salary + bonus * 0.15;

	println!("TOTAL = R$ {:.2}", total);

	Ok(())
}
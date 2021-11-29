use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let number: i64 = buffer.trim().parse()?;
	
	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let hours: f64 = buffer.trim().parse()?;
	
	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let value: f64 = buffer.trim().parse()?;

	let salary: f64 = hours * value;

	println!("NUMBER = {}", number);
	println!("SALARY = U$ {:.2}", salary);

	Ok(())
}
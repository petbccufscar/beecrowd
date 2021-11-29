use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut dias: i64 = buffer.trim().parse()?;

	let anos: i64 = dias / 365;
	dias %= 365;

	let meses: i64 = dias / 30;
	dias %= 30;

	println!("{} ano(s)", anos);
	println!("{} mes(es)", meses);
	println!("{} dia(s)", dias);

	Ok(())
}
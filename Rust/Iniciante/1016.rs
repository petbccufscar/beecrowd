use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let distancia: i64 = buffer.trim().parse()?;

	let tempo: i64 = distancia * 2;

	println!("{} minutos", tempo);

	Ok(())
}
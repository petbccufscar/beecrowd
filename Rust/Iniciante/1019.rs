use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut segundos: i64 = buffer.trim().parse()?;

	let mut minutos: i64 = segundos / 60;
	segundos %= 60;

	let horas = minutos / 60;
	minutos %= 60;

	println!("{}:{}:{}", horas, minutos, segundos);

	Ok(())
}
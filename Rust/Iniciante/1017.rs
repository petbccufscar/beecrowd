use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let tempo: i64 = buffer.trim().parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let velocidade: i64 = buffer.trim().parse()?;

	let distancia: i64 = tempo * velocidade;
	let litros: f64 = distancia as f64 / 12.0;

	println!("{:.3}", litros);

	Ok(())
}
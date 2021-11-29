use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	let mut total: f64 = 0.0;

	for _ in 0..2 {
		buffer.clear();
		stdin.read_line(&mut buffer)?;

		let mut tokens = buffer.split_whitespace();

		let _ = tokens.next();
		let qt: f64 = tokens.next().unwrap().parse()?;
		let value: f64 = tokens.next().unwrap().parse()?;

		total += qt * value;
	}

	println!("VALOR A PAGAR: R$ {:.2}", total);

	Ok(())
}
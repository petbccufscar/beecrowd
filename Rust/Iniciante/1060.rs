use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	let mut contador = 0;

	for _ in 0..6 {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		
		let n: f64 = buffer.trim().parse()?;

		if n > 0.0 {
			contador += 1;
		}
	}

	println!("{} valores positivos", contador);

	Ok(())
}
use std::io;
use std::error::Error;

// Incompleto

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	loop {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		let mut tokens = buffer.split_whitespace();

		let x: i64 = tokens.next().unwrap().parse()?;
		let y: i64 = tokens.next().unwrap().parse()?;

		if x == y {
			break;
		}

		if x < y {
			println!("Crescente");
		} else if x > y {
			println!("Decrescente");
		}
	}

	Ok(())
}
use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let a: i64 = tokens.next().unwrap().parse()?;
	let b: i64 = tokens.next().unwrap().parse()?;

	if a % b == 0 || b % a == 0 {
		println!("Sao Multiplos");
	} else {
		println!("Nao sao Multiplos");
	}

	Ok(())
}
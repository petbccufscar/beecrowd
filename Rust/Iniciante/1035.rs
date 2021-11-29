use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let a: i64 = tokens.next().unwrap().parse()?;
	let b: i64 = tokens.next().unwrap().parse()?;
	let c: i64 = tokens.next().unwrap().parse()?;
	let d: i64 = tokens.next().unwrap().parse()?;

	if b > c && d > a && (c + d) > (a + b) && c > 0 && d > 0 && (a % 2) == 0 {
		println!("Valores aceitos");
	} else {
		println!("Valores nao aceitos");
	}

	Ok(())
}
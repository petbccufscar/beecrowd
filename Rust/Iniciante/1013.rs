use std::io;
use std::error::Error;

fn maior(a: i64, b: i64) -> i64 {
	return (a + b + (a - b).abs()) / 2;
}

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let a: i64 = tokens.next().unwrap().parse()?;
	let b: i64 = tokens.next().unwrap().parse()?;
	let c: i64 = tokens.next().unwrap().parse()?;

	let m: i64 = maior(a, maior(b, c));

	println!("{} eh o maior", m);

	Ok(())
}
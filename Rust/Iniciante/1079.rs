use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let n: i64 = buffer.trim().parse()?;

	for _ in 0..n {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		let mut tokens = buffer.split_whitespace();

		let a: f64 = tokens.next().unwrap().parse()?;
		let b: f64 = tokens.next().unwrap().parse()?;
		let c: f64 = tokens.next().unwrap().parse()?;

		let media: f64 = (2.0 * a + 3.0 * b + 5.0 * c) / 10.0;

		println!("{:.1}", media);
	}

	Ok(())
}
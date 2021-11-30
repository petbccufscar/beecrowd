use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let mut n: i64 = buffer.trim().parse()?;

	n |= 1;

	for _ in 0..6 {
		println!("{}", n);
		n += 2;
	}

	Ok(())
}
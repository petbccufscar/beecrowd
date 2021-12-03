use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let n: i64 = buffer.trim().parse()?;

	for i in 1..10001 {
		if i % n == 2 {
			println!("{}", i);
		}
	}

	Ok(())
}
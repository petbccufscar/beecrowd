use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let n: i64 = buffer.trim().parse()?;

	for i in 2..n+1 {
		if i % 2 == 0 {
			println!("{}^2 = {}", i, i.pow(2));
		}
	}

	Ok(())
}